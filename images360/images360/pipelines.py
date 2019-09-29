# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import pymysql


class Images360Pipeline(ImagesPipeline):
    # 重写get_media_requests()方法
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['img_url'],
            meta={'item': item['img_title']}
        )

    def file_path(self, request, response=None, info=None):
        title = request.meta['item']
        filename = title + '.' + request.url.split('.')[-1]
        return filename


class MysqlPipeline():

    def open_spider(self, spider):
        self.db = pymysql.connect('localhost', 'root', '123456', 'images360', charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into images values (%s,%s)'
        L = [item['img_title'], item['img_url']]
        self.cursor.execute(sql, L)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()
