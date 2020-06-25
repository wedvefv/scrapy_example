# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy 

class ExamplePipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

	# from_crawler 是生成pipeline对象是调用 ，
	# 类似init函数, 返回的是对象cls是类本身
	@classmethod
	def from_crawler(cls, crawler):
		cls.DB_URI = crawler.settings.get("MONGO_DB_URI")
		cls.DB_NAME = crawler.settings.get("MONGO_DB_NAME")
		return cls()


	def open_spider(self, spider):
		self.client = pymongo.MongoClient(self.DB_URI)
		self.db = self.client[self.DB_NAME]


	def close_spider(self, spider):
		self.client.close()

		
	def process_item(self, item, spider):
		coll = self.db[spider.name]
		post = dict(item) if isinstance(item, scrapy.item.Item) else item
		coll.insert(post)
		return item
        

