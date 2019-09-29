#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-11 下午7:34 
# @Author : Lattesea 
# @File : 爬取快代理.py 
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
        self.url = 'https://www.kuaidaili.com/free/inha/'
        self.url_test = 'http://httpbin.org/get'

    def get_headers(self):
        """
            随机产生请求头
        :return:
        """
        ua = UserAgent()
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': ua.random,
            'Host': 'www.kuaidaili.com',
            # 'Cookie': 'channelid=0;sid=1568201343183464;ga=GA1.2.173662909.1568201344;_gid=GA1.2.207571687.1568201344;Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1568201344;Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1568203503'
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
                print(response.status_code)
                raise ValueError("打开网页错误")
            except RequestException as err:
                print(err)

    def parse_ip(self, text):
        html = etree.HTML(text)
        ip = html.xpath("//tr/td[1]/text()")
        print(ip)
        port = html.xpath("//tr/td[2]/text()")
        print(port)
        return zip(ip, port)

    def test_ip(self, ip, port):
            try:
                url_ip = 'http://' + ip + ':' + port
                proxies = {
                    'http': url_ip,
                    'https': url_ip
                }
                headers = self.get_headers()
                response = requests.get(url_ip, headers=headers, proxies=proxies, timeout=3)
                if response.status_code == 200:
                    return ip, port
                return None
            except RequestException:
                print('%s失效' % ip)

    def save_ip(self, result):
        with open("kuaidailiip.csv", "a")as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerows(result)

    def run(self):
        for i in range(1, 101):
            url = self.url + str(i) + '/'
            text = self.get_page(url)
            ip = self.parse_ip(text)
            result = []
            for j in ip:
                ok_ip = self.test_ip(j[0], j[1])
                result.append(ok_ip)
            self.save_ip(result)
            time.sleep(5)


if __name__ == '__main__':
    spider = IPSpider()
    spider.run()
