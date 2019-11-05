#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-05 5:14
# @Author: Lattesea
# @File: 计算总和字体反爬篇test2.py
import requests
import re
from fake_useragent import UserAgent
import base64
from fontTools.ttLib import TTFont
from lxml import etree


class SkySpider(object):
    def __init__(self):
        self.url = 'http://glidedsky.com/level/web/crawler-font-puzzle-1?page={}'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.2.1001174242.1571676446; footprints=eyJpdiI6IjM2aG9pWENqd0ZXK3hKemEzcWhJdFE9PSIsInZhbHVlIjoiczAxQTlTKzBcL0dhckJsUXllRWQyK240UWFuWWdMUitOciszNVpCSHMwc2J6ejJEdDdJRm1KeVJGYld6eTgxd1QiLCJtYWMiOiIwNTc3N2FiMTQyMzZkYjg5MTgyOWY0MGUwNTc5MDBkMmQ0ODQ1YmM5ODYyMmViMTMxOWQzMmVmNjlkNTYxZjU4In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IlpcL0NnSTk5UVBJNXY5amdSWDdLa1d3PT0iLCJ2YWx1ZSI6InFSbGpEU0RDU3hyQzNsbFpLQU5oYkFMZGlHV1RXWVNhOTI2ZSsxQ3lqYW1ISUQ2d0VWbnZJSFpRZlwvV0JuTHpZaWdVZU5WV3hjR0ZrN1l4ZXdQQlRSSUkySFJBc3lmWGRGd25QRHQ2WGZnRmIzK3krYnlMXC9MUm1lY29Na1wvdldvU3hNQ0FNeVwvdVhFeUZGSHhKbXZHd2pINFpaMWNFU0N0ajNjSUJHMHJ3TlE9IiwibWFjIjoiMGQ0OWM2ZjdiNTNjYWM2OTg4YjYwMDY5YWFlNDEwYmYzZWE1YjM2NjQwYmUwNjY0MDViNzA5NDQ1ZmM4NDJlYyJ9; _gid=GA1.2.1226032585.1572901871; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1571676446,1571759255,1572901871; XSRF-TOKEN=eyJpdiI6IjVteHBxYTgyVERcL3pseU9FMWhoaDVRPT0iLCJ2YWx1ZSI6Imc1U240b1wvNHRtaHRJUk1hUFEzdTZ1MXN4cUs4eGpTbDJjUXV5Q1RIWUFBdUpPTXd4d0lyZWtDTkxTRXVKcnY4IiwibWFjIjoiNjNkNjUwNzE3ZjRkYWU0MzRiOWEwOWYwNzUxYWY2YjJhZTk3ZTQ2YTI0MjJkODNjOGY4NGE1YzAxMWViMDhmMiJ9; glidedsky_session=eyJpdiI6IkRPOGhIbU5LNEFwQUY0RUJ6YzJQUEE9PSIsInZhbHVlIjoib1FhaFlHSWhUa2E3dkxvcG5SYkZ2THJ1bnBRdDlEeDdHQ1B3dno3RGdubWc1QU1MQ1wvcmVRa0ZWXC9icmIzK0NpIiwibWFjIjoiMjEyOGRlMmM2MDJhMTkwODYxZjdmNDY3MmViNmZiZWIwNmE4YTZmOWMzYmQ1M2UyNmRkMjFlNTYxZjcxYmQ3OSJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1572903027; _gat_gtag_UA_75859356_3=1",
            "Host": "glidedsky.com",
            "Referer": "http://glidedsky.com/level/web/crawler-font-puzzle-1?page=2",
            "Upgrade-Insecure-Requests": "1",
            'User-Agent': ua.random
        }
        return headers

    def parse(self,number):
        base_font = TTFont('font.ttf')
        base_uni_list = base_font.getGlyphOrder()[1:]
        print(base_uni_list)
        origin_dict = {'one': 5, 'two': 8, 'three': 3, 'four': 4, 'five': 2, 'six': 7,
                       'seven': 0, 'eight': 9, 'nine': 6, 'zero': 1}
        # print(base_uni_list)
        response = requests.get(url=self.url.format(number), headers=self.get_headers()).text
        font_base64 = re.findall("base64,(.*?)\) format", response)
        b = base64.b64decode(font_base64[0])
        with open('font_online.ttf', 'wb') as f:
            f.write(b)
        online_font = TTFont('font_online.ttf')
        online_font.saveXML('online.xml')
        online_dict = {}
        online_uni_list = online_font.getGlyphOrder()[1:]
        print(online_uni_list)
        for uni2 in online_uni_list:
            obj2 = online_font['glyf'][uni2]
            for uni1 in base_uni_list:
                obj1 = base_font['glyf'][uni1]
                if obj1 == obj2:
                    online_dict[uni2] = origin_dict[uni1]

        html = etree.HTML(response)
        false_number = html.xpath("//div[@class='col-md-1']/text()")
        false_number = list(map(lambda item: re.sub('\s+', '', item), false_number))
        false_number = list(filter(None, false_number))
        print(false_number)
        print(online_dict)
        sum_true = 0
        for i in false_number:
            result = self.judge(i, online_dict)
            sum_true += int(result)
        return sum_true


    # def parse(self, number):
    #     response = requests.get(url=self.url.format(number), headers=self.get_headers()).text
    #     font_base64 = re.findall("base64,(.*?)\) format", response)
    #     b = base64.b64decode(font_base64[0])
    #     with open('font_online.ttf', 'wb') as f:
    #         f.write(b)
    #     online_font = TTFont('font_online.ttf')
    #     online_font.saveXML('online.xml')
    #     online_uni_list = online_font.getGlyphOrder()[1:]
    #     dict_font = {}
    #     n = 1
    #     for i in online_uni_list:
    #         if n == 10:
    #             n = 0
    #             dict_font[i] = n
    #         else:
    #             dict_font[i] = n
    #             n += 1
    #     print(dict_font)
    #     html = etree.HTML(response)
    #     false_number = html.xpath("//div[@class='col-md-1']/text()")
    #     false_number = list(map(lambda item: re.sub('\s+', '', item), false_number))
    #     false_number = list(filter(None, false_number))
    #     print(false_number)
    #     sum_true = 0
    #     for i in false_number:
    #         result = self.judge(i, dict_font)
    #         sum_true += int(result)
    #     return sum_true
    #
    # def judge(self, number, dict_font):
    #     replace_list = []
    #     for i in number:
    #         if i == '1':
    #             replace_list.append(dict_font['one'])
    #         elif i == '2':
    #             replace_list.append(dict_font['two'])
    #         elif i == '3':
    #             replace_list.append(dict_font['three'])
    #         elif i == '4':
    #             replace_list.append(dict_font['four'])
    #         elif i == '5':
    #             replace_list.append(dict_font['five'])
    #         elif i == '6':
    #             replace_list.append(dict_font['six'])
    #         elif i == '7':
    #             replace_list.append(dict_font['seven'])
    #         elif i == '8':
    #             replace_list.append(dict_font['eight'])
    #         elif i == '9':
    #             replace_list.append(dict_font['nine'])
    #         elif i == '0':
    #             replace_list.append(dict_font['zero'])
    #     true_number = ""
    #     for a in replace_list:
    #         true_number += str(a)
    #     print(true_number)
    #     return true_number

    def judge(self,number,online_dict):
        replace_list = []
        for i in number:
            if i == '1':
                replace_list.append(online_dict['one'])
            elif i == '2':
                replace_list.append(online_dict['two'])
            elif i == '3':
                replace_list.append(online_dict['three'])
            elif i == '4':
                replace_list.append(online_dict['four'])
            elif i == '5':
                replace_list.append(online_dict['five'])
            elif i == '6':
                replace_list.append(online_dict['six'])
            elif i == '7':
                replace_list.append(online_dict['seven'])
            elif i == '8':
                replace_list.append(online_dict['eight'])
            elif i == '9':
                replace_list.append(online_dict['nine'])
            elif i == '0':
                replace_list.append(online_dict['zero'])
        true_number = ""
        for a in replace_list:
            true_number += str(a)
        print(true_number)
        return true_number




    def run(self):
        result = 0
        for i in range(1, 1001):
            result += self.parse(i)
        print(result)


if __name__ == '__main__':
    spider = SkySpider()
    spider.run()
