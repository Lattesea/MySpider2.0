#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-11 下午6:32 
# @Author : Lattesea 
# @File : 爬取西刺代理.py
import requests
import time
import random
from fake_useragent import UserAgent
import re
from requests.exceptions import RequestException
from lxml import etree
import csv
from pyquery import PyQuery as pq


class IPSpider(object):
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/'
        self.url_test = 'http://httpbin.org/get'

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
        while True:
            try:
                headers = self.get_headers()
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response.text
                return None
            except RequestException as err:
                print(err)

    def parse_ip(self, text):
        html = etree.HTML(text)
        ip = html.xpath("//tr/td[2]/text()")
        port = html.xpath("//tr/td[3]/text()")
        return zip(ip, port)

    def test_ip(self, ip, port):

        while True:
            try:
                url_ip = 'http://' + ip + ':' + port
                proxies = {
                    'http': url_ip,
                    'https': url_ip
                }
                headers = self.get_headers()
                response = requests.get(url, headers=headers, proxies=proxies)
                if response.status_code == 200:
                    return ip, port
                return None
            except RequestException:
                print('%s失效' % ip)

    def run(self):
        for i in range(1,100):
            pass


if __name__ == '__main__':
    spider = IPSpider()
    url = spider.url
    text = spider.get_page(url)
    result = spider.parse_ip(text)
    for i in result:
        print(i)
