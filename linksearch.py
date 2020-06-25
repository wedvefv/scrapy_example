#encoding=utf8
import urllib2
from scrapy.http import HtmlResponse

#  提取网站中的链接
# https://www.runoob.com/bootstrap/bootstrap-forms.html
#html1 = open("example1.html").read() # example1.html 是任意一个html 本地文件
req = urllib2.Request("https://www.runoob.com/bootstrap/bootstrap-forms.html")
html1 = urllib2.urlopen(req).read()

response =HtmlResponse(url="http://example1.com",body=html1)

from scrapy.linkextractors import LinkExtractor
le = LinkExtractor()
links = le.extract_links(response)


#for link in links:
    #print link.url


##  正则表达式提取链接
# allow 参数接受一个正则规则
# deny  表示正则相反的规则
# allow_domains 允许的域名列表
# deny_domains 排除指定的域名列表
# restrict_xpaths 选择xpath指定路径下的链接
# restrict_css 是一个选择器或选择器列表
# tags 指定html标签，attrs指定属性名
# process_value 指定回调处理函数

pattern = './django/.+\.html$' # django  开头然后 html 结尾
le = LinkExtractor(deny=pattern)
links = le.extract_links(response)
#for x in links:
    #print x.url



xpath = "//div[@class='shang_info']"
le = LinkExtractor(restrict_xpaths=xpath)
links = le.extract_links(response)
#for x in links:
#    print x.url

css = "p.fieldset" 
le = LinkExtractor(restrict_css=css)
links = le.extract_links(response)
#for x in links:
#    print x.url


tag = "script"
le = LinkExtractor(tags=tag,attrs='src')
links = le.extract_links(response)
for x in links:
    print x.url




