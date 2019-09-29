#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-10 上午11:11 
# @Author : Lattesea 
# @File : 爬取妹纸图.py 
import requests
import time
import random
from fake_useragent import UserAgent
import re
from requests.exceptions import RequestException
from lxml import etree
import csv
from pyquery import PyQuery as pq


class MeiziSpider(object):
    def __init__(self):
        self.url = 'https://gz.lianjia.com/ershoufang/'

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

    def parse_index_link(self, text):
        html = etree.HTML(text)
        link = html.xpath("//div[@class='postlist']/ul[@id='pins']/li/span/a/@href")
        return link

    def parse_someone_link(self, text):
        html = etree.HTML(text)
        link = html.xpath("//div[@class='main-image']/p/a/img/@src")
        return link

    def parse_max_page(self, text):
        html = etree.HTML(text)
        number = html.xpath("//div[@class='pagenavi']/a[last()-1]/span/text()")
        return number

    def save_image(self, number, image_link):
        for i in range(1, number)


if __name__ == '__main__':
    spider = MeiziSpider()
    url = 'https://www.mzitu.com/'
    text = spider.get_page(url)
    link = spider.parse_link(text)
    print(link)
