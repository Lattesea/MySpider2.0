# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class DaomuPipeline(object):
    def process_item(self, item, spider):
        # item['title']:  盗墓笔记1:七星鲁王宫
        # item['name']:   七星鲁王 第一章 血尸
        # item['content']: 具体小说内容
        # directory: /home/tarena/novel/盗墓笔记1：七星鲁王宫/
        directory = '/home/tarena/novel/{}/'.format(item['title'])
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = directory + item['name'] + '.txt'
        with open(filename,'w') as f:
            f.write(item['content'])

        return item











