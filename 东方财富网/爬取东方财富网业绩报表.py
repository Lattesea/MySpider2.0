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
import csv
import time

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

    def parse(self, number):
        param = {
            "type": "YJBB21_YJBB",
            "token": "70f12f2f4f091e459a279469fe49eca5",
            "st": "latestnoticedate",
            "sr": "-1",
            "p": number,
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

    def replace_str(self, number):
        response = self.parse(number)
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
        sname = re.findall('sname":"(.*?)"', response)  # 股票简称
        scode = re.findall('scode":"(.*?)"', response)  # 股票代码
        basiceps = re.findall('basiceps":"(.*?)"', response)  # 每股收益
        totaloperatereve = re.findall('totaloperatereve":"(.*?)"', response)  # 营业收入
        ystz = re.findall('ystz":"(.*?)"', response)  # 营业收入同比增长
        yshz = re.findall('yshz":"(.*?)"', response)  # 营业收入季度环比增长
        parentnetprofit = re.findall('parentnetprofit":"(.*?)"', response)  # 净利润
        sjltz = re.findall('sjltz":"(.*?)"', response)  # 净利润同比增长
        sjlhz = re.findall('sjlhz":"(.*?)"', response)  # 净利润季度环比增长
        roeweighted = re.findall('roeweighted":"(.*?)"', response)  # 净值产收益率
        bps = re.findall('bps":"(.*?)"', response)  # 每股净资产
        mgjyxjje = re.findall('mgjyxjje":"(.*?)"', response)  # 每股经营现金流量
        xsmll = re.findall('xsmll":"(.*?)"', response)  # 销售毛利率
        publishname = re.findall('publishname":"(.*?)"', response)  # 所属行业
        reportdate = re.findall('reportdate":"(.*?)"', response)  # 更新日期
        # print(sname, scode, basiceps, totaloperatereve, ystz, yshz, parentnetprofit, sjltz, sjlhz, roeweighted, bps,
        #       mgjyxjje, xsmll, publishname, reportdate)
        result = zip(sname, scode, basiceps, totaloperatereve, ystz, yshz, parentnetprofit, sjltz, sjlhz, roeweighted,
                     bps, mgjyxjje, xsmll, publishname, reportdate)
        return result

    def save(self, result):
        with open('reuslt.csv', mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

    def run(self):
        for i in range(1, 78):
            result = self.replace_str(i)
            self.save(result)
            time.sleep(1)


if __name__ == '__main__':
    spider = DongfangSpider()
    spider.run()
