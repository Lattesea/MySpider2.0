# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()  # 岗位名称
    company_name = scrapy.Field()  # 公司名称
    company_type = scrapy.Field()  # 公司类型
    company_size = scrapy.Field()  # 公司大小
    city = scrapy.Field()  # 城市
    updateDate = scrapy.Field()  # 更新日期
    salary = scrapy.Field()  # 薪资
    eduLevel = scrapy.Field()  # 学历
    workingExp = scrapy.Field()  # 工作经验
    welfare = scrapy.Field()  # 福利
    url = scrapy.Field()  # 链接
    people = scrapy.Field()  # 人数
    dult = scrapy.Field()  # 责则
