# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 一级页面标题
    title = scrapy.Field()
    # 二级页面标题
    name = scrapy.Field()
    # 小说内容
    content = scrapy.Field()
    # 文件名
    filename=scrapy.Field()
