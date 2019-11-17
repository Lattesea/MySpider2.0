# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SgcnspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _time = scrapy.Field()
    _phone = scrapy.Field()
    _email = scrapy.Field()
    _wechat = scrapy.Field()
