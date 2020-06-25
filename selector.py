#encoding=utf8

# 使用选择器对象

from scrapy.selector import Selector

text = '''
<html>
    <body>
        <h1> hello world</h1>
        <h1> hello world</h1>
        <b>hello python </b>
        <ul>
            <li> C++ </li>
            <li> Java </li>
            <li> python </li>
        </ul>
    </body>
</html>
'''

selector = Selector(text = text)
# print selector.extract() # 整个html元素

sl = selector.xpath(".//li/text()")
print sl.extract_first()


text = '''
<ul> 
<li> 学习手册 <b>价格：89.90</b></li>
<li> 核心编程 <b>价格：100.90</b> </li>
<li> 基础教程 <b>价格：79.90</b> </li>
</ul>

'''

sl = Selector(text=text).xpath(".//li/b/text()").re('\d+\.\d+')

print sl



