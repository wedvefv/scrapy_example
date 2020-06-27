# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
from scrapy.pipelines.files import FilesPipeline
from urlparse import urlparse
# 解析url得到http， 域名， path， 参数

from os.path import basename, dirname, join
# basename 文件名
# dirname 除了文件名的其余部分

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
        

# 重写文件名
class MyFilesPipeline(FilesPipeline):
	def file_path(self, request, response=None, info=None):
		path = urlparse(request.url).path # 域名之后的部分，不含参数
		# 取斜杠分割的最后一个是文件名，倒数第二个部分是目录名（分类）
		x = join(basename(dirname(path)), basename(path))
		return x



