#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-10 下午3:32 
# @Author : Lattesea 
# @File : yongrong.py 
import requests
from fake_useragent import UserAgent
import random
import os
from lxml import etree
from requests.exceptions import RequestException
import time


class MeiziSpider(object):
    def __init__(self):
        self.url = ''
        self.headers = self.get_headers()

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

    def parse_link(self, text):
        html = etree.HTML(text)
        link = html.xpath("//ul[@class='list']/li[@class='loading-block']/a/img/@src")
        return link

    def save_image(self, filename, img_link):
        html = requests.get(url=img_link, headers=self.headers).content
        with open('%s.jpg' % filename, 'wb') as f:
            f.write(html)
        print(filename, '下载成功')

    def run(self):
        n = 1
        url = 'http://www.oneniceapp.com/user/Hw4HJQ'
        text = self.get_page(url)
        link = self.parse_link(text)
        for i in link:
            filename = 'yongrong%d' % n
            self.save_image(filename, i)
            n += 1


if __name__ == '__main__':
    spider = MeiziSpider()
    # url = 'http://www.oneniceapp.com/user/Hw4HJQ'
    # text = spider.get_page(url)
    # link = spider.parse_link(text)
    # print(link)
    spider.run()
