from baidu_spider import spider_main
rooturl = 'https://baike.baidu.com/item/Python/407313'
obj_spider = spider_main.SpiderMain()
obj_spider.craw(rooturl)
