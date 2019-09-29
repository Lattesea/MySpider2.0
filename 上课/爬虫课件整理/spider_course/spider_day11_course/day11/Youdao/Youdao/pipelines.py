# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YoudaoPipeline(object):
    def process_item(self, item, spider):
        print('翻译结果:',item['result'])
        return item
