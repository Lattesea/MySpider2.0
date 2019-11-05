#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-04 16:37
# @Author: Lattesea
# @File: 爬取东方财富网业绩报表.py
import requests
import re
from fake_useragent import UserAgent
from fontTools.ttLib import TTFont
import json


class DongfangSpider(object):
    def __init__(self):
        self.url = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?'

    def get_headers(self):
        ua = UserAgent()

        headers = {
            'Referer': 'http://data.eastmoney.com/bbsj/201909/yjbb.html',
            'User-Agent': ua.random
        }
        return headers

    def parse(self):
        param = {
            "type": "YJBB21_YJBB",
            "token": "70f12f2f4f091e459a279469fe49eca5",
            "st": "latestnoticedate",
            "sr": "-1",
            "p": "1",
            "ps": "50",
            "js": "var UgFdFova={pages:(tp),data: (x),font:(font)}",
            "filter": "(securitytypecode in ('058001001','058001002'))(reportdate=^2019-09-30^)",
            "rt": "52428561"
        }
        response = requests.get(url=self.url, headers=self.get_headers(), params=param).text
        print(response)
        return response

    # def parse_woff(self):
    #     response = self.parse()
    #     print(response)
    #     ua = UserAgent()
    #     response_woff = requests.get('http://data.eastmoney.com/bbsj/201909/yjbb.html', headers={
    #         'User-Agent': ua.random
    #     })
    #     font_url = re.findall('"WoffUrl":"(.*?)"', response_woff.text)[0]
    #     # print(font_url)
    #     font_response = requests.get(font_url)
    #     with open('字体文件.woff', mode='wb') as f:
    #         f.write(font_response.content)
    #     fi = TTFont('字体文件.woff')
    #     fi.saveXML('font.xml')
    #     font_map = fi['cmap'].getBestCmap()
    #     print(font_map)
    #     d = {'x': '.', 'wqqdzs': 3, 'zrwqqdl': 2, 'bgldyy': 7, 'zwdxtdy': 8, 'whyhyx': 9,
    #          'qqdwzl': 1, 'zbxtdyc': 4, 'sxyzdxn': 6, 'bdzypyc': 0, 'nhpdjl': 5}
    #     for key in font_map:
    #         font_map[key] = d[font_map[key]]
    #
    #     print(font_map)
    #
    #     for key in font_map:
    #         response = response.replace('&#' + str(hex(key))[1::].upper() + ';', response)
    #         print('&#' + str(hex(key))[1::].upper() + ';')
    #     print(type(response))
    #     print(response)

    def replace_str(self):
        response = self.parse()
        print(response)
        dict_FontMapping = {}
        response_replace = re.findall('"FontMapping":(.*?)}}', response)[0]
        response_code = re.findall('"code":"(.*?)"', response_replace)
        response_values = re.findall('"value":(.*?)}', response_replace)
        response_zip = zip(response_code, response_values)
        for i in response_zip:
            dict_FontMapping[i[0]] = i[1]
        print(dict_FontMapping)
        for key in dict_FontMapping:
            response = response.replace(str(key), dict_FontMapping[key])
        print(response)

    def run(self):
        self.replace_str()


if __name__ == '__main__':
    spider = DongfangSpider()
    spider.run()
