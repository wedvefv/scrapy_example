#encoding=utf8

import scrapy
from scrapy.linkextractors import LinkExtractor 

from ..items import MatItem

class MatSpider(scrapy.Spider):
	name = "matplot"
	allowed_domains = ["matplotlib.org"]
	start_urls = ['http://matplotlib.org/examples/index.html']

	def parse(self, response):
		le = LinkExtractor(restrict_css="div.toctree-wrapper", deny="/index.html$")
		links = le.extract_links(response)
		for link in links:
			yield scrapy.Request(url=link.url, callback=self.parse_detail)

	
	def parse_detail(self, response):
		href = response.css('a.reference.external::attr(href)').extract_first()
		url = response.urljoin(href)
		print url
		mat = MatItem()
		mat["file_urls"] = [url]
		return mat