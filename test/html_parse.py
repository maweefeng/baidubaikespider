
from bs4 import BeautifulSoup
import re


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf8')

# 查找所有标签为a的节点
links = soup.find_all('a')

for  link in links:
    print(link.name,link['href'],link.get_text())


# 查找所有标签为a 链接符合http://example.com/lacie形式的节点
link_node = soup.find('a',href='http://example.com/lacie')
print(link_node.name,link_node['href'],link_node.get_text())


# 正则表达式匹配
link_nodes = soup.find_all('a',href=re.compile(r'ill'))
for  link in link_nodes:
    print(link.name,link['href'],link.get_text())


#查找所有标签为div class 为abc 文字为python的节点
link_classnodes = soup.find_all('p',class_='story',text='...')

for  link in link_classnodes:
    print(link.name,link.get_text())


