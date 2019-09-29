#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-21 下午1:04 
# @Author : Lattesea 
# @File : 爬取eia网站数据.py 
"""
    爬取eia所有chart data
"""
import requests
from fake_useragent import UserAgent
import csv
from lxml import etree
import time
import random
import os


class EiaSpider(object):
    def __init__(self):
        self.url = 'https://www.eia.gov/opendata/qb.php?category=3390101'
        self.url1 = 'https://www.eia.gov/opendata/qb.php{}'

    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        return headers

    def get_one_link(self):
        text = requests.get(url=self.url, headers=self.get_headers()).text
        # print(text)
        html = etree.HTML(text)
        link = html.xpath("//*[@id='innerX']/div[3]/div[1]/ul/li[3]/ul/li/a/@href")
        filename = html.xpath("//*[@id='innerX']/div[3]/div[1]/ul/li[3]/ul/li/a/text()")
        list_result = []
        for i in zip(link, filename):
            list_result.append(i)
        return list_result

    def get_two_link(self, two_url):
        text = requests.get(two_url, headers=self.get_headers()).text
        # print(text)
        html = etree.HTML(text)
        link_two = html.xpath("//*[@id='innerX']/div[3]/div[1]/ul/li/a/@href")
        filename = html.xpath("//*[@id='innerX']/div[3]/div[1]/ul/li/a/text()")
        list_result = []
        for i in zip(link_two, filename):
            list_result.append(i)
        return list_result

    def parse_three_page(self, three_url):
        text = requests.get(three_url, headers=self.get_headers()).text
        html = etree.HTML(text)
        name = html.xpath("//*[@id='innerX']/div[3]/div[1]/table/tbody/tr/td[1]/text()")
        period = html.xpath("//*[@id='innerX']/div[3]/div[1]/table/tbody/tr/td[2]/text()")
        frequency = html.xpath("//*[@id='innerX']/div[3]/div[1]/table/tbody/tr/td[3]/text()")
        value = html.xpath("//*[@id='innerX']/div[3]/div[1]/table/tbody/tr/td[4]/text()")
        units = html.xpath("//*[@id='innerX']/div[3]/div[1]/table/tbody/tr/td[5]/text()")
        list_result = []
        for i in zip(name, period, frequency, value, units):
            list_result.append(i)
        print(list_result)
        return list_result

    def save_csv(self, result, filename):
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

    def run(self):
        link_list = self.get_one_link()
        try:
            for link in link_list:
                print(link)

                url = self.url1.format(link[0])
                link2 = self.get_two_link(url)
                print(link2)
                for j in link2:
                    url1 = self.url1.format(j[0])
                    print(url1)
                    result = self.parse_three_page(url1)

                    directory = '/home/tarena/爬虫项目/eia/%s/' % link[1]
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    filename = directory+j[1] + '.csv'
                    print(filename)
                    self.save_csv(result, filename)
                    print("%s保存成功" % filename)
                    # time.sleep(random.randint(1, 3))
        except Exception as err:
            print(err)

        # url = 'https://www.eia.gov/opendata/qb.php?category=3390119&sdid=EBA.YAD-ALL.NG.WAT.H'
        # self.parse_three_page(url)


if __name__ == '__main__':
    spider = EiaSpider()
    spider.run()
