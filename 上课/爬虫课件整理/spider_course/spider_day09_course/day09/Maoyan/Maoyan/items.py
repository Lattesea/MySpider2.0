
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MaoyanItem(scrapy.Item):
    '''定义要抓取的数据结构'''
    # define the fields for your item here like:
    name = scrapy.Field()
    star = scrapy.Field()
    time = scrapy.Field()








