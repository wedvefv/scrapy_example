from scrapy.selector import Selector
from scrapy.http import HtmlResponse



body = '''
<html>
   <head>
<base href='http://example.com/' />
        <title>Example website</title>
   </head>
<body>
<div id='images-1' style="width: 1230px;">
	<a href='image1.html'>Name: Image 1 </a> <br/> 
	<a href='image2.html'>Name: Image 2 </a> <br/>
	<a href='image3.html'>Name: Image 3 </a> <br/>
</div>

<div id='images-2' class='small'>
	<a href='image4.html'>Name: Image 4 </a> <br/>
	<a href='image5.html'>Name: Image 5 </a> <br/>
</div>
   </body>
</html>>
   </body>
</html>
'''


res = HtmlResponse(url='http://www.example.com', body=body)
print res.css('a').extract()
print '\n' * 2
print res.css('a:nth-child(1)').css('a::text').extract()