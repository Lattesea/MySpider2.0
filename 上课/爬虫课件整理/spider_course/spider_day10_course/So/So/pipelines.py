# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入scrapy的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class SoPipeline(ImagesPipeline):
    # 重写get_media_requests()方法
    def get_media_requests(self, item, info):
        # 直接交给调度器入队列
        yield scrapy.Request(
            url=item['img_link'],
            meta={'title':item["img_title"]}
        )

    # 重写file_path()方法: 解决 路径+文件名 问题
    def file_path(self, request, response=None, info=None):
        # request.meta  获取meta属性值
        title = request.meta['title']
        filename = title + '.jpg'

        return filename









