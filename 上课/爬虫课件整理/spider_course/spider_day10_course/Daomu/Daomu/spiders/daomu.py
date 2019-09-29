# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    # 解析一级页面 - 链接+title
    def parse(self, response):
        # 基准xpath
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')
        for a in a_list:
            item = DaomuItem()
            item['title'] = a.xpath('./text()').get()
            link = a.xpath('./@href').get()
            # 扔给调度器入队列
            yield scrapy.Request(
                url=link,
                # 不同解析函数之间传递数据
                meta={'item':item},
                callback=self.parse_two_page
            )

    # 解析二级页面函数 : 名称(七星鲁王 第一章 血尸)+链接
    def parse_two_page(self,response):
        # 获取item
        item = response.meta['item']
        article_list = response.xpath('//article')
        for article in article_list:
            name = article.xpath('./a/text()').get()
            two_link = article.xpath('./a/@href').get()
            # 继续交给调度器入队列
            yield scrapy.Request(
                url=two_link,
                meta={'item':item,'name':name},
                callback=self.parse_three_page
            )

    # 解析三级页面: 小说内容
    def parse_three_page(self,response):
        item = response.meta['item']
        item['name'] = response.meta['name']
        # p_list: ['段落1','段落2','段落3']
        p_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        content = '\n'.join(p_list)
        item['content'] = content

        yield item













