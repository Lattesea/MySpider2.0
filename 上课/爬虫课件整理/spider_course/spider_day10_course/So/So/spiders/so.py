# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem
import os

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'http://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
    directory = '/home/tarena/images/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 重写start_requests()方法
    def start_requests(self):
        for pn in range(0,100,30):
            url = self.url.format(pn)
            yield scrapy.Request(
                url=url,
                callback=self.parse_image
            )

    def parse_image(self,response):
        html = json.loads(response.text)
        item = SoItem()
        for img in html['list']:
            item['img_link'] = img['qhimg_url']
            item['img_title'] = img['title']

            yield item
















