# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'], item['time'], item['star'])
        return item


import pymysql
from .settings import *


class MaoyanMysqlPipeline(object):
    def open_spider(self, spider):
        # 创建数据库连接
        print("我是open_spider函数输出")
        self.db = pymysql.connect(host=MYSQL_HOST,
                                  user=MYSQL_USER,
                                  password=MYSQL_PWD,
                                  database=MYSQL_DB,
                                  charset=MYSQL_CHAR
                                  )
        self.cursor = self.db.cursor()  #创建游标

    def process_item(self, item, spider):
        ins = 'insert into filmtab values(%s,%s,%s)'
        L = [
            item['name'], item['star'], item['time']
        ]
        self.cursor.execute(ins, L)
        self.db.commit()
        # 如果没有数据表就创建
        # create table if not exists filmtab(XX XX)
        return item

    def close_spider(self, spider):
        print("我是close_spider函数输出")
        self.cursor.close()
        self.db.close()
