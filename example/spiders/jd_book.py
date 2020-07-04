# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
from ..items import JdbookItem
#爬去京东商品中的书籍信息, 使用splash的execute端点模拟js操作
# lua代码 模拟js
lua_script = '''
function main(splash)
	splash:go(splash.args.url)
	splash:wait(2)
	splash:runjs("document.getElementsByClassName('page')[0]")
	splash:wait(2)
	return splash:html()
end
'''

class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    allowed_domains = ['search.jd.com']
    #start_urls = ['http://search.jd.com/']
    base_url = "https://search.jd.com/Search?keyword=python"


    def start_requests(self):
        yield Request(self.base_url, callback=self.parse_url)

    def parse_url(self, response):
        # print response.text
        total = int(float(response.css('span#J_resCount::text').re_first("\d+\.?\d+")) * 10000)
        # // 是向下取整
        pageNum = total // 60 + (1 if total%60 else 0)
        # 构造页面的url， 向splash的execute接口发送请求解析
        for i in xrange(pageNum):
            # 京东每一页的page都是page奇数1，3，5，7  
            url = '%s&page=%s' %(self.base_url, 2*i + 1)
            yield SplashRequest(url, endpoint='execute', 
                args={'lua_source': lua_script},
                cache_args = ['lua_source'])

    def parse(self, response):
        for sel in response.css("ul.gl-warp.clearfix > li.gl-item"):
            item = JdbookItem()
            item["name"] =  sel.css("div.p-name").xpath(".//em/text()").extract_first()
            item["price"] = sel.css("div.p-price").xpath(".//i/text()").extract_first()
            yield item
            
