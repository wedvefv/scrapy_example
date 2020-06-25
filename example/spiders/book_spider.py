# -*- coding: utf-8 -*-
import scrapy,os
from scrapy.linkextractors import LinkExtractor
from ..items import ExampleItem 

class BookSpiderSpider(scrapy.Spider):
	name = 'book_spider'
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']

	def parse(self, response):
		# item_list = []
		# for book in response.css('article.product_pod'):
		# 	item = ExampleItem()
		# 	item["name"] = book.xpath("./h3/a/@title").extract()[0] #_first()
		# 	price = book.xpath("./div[2]/p[1]/text()").extract()[0]
		# 	item["price"] = price 
		# 	item_list.append(item)
		
		# next_url = response.css('ul.pager li.next a::attr(href)').extract()[0]
		# if next_url:
		# 	print "====",next_url
		# return item_list

		# 提取当前也的链接
		le = LinkExtractor(restrict_css="article.product_pod h3") # 这下面的每本书的链接
		for link in le.extract_links(response):
			#print link.url
			yield scrapy.Request(link.url, callback=self.parse_book)

		le = LinkExtractor(restrict_css="ul.pager li.next")
		links = le.extract_links(response)
		if links:
			print links[0].url, "+++++"
			yield scrapy.Request(links[0].url, callback=self.parse)
	
	def parse_book(self, response):
		# 提取信息
		item = ExampleItem()
		sel = response.css("div.product_main")
		item["name"] = sel.xpath("./h1/text()").extract_first()
		item["price"] = sel.xpath("./p[1]/text()").extract()[0]
		#item["review_rating"] = sel.xpath('./p[3]/@class').re_first("star-rating ([A-Za-z]+)")
		item["review_rating"] = sel.css('p.star-rating::attr(class)').re_first("star-rating ([A-Za-z]+)")
		print item, "==================="

	