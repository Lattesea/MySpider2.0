# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BitfinexItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    buy_price = scrapy.Field()
    buy_amount = scrapy.Field()
    sell_price = scrapy.Field()
    sell_amount = scrapy.Field()
    time = scrapy.Field()
