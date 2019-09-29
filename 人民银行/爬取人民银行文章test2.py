#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-24 下午9:23 
# @Author : Lattesea 
# @File : 爬取人民银行文章test2.py 
"""
    使用selenium爬取人民银行文章
"""
from selenium import webdriver
import time
from lxml import etree
import csv


class RenminyinhangSpider(object):
    def __init__(self):
        self.url='http://www.pbc.gov.cn'
        self.url1 = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index1.html'
        self.browser = webdriver.Chrome()  # 生成浏览器对象

    def parse_index_page(self):
        self.browser.get(self.url1)
        text = self.browser.page_source
        html = etree.HTML(text)
        link = html.xpath("//div[@id='11040']/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/font["
                          "@class='newslist_style']/a/@href")
        print(link)

    def run(self):
        self.parse_index_page()


if __name__ == '__main__':
    spider = RenminyinhangSpider()
    spider.run()
