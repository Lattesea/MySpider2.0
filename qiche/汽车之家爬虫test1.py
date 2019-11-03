#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-8 上午9:53 
# @Author : Lattesea 
# @File : 汽车之家爬虫test1.py 
import requests
from fake_useragent import UserAgent
from lxml import etree


class QichezhijiaSpider(object):
    def __init__(self):
        self.url = 'https://car.autohome.com.cn/config/series/59.html#pvareaid=3454437'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def parse(self):
        text = requests.get(url=self.url, headers=self.get_headers()).text
        print(text)
        html = etree.HTML(text)

    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = QichezhijiaSpider()
    spider.run()
