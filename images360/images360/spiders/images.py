# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import Images360Item


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    # start_urls = ['http://images.so.com/']
    url = 'https://image.so.com/zj?ch=beauty&sn={}&listtype=new&temp=1'

    def parse(self, response):
        html = json.loads(response.text)
        item = Images360Item()
        for img in html['list']:
            item['img_url'] = img['qhimg_url']
            item['img_title'] = img['group_title']
            yield item

    def start_requests(self):
        for sn in range(0, 1000, 30):
            url = self.url.format(sn)
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                dont_filter=False
            )
