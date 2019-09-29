# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    # 起始url地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        result = response.xpath('/html/head/title/text()')
        print('*'*50)
        print(result)
        print('*'*50)






