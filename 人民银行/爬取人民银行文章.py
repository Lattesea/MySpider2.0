#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-18 下午8:37 
# @Author : Lattesea 
# @File : 爬取人民银行文章.py 
import requests
from fake_useragent import UserAgent
import time
import random
from lxml import etree


class RenminyinhangSpider(object):
    def __init__(self):
        self.url = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index1.html'
        self.url2='http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/3895219/index.html'
    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random,
                   "Accept-Encoding": "gzip, deflate",
                   "Referer": "http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index1.html",
                   "Accept-Language": "zh-CN,zh;q=0.9"
                   }
        return headers

    def get_one_page(self, url):
        text = requests.get(url=url, headers=self.get_headers()).text
        print(text)
        html = etree.HTML(text)
        print(html)
        # link = html.xpath("//tr[2]/td/table[1]/tbody/tr/td/font[@class='newslist_style']/a/@href")
        # print(link)

    def get_two_page(self, url):
        text = requests.get(url=url, headers=self.get_headers()).text
        print(text)
        html = etree.HTML(text)
        title = html.xpath("//table[2]/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td/h2/text()")
        print(title)

    def run(self):
        # self.get_one_page(self.url)
        self.get_two_page(self.url2)

if __name__ == '__main__':
    spider = RenminyinhangSpider()
    spider.run()
