#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-21 下午8:53 
# @Author : Lattesea 
# @File : 计算总和翻页篇.py 
import requests
from fake_useragent import UserAgent
from lxml import etree
import re


class SumSpider(object):
    def __init__(self):
        self.url = 'http://glidedsky.com/level/web/crawler-basic-2?page={}'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1571661021; _ga=GA1.2.711956546.1571661022; _gid=GA1.2.1734584790.1571661022; footprints=eyJpdiI6IklRQ2xXcHBKM2p3RFcxN2R0TWhuQkE9PSIsInZhbHVlIjoiRFQrTlRDQ3ZrQ2xvMkU4bW1UVG8xQVYyTzNcL1RzY0psYTRFMjhva1U0THJwZ01aR3d3aHRiRG1WVnhncUdCOVgiLCJtYWMiOiI2ZTRmZDkzNzRlZjllMjMxZDY4MTkzOTAzM2RhYmRmMWFmOGQwZGYyY2VlMTUzMTA5MmJhMDQwNTUwOGNjY2IyIn0%3D; _gat_gtag_UA_75859356_3=1; XSRF-TOKEN=eyJpdiI6InhTNFRkXC91WFB3RW1hRk9INGhXZHdRPT0iLCJ2YWx1ZSI6ImUxQ0RqWmhIK2dwWGlObmFRTFNMSEoxa0l0RmRTMHYzV1ZTajg5VzhVbWVZMm82bFwvT0ZwWWtPZVNDTGJcL3FZRiIsIm1hYyI6ImU4YjM3YzhlNjBlMmYwZmMzNGJjZDMwZGVlY2U4YzgxYzUzOTljMGFkYWViN2YwNmRjMzQ0MmM3NDBhYjBmNjMifQ%3D%3D; glidedsky_session=eyJpdiI6Indma1VrT25kVGJvaVQyWEsra3pCakE9PSIsInZhbHVlIjoiQVwvVGxreTd3VGtIN1RVVjNrczZzcUNNQ1FWRTViNFFZK1FobDN0YmpJU3Fra1dOaGNySStyVzFvSlc1T0hLSTQiLCJtYWMiOiIwNThiYzNlNTk2YjIyZWIyZjFmY2E0YWMzNWU0NTcyNjkzOTk5MjgxMjExMmFhY2Q4N2VmMjhjYTlkYTlkZjZkIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1571661376",
            "Host": "glidedsky.com",
            "Referer": "http://glidedsky.com/level/crawler-basic-1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        }
        return headers

    def parse(self, number):
        url = 'http://glidedsky.com/level/web/crawler-basic-2?page={}'.format(number)
        text = requests.get(url=url, headers=self.get_headers()).text
        # print(text)
        html = etree.HTML(text)
        number = html.xpath(
            "//div[@class='card']/div[@class='card-body']/div[@class='row']/div[@class='col-md-1']/text()")
        number = list(map(lambda item: re.sub('\s+', '', item), number))
        number = list(filter(None, number))
        result = 0
        for i in number:
            result += int(i)
        print(result)
        return result

    def run(self):
        result = 0
        for i in range(1, 1001):
            result += self.parse(i)
        print(result)


if __name__ == '__main__':
    spider = SumSpider()
    spider.run()
