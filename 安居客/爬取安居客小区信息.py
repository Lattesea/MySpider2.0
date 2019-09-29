#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-21 下午4:15 
# @Author : Lattesea 
# @File : 爬取安居客小区信息.py 
import requests
from fake_useragent import UserAgent
import csv
from lxml import etree


class AnjukeSpider(object):
    def __init__(self):
        # self.url = 'https://qd.anjuke.com/community/?from=esf_list_navigation'
        self.url = 'https://qd.anjuke.com/community/p{}/'

    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random,
                   'referer': 'https://qd.anjuke.com/community/?from=esf_list_navigation'
                   }
        return headers

    def get_link(self):
        text = requests.get(url=self.url, headers=self.get_headers()).text
        html = etree.HTML(text)
        link = html.xpath("//h3/a/@href")
        print(link)

    def parse_message_page(self, url):
        text = requests.get(url=url, headers=self.get_headers()).text
        # print(text)
        html = etree.HTML(text)
        name = html.xpath("//div[@class='comm-title']/a/@title")
        address = html.xpath("/html/body/div[2]/div[3]/div[1]/h1/span/text()")
        property_type = html.xpath("//*[@id='basic-infos-box']/dl/dd[1]/text()")
        property_money = html.xpath("//*[@id='basic-infos-box']/dl/dd[2]/text()")
        total_area = html.xpath("//*[@id='basic-infos-box']/dl/dd[3]/text()")
        total_family = html.xpath('//*[@id="basic-infos-box"]/dl/dd[4]/text()')
        year = html.xpath('//*[@id="basic-infos-box"]/dl/dd[5]/text()')
        parking_count = html.xpath('//*[@id="basic-infos-box"]/dl/dd[6]/text()')
        plot_ratio = html.xpath('//*[@id="basic-infos-box"]/dl/dd[7]/text()')
        green_rate = html.xpath('//*[@id="basic-infos-box"]/dl/dd[8]/text()')
        developers = html.xpath('//*[@id="basic-infos-box"]/dl/dd[9]/text()')
        property_company = html.xpath('//*[@id="basic-infos-box"]/dl/dd[10]/text()')
        business_circle = html.xpath('//*[@id="basic-infos-box"]/dl/dd[11]/text()')

        print(name, address)

    def run(self):
        # self.get_link()
        url = 'https://qd.anjuke.com/community/view/792706?from=Filter_1&hfilter=filterlist'
        self.parse_message_page(url)


if __name__ == '__main__':
    spider = AnjukeSpider()
    spider.run()
