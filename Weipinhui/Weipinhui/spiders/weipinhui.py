# -*- coding: utf-8 -*-
import scrapy


class WeipinhuiSpider(scrapy.Spider):
    name = 'weipinhui'
    allowed_domains = ['www.vip.com']
    start_urls = ['http://www.vip.com/']

    def parse(self, response):
        result=response.xpath("")
