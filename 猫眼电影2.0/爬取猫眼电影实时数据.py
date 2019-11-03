#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-21 上午8:40 
# @Author : Lattesea 
# @File : 爬取猫眼电影实时数据.py 
import requests
from fake_useragent import UserAgent
from lxml import etree


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'http://piaofang.maoyan.com/?ver=normal&isid_key=1A5BCB853F44B09D6DC5DC4D74A89B17C7434B37F87C5DB9F89B3FB776FCC134'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def parse(self):
        text = requests.get(url=self.url, headers=self.get_headers()).text
        html = etree.HTML(text)
        name = html.xpath("//div[@id='ticket_tbody']/ul[@class='canTouch']/li[@class='c1']/b/text()")
        count_day = html.xpath("//div[@id='ticket_tbody']/ul[@class='canTouch']/li[@class='c1']/em[1]/text()")
        total_money = html.xpath(
            "//div[@id='ticket_tbody']/ul[@class='canTouch']/li[@class='c1']/em[2]/i[@class='cs']/text()")
        result = zip(name, count_day, total_money)
        for i in result:
            print(i)
        return result

    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
