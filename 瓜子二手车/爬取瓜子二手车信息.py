#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-06 21:40
# @Author: Lattesea
# @File: 爬取瓜子二手车信息.py
import requests
from fake_useragent import UserAgent
from lxml import etree


class GuaziSpider(object):
    def __init__(self):
        self.url = 'https://www.guazi.com/gz/buy/'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "uuid=1990576c-6fec-47bb-cf1d-104413625461; cityDomain=gz; user_city_id=16; ganji_uuid=7179843687447180470720; lg=1; GZ_TOKEN=e68a8kOl%2BLuipgyyObkZLXJXuEX0VhFUEX2xRdSY4ybBVzkkz1EU9dQhd3Hfs%2Bzp%2BymDY6MId9QRuD985d3vcOAypTNDcLbLRm3a00PtuqYLw%2Bw%2Fzbq9zF4z9Gn2VZD0%2FtAi8%2BvX21Rh6%2FpD7w; guaZiUserInfo=bMSSSmF06GUUjBgIe8iIY8; userid=717077384; CHDSSO=e68a8kOl%2BLuipgyyObkZLXJXuEX0VhFUEX2xRdSY4ybBVzkkz1EU9dQhd3Hfs%2Bzp%2BymDY6MId9QRuD985d3vcOAypTNDcLbLRm3a00PtuqYLw%2Bw%2Fzbq9zF4z9Gn2VZD0%2FtAi8%2BvX21Rh6%2FpD7w; antipas=90081d767V993w9E098880p97; clueSourceCode=%2A%2300; sessionid=9c3bc78a-4b40-4ed8-9553-1b67ad38f640; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1573046540,1573104609; close_finance_popup=2019-11-07; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%221990576c-6fec-47bb-cf1d-104413625461%22%2C%22ca_city%22%3A%22gz%22%2C%22sessionid%22%3A%229c3bc78a-4b40-4ed8-9553-1b67ad38f640%22%7D; preTime=%7B%22last%22%3A1573104636%2C%22this%22%3A1573046540%2C%22pre%22%3A1573046540%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1573104635",
            "Host": "www.guazi.com",
            "Referer": "https://www.guazi.com/gz/?ca_kw&ca_n=default&ca_s=seo_baidu",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        }
        return headers

    def parse(self):
        response = requests.get(url=self.url, headers=self.get_headers(), verify=False).text

        print(response)
        html = etree.HTML(response)
        name = html.xpath(
            "//div[@class='list-wrap js-post']/ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/h2[@class='t']/text()")
        message = html.xpath(
            "//div[@class='list-wrap js-post']/ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/div[@class='t-i']/text()")
        time = []
        for i in message[::2]:
            time.append(i)
        far = []
        for i in message[1::2]:
            far.append(i)
        price = html.xpath(
            "//div[@class='list-wrap js-post']/ul[@class='carlist clearfix js-top']/li/a[@class='car-a']/div[@class='t-price']/p/text()")
        print(name)
        # print(message)
        print(time)
        print(far)
        print(price)

    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = GuaziSpider()
    spider.run()
