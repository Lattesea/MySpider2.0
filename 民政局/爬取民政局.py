#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午3:03 
# @Author : Lattesea 
# @File : 爬取民政局.py 
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


class MinzhengSpider(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.url1 = 'http://www.mca.gov.cn'

    def get_headers(self):
        """
            随机产生请求头
        :return:
        """
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        return headers

    def get_page(self, url):
        """
            获取网页源代码
        :param url:
        :return:
        """
        # while True:
        try:
            headers = self.get_headers()
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            return None
        except RequestException as err:
            print(err)

    def parse_message(self, text):
        """
            获取信息页代号
        :param text:
        :return:
        """
        html = etree.HTML(text)
        number = html.xpath("//tr/td[@class='xl7110750'][1]/text()")
        address = html.xpath("//tr/td[@class='xl7110750'][2]/text()")
        return zip(address, number)

    def parse_index(self, text):
        """
            获取假链接
        :param text:
        :return:
        """
        html = etree.HTML(text)
        link = html.xpath('//tr[2]/td[@class="arlisttd"]/a/@href')
        false_url = self.url1 + link[0]
        return false_url

    def run(self):
        index_url = self.url
        text_index = self.get_page(index_url)
        false_url = self.parse_index(text_index)
        print(false_url)
        text_false = self.get_page(false_url)
        print(text_false)


if __name__ == '__main__':
    spider = MinzhengSpider()
    spider.run()
