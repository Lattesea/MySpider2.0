#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-10-22 3:32
# @Author: Lattesea
# @File: 计算总和字体反爬篇.py
import base64
from fontTools.ttLib import TTFont
import requests
from lxml import etree
import re


class SkySpider(object):
    def __init__(self):
        self.url = 'http://glidedsky.com/level/web/crawler-font-puzzle-1?page={}'

    def get_headers(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1571676446; _ga=GA1.2.1001174242.1571676446; _gid=GA1.2.409896106.1571676446; footprints=eyJpdiI6IjM2aG9pWENqd0ZXK3hKemEzcWhJdFE9PSIsInZhbHVlIjoiczAxQTlTKzBcL0dhckJsUXllRWQyK240UWFuWWdMUitOciszNVpCSHMwc2J6ejJEdDdJRm1KeVJGYld6eTgxd1QiLCJtYWMiOiIwNTc3N2FiMTQyMzZkYjg5MTgyOWY0MGUwNTc5MDBkMmQ0ODQ1YmM5ODYyMmViMTMxOWQzMmVmNjlkNTYxZjU4In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlpcL0NnSTk5UVBJNXY5amdSWDdLa1d3PT0iLCJ2YWx1ZSI6InFSbGpEU0RDU3hyQzNsbFpLQU5oYkFMZGlHV1RXWVNhOTI2ZSsxQ3lqYW1ISUQ2d0VWbnZJSFpRZlwvV0JuTHpZaWdVZU5WV3hjR0ZrN1l4ZXdQQlRSSUkySFJBc3lmWGRGd25QRHQ2WGZnRmIzK3krYnlMXC9MUm1lY29Na1wvdldvU3hNQ0FNeVwvdVhFeUZGSHhKbXZHd2pINFpaMWNFU0N0ajNjSUJHMHJ3TlE9IiwibWFjIjoiMGQ0OWM2ZjdiNTNjYWM2OTg4YjYwMDY5YWFlNDEwYmYzZWE1YjM2NjQwYmUwNjY0MDViNzA5NDQ1ZmM4NDJlYyJ9; XSRF-TOKEN=eyJpdiI6IlpibEtWZWFpZmhTNjFpREp3Z2FxMHc9PSIsInZhbHVlIjoiS1lEYkZQQ1JxNlN5dlNiR1wvZUJ3eWxRMm9ncEZlVVI5aHJXWW9LM3cyWVZZMGFDYnVLaTQ3XC9VdTY0aVZQRnZwIiwibWFjIjoiZmE0ODU4YWM5Yzc2YmE4ODRmYjMxOGEyOTdiZjc3ZDA4ZDU3MzllOWExN2M0NzdlNjc5MDU4MzdmNzU4ZmRkMiJ9; glidedsky_session=eyJpdiI6InhHanl5bXhDSkZ1YnA4YVlTeFVZUlE9PSIsInZhbHVlIjoiam1tTytDTTJVOVpCcEtFaUhOQWJUYWxHWlZxRHNcL0JCQnhHRWRINHhXbDZsWmRUTVNGS3Z1QkloYnZvenNGcFIiLCJtYWMiOiIzNmIyMDFjZmViNDU2NTA3YzcyNGJkODViNDkxNDViMTI1YTVhNWU5ZWQ1MmNmNWM2ODYxMDEwNjY2ZDhmMGRiIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1571685711",
            "Host": "glidedsky.com",
            "Referer": "http://glidedsky.com/level/crawler-font-puzzle-1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        }
        return headers

    def parse(self, number):
        # font_face = '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'
        # b = base64.b64decode(font_face)
        # with open('font.ttf', 'wb') as f:
        #     f.write(b)
        #
        # font = TTFont('font.ttf')
        # font.saveXML('01.xml')
        #
        tff_dict = {'8': '0', '5': '1', '1': '2', '3': '3', '6': '4', '0': '5', '7': '6', '4': '7', '9': '8',
                    '2': '9'}
        text = requests.get(url=self.url.format(number), headers=self.get_headers()).text
        html = etree.HTML(text)
        false_number = html.xpath("//div[@class='col-md-1']/text()")
        false_number = list(map(lambda item: re.sub('\s+', '', item), false_number))
        false_number = list(filter(None, false_number))
        print(false_number)
        true_number_list = []
        true_number = ''
        for i in false_number:
            for j in i:
                new = j.replace(j, tff_dict[j])
                true_number += new
            true_number_list.append(true_number)
            true_number = ''
        print(true_number_list)
        result = 0
        for i in true_number_list:
            result += int(i)
        return result

    def run(self):
        result = 0
        for i in range(1, 1001):
            result += self.parse(i)
        print(result)


if __name__ == '__main__':
    spider = SkySpider()
    spider.run()
