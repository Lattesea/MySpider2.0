#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-18 下午3:34 
# @Author : Lattesea 
# @File : valuation_spider.py 
import requests
import json
import csv
from fake_useragent import UserAgent
import time
import random


class YYpingjiSpider_valuation(object):
    def __init__(self):
        self.url = 'https://api.ratingdog.cn/v1/queryIssuerYYbondyieldApilist?IssuerID={}'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://www.ratingdog.cn",
            "Referer": "https://www.ratingdog.cn/",
            "Sec-Fetch-Mode": "cors",
            "User-Agent": ua.random
        }
        return headers

    def parse(self, IssuerID):
        url = self.url.format(IssuerID)
        valuation = {}
        html_json = requests.get(url=url, headers=self.get_headers()).text
        html_py = json.loads(html_json)
        print(html_py)
        for i in html_py['rows']:
            valuation['BondCode'] = i['BondCode']
            valuation['ShortName'] = i['ShortName']
            valuation['ResidualMaturity'] = i['ResidualMaturity']
            valuation['MaturityYield'] = i['MaturityYield']
            valuation['DefaultRate'] = i['DefaultRate']
            valuation['IssueMethod'] = i['IssueMethod']
            valuation['AssessDate'] = i['AssessDate']
        print(valuation)
        return valuation

    def save_csv(self, result):
        keyword_list1 = ['BondCode', 'ShortName', 'ResidualMaturity', 'MaturityYield', 'DefaultRate', 'IssueMethod',
                         'AssessDate']
        with open('估值数据.csv', 'a', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(keyword_list1)
        with open('估值数据.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, keyword_list1)
            # for row in result:
            writer.writerow(result)

    def valuation_run(self, IssuerID_IssuerType):
        print(IssuerID_IssuerType)
        for j in IssuerID_IssuerType:
            result = self.parse(j[0])
            self.save_csv(result)
            time.sleep(random.uniform(1, 4))
            print("%s存入成功" % result)
