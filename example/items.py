# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy,os


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field() 
    review_rating = scrapy.Field() 
    review_num = scrapy.Field() 
    upc = scrapy.Field()
    stock = scrapy.Field()
    
class MatItem(scrapy.Item):
	file_urls = scrapy.Field()
	files = scrapy.Field()
	

class ImageItem(scrapy.Item):
	image_urls = scrapy.Field()
	image = scrapy.Field()

class JdbookItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()