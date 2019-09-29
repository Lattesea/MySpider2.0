# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 名称+类别+职责+要求+地址+时间
    job_name = scrapy.Field()
    job_type = scrapy.Field()
    job_duty = scrapy.Field()
    job_require = scrapy.Field()
    job_address = scrapy.Field()
    job_time = scrapy.Field()
