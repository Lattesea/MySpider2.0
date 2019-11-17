# -*- coding: utf-8 -*-
import scrapy


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['list.jd.com']
    start_urls = ['http://list.jd.com/']

    def start_requests(self):
        url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=fd0030d27dbe4e9b9f36cda661012c74'

    def parse(self, response):
        pass
