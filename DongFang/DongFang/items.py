# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DongfangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sname = scrapy.Field()
    scode = scrapy.Field()
    basiceps = scrapy.Field()
    totaloperatereve = scrapy.Field()
    ystz = scrapy.Field()
    yshz = scrapy.Field()
    parentnetprofit = scrapy.Field()
    sjltz = scrapy.Field()
    sjlhz = scrapy.Field()
    roeweighted = scrapy.Field()
    bps = scrapy.Field()
    mgjyxjje = scrapy.Field()
    xsmll = scrapy.Field()
    publishname = scrapy.Field()
    reportdate = scrapy.Field()
