# coding:utf8
import urllib.request
import http.cookiejar
import bs4
import ssl


url = "https://baike.baidu.com/item/vlog/7548732"
# urllib 下载网页的三种方法
#1
# response =  urllib.request.urlopen(url)
# responsestr = response.read()
# print(response.getcode())
# print(len(responsestr))

#2 
# request = urllib.request.Request(url)
# request.add_header('user-agent','Mozilla/5.0')
# response2 = urllib.request.urlopen(request)
# print(response2.getcode())
# print(len(response2.read()))

#3
# cj = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# urllib.request.install_opener(opener)
# response3= urllib.request.urlopen(url)
# print(response3.getcode())
# print(cj)
# print(response3.read())

#4 https 
ssl._create_default_https_context = ssl._create_unverified_context
opener = urllib.request.build_opener(urllib.request.HTTPSHandler())
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(response3.read())

