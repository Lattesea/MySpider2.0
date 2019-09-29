#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-10 上午10:34 
# @Author : Lattesea 
# @File : 爬取红薯小说.py 
"""

"""
import requests
import time
import random
from fake_useragent import UserAgent
import re
from requests.exceptions import RequestException
from lxml import etree
import csv
from pyquery import PyQuery as pq


class HongshuSpider(object):
    def __init__(self):
        self.url = 'https://gz.lianjia.com/ershoufang/'

    def get_headers(self):
        """
            随机产生请求头
        :return:
        """
        ua = UserAgent()
        headers = {'User-Agent': ua.random
                   # ':authority': 'g.hongshu.com',
                   # ':method': 'GET',
                   # ':path': '/content/95678/14321012.html',
                   # ':scheme': 'https',
                   # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                   # 'accept-encoding': 'gzip, deflate, br',
                   # 'accept-language': 'zh-CN,zh;q=0.9',
                   # 'cookie': 'pgv_pvi=2657113088; pgv_si=s3259039744; Hm_lvt_e966b218bafd5e76f0872a21b1474006=1568079767; yqksid=ev9dstu3gnu0ag5f3h9gp58896;'
                   #           'bookfav=%7B%22b88594%22%3A0%2C%22b95678%22%3A0%7D; Hm_lpvt_e966b218bafd5e76f0872a21b1474006=1568084310',
                   # 'referer': 'https://g.hongshu.com/content/95678/14321011.html',
                   # 'sec-fetch-mode': 'navigate',
                   # 'sec-fetch-site': 'same-origin',
                   # 'sec-fetch-user': '?1',
                   # 'upgrade-insecure-requests': '1',

                   }
        return headers

    def get_page(self, url):
        """
            获取网页源代码
        :param url:
        :return:
        """
        while True:
            try:
                headers = self.get_headers()
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response.text
                return None
            except RequestException as err:
                print(err)


if __name__ == '__main__':
    spider = HongshuSpider()
    url = 'https://g.hongshu.com/content/95678/14321011.html'
    text = spider.get_page(url)
    print(text)
