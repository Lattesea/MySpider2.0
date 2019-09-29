# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):

        print(item['name'],item['time'])

        return item

import pymysql
from .settings import *

class MaoyanMysqlPipeline(object):
    # 爬虫程序开始时只执行1次
    def open_spider(self,spider):
        print('我是open_spider,哈哈')
        # 一般用于创建数据库连接
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=CHARSET
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into filmtab values(%s,%s,%s)'
        L = [
            item['name'],
            item['star'],
            item['time']
        ]
        self.cursor.execute(ins,L)
        self.db.commit()
        ## create database if not exists maoyandb charset utf8;
        ## create table if note exists filmtab(xx xx);

        return item

    # 爬虫程序结束时只执行1次
    def close_spider(self,spider):
        # 收尾工作: 一般用于断开数据库
        self.cursor.close()
        self.db.close()
        print('我是close_spider,哈哈')


class MaoyanMongoPipeline(object):
    def process_item(self,item,spider):
        return item





















