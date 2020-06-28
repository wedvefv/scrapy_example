#encoding=utf8

import scrapy,json
from scrapy.linkextractors import LinkExtractor 

from ..items import MatItem

class MatSpider(scrapy.Spider):
	name = "image"
	allowed_domains = ["image.so.com"]
	BASE_URL="https://image.so.com/zjl?ch=art&sn=%d&listtype=new&temp=1"
	start_index = 0
	MAX_DOWNLOAD_NUM = 1000
	start_urls = [BASE_URL % 0]

	def parse(self, response):
		infos = json.loads(response.body.decode("utf-8"))
		yield {'image_urls': [info["imgurl"] for info in infos['list']]}

		self.start_index += infos['count']
		if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
			yield scrapy.Request(self.BASE_URL % self.start_index)