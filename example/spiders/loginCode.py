# -*- coding: utf-8 -*-
import scrapy
from io import BytesIO
import pytesseract
from scrapy.http import Request,FormRequest

# 当前爬虫文件只是框架,照书抄的，没有实际网站操作过
'''
class LoginCodeSpider(scrapy.Spider):
	name = 'login_captcha'

	login_url = "http://xxx.com/login"
	ser = "liu@xxx.com"
	password = "123232"

	# 登录之后的操作, 比如取爬去一个页面
	def super_requests(self):
		url = "http://example.webscraping.com/places/default/user/profile?_next=/places/default/index"
		return  Request(url, callback=self.parse)


	def start_requests(self):
		yield Request(self.login_url, callback=self.login, dont_filter=true)

	def login(self, reponse):
		''' 登录页面的解析函数，也是提取验证码的函数'''
		login_response = response.meta.get('login_response')
		if not login_response:
			code_url = response.css('label.field.prepend-icon').extract_first()
			code_url = response.urljoin(code_url)
			yield Request(code_url, 
							callback=self.login, 
							meta={"login_response":response},
							dont_filter=true)
		else:
			formdata = {
				"email": self.user,
				"password": self.password,
				"code": self.get_captcha_by_OCR(response.body)
			}
			yield FormRequest.from_response(login_response,
				callback=self.parse,
				fomdata=formdata,
				dont_filter=true)

	def parse(self, response):
		info = json.loads(response.text)
		if info["error"] == '0':
			logger.info("login success.")
			yield self.super_requests()

	


	def login(self, response):
		fd = {
			"email": "447060492@qq.com",
			"password": "123456"
		}
		yield FormRequest.from_response(response, formdata=fd, callback=self.parse_login)
	

	def parse_login(self, response):
		# print response.text
		info = json.loads(response.text)
		if info["error"] == '0':
			logger.info("login success")
			return  self.super_requests()

		logger.info("login failed")
		return self.start_requests()

	
	# 识别验证码
	def get_captcha_by_OCR(self, data):
		img = Image.open(BytesIO(data))
		img = img.convert("L") # 图片转为黑白
		code = pytesseract.image_to_string(img)
		img.close()
		return code 

	# 使用验证码api识别
	def get_captcha_by_network(self ,data):
		import request
		url = 'http://ali-checkcode.showapi.com/checkcode'
		appcode = "f23cca37f287418a90e2f922649273c4"

		form = {}
		form["convert_to_jpg"] = '0'
		form["img_base64"] = base64.b64encode(data)
		form["typeId"] = '3040'
		headers = {}
		headers["Authorization"] = "APPCODE "+ appcode
		response = requests.post(url, headers = headers, data=formdata)
		res = response.json()

		if res["showapi_res_code"] == 0:
			return ret["showapi_res_body"]["result"]
		return ""

'''