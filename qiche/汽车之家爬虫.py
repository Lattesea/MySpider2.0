#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-23 下午4:35 
# @Author : Lattesea 
# @File : 汽车之家爬虫.py 
"""
    爬取汽车之家所有车的型信息
"""
import requests
from fake_useragent import UserAgent
import re
import csv
import time
import random
from lxml import etree


class QichezhijiaSpider(object):
    def __init__(self):
        self.url = 'https://www.autohome.com.cn/car/'
        self.url2 = 'https://www.autohome.com.cn/3170/#levelsource=000000000_0&pvareaid=101594'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def parse_index_page(self):
        text = requests.get(url=self.url, headers=self.get_headers()).text
        html = etree.HTML(text)
        car_name = html.xpath('//*[@id="s3170"]/h4/a/@href')
        print(car_name)

    def parse_two_page(self):
        text = requests.get(url=self.url2, headers=self.get_headers()).text
        html = etree.HTML(text)
        car_name = html.xpath('//*[@id="spec_36622"]/a/text()')
        guide_price = html.xpath('//*[@id="specWrap-2"]/dl[1]/dd[1]/div[3]/p/span/text()')
        reference_price = html.xpath('//*[@id="specWrap-2"]/dl[1]/dd[1]/div[4]/p/a/text()')
        print(car_name)
        print(guide_price)
        print(reference_price)

    def run(self):
        # self.parse_index_page()
        self.parse_two_page()


if __name__ == '__main__':
    spider = QichezhijiaSpider()
    spider.run()
