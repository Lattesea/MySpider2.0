# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem
import os


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']
    basedir = '/home/tarena/novel/'

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
            # 创建一级文件夹
            onedir = self.basedir + item['title'] + '/'
            print(onedir)
            # 判断是否存在文件夹,不存在则创建
            if not os.path.exists(onedir):
                os.makedirs(onedir)

            # 交给调度器入队列
            yield scrapy.Request(
                url=link,
                meta={'item': item, 'onedir': onedir},
                callback=self.parse_two_page
            )

    def parse_two_page(self, response):
        """
            解析二级页面小说,获得每一节标题和每一节的连接
        :param response:
        :return:
        """
        item = response.meta['item']
        onedir = response.meta['onedir']
        article_list = response.xpath("//article")
        for article in article_list:
            item['name'] = article.xpath("./a/text()").get().replace('', '-')
            # 处理特殊符号
            all_chars = '*<>|?\/:"'
            for char in all_chars:
                if char in all_chars:
                    item['name'] = item['name'].replace(char, '-')
            two_link = article.xpath("./a/@href").get()
            # 创建二级文件夹
            twodir = onedir + item['name'] + '/'
            if not os.path.exists(twodir):
                os.makedirs(twodir)
            # 交给调度器
            yield scrapy.Request(
                url=two_link,
                meta={'item': item, 'twodir': twodir},
                callback=self.parse_three_page
            )

    def parse_three_page(self, response):
        item = response.meta['item']
        twodir = response.meta['twodir']
        # p_list=['段落1','段落2','段落3']
        p_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['content'] = '\n'.join(p_list)
        # 拼接绝对路径文件名xxx.txt
        item['filename'] = twodir + item['name'] + '.txt'
        yield item
