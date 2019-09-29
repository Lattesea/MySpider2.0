# -*- coding: utf-8 -*-
import scrapy
# 导入items.py中的类: MaoyanItem
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']
    offset = 0

    def parse(self, response):
        # 创建item对象
        item = MaoyanItem()
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            # item['name']: [<Selector xpath='./a/@title' data='乱世佳人'>]
            # extract()之后: ['乱世佳人']
            # extract_first(): 序列化第一个选择器,结果为 '乱世佳人'
            # get(): 等同于extract_first()
            item["name"] = dd.xpath('./a/@title').extract()[0]
            item["star"] = dd.xpath('.//p[@class="star"]/text()').extract_first()
            item["time"] = dd.xpath('.//p[@class="releasetime"]/text()').get()

            # 把数据交给管道文件 - pipelines.py
            yield item

        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            # 把url交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )






# https://maoyan.com/board/4?offset={}





