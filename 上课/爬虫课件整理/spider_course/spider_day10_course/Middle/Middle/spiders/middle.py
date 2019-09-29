# -*- coding: utf-8 -*-
import scrapy

class MiddleSpider(scrapy.Spider):
    name = 'middle'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print('我是parse函数输出')






