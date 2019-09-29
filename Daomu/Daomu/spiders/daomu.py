# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem
import os


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']
    # basedir = '/home/tarena/novel/'

    def parse(self, response):
        """
            提取一级页面,获得每一部链接+每一部的名字
        :param response:
        :return:
        """
        # 匹配所有的a节点,因为a节点里面包含名字还有链接
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        # 循环访问a节点取出里面的名字还有链接
        for a in a_list:
            item = DaomuItem()
            # 每一部的标题,例如'盗墓笔记1:七星鲁王宫'
            item['title'] = a.xpath("./text()").get()
            # 每一部的链接
            link = a.xpath("./@href").get()

            # 交给调度器入队列
            yield scrapy.Request(
                url=link,
                meta={'item': item},
                callback=self.parse_two_page
            )

    def parse_two_page(self, response):
        item = response.meta['item']
        article_list = response.xpath("//article")
        for article in article_list:
            name= article.xpath("./a/text()").get()
            two_link = article.xpath("./a/@href").get()
            yield scrapy.Request(
                url=two_link,
                meta={'item': item, 'name': name},
                callback=self.parse_three_page
            )

    def parse_three_page(self, response):
        item = response.meta['item']
        item['name'] = response.meta['name']
        p_list = response.xpath("").extract()
        content = '\n'.join(p_list)
        item['content'] = content
        yield item

