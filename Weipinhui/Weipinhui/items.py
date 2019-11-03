# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeipinhuiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    original_price = scrapy.Field()
    discount = scrapy.Field()
    describe = scrapy.Field()
