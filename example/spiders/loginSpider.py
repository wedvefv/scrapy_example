# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class LoginspiderSpider(scrapy.Spider):
	name = 'loginSpider'
	allowed_domains = ["example.webscraping.com"]
	def super_requests(self):
		url = "http://example.webscraping.com/places/default/user/profile?_next=/places/default/index"
		return  Request(url, callback=self.parse)


	def start_requests(self):
		url = "http://example.webscraping.com/places/default/user/login?_next=/places/default/index"
		yield Request(url, callback=self.login)


	def login(self, response):
		fd = {
			"email": "447060492@qq.com",
			"password": "123456"
		}
		yield FormRequest.from_response(response, formdata=fd, callback=self.parse_login)
	

	def parse_login(self, response):
		print "----"
		# print response.text
		if 'ming' in response.text:
			print "login in success!"
			yield self.super_requests()


	# 访问profile页，提取个人信息
	def parse(self, response):
		keys = response.css("td.w2p_fl>label::text").extract()
		values = response.css("td.w2p_fw::text").extract()
		print keys
		print values

