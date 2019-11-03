# -*- coding: utf-8 -*-
import scrapy


class DazhongdianpingSpider(scrapy.Spider):
    name = 'dazhongdianping'
    allowed_domains = ['www.dianping.com']
    start_urls = ['http://www.dianping.com/']

    def parse(self, response):
        pass
