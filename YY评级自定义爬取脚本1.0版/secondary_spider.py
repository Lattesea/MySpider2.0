#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-18 下午4:28 
# @Author : Lattesea 
# @File : secondary_spider.py 
import requests
import json
import csv
from fake_useragent import UserAgent
import time
import random


class YYpingjiSpider_secondary(object):
    def __init__(self):
        self.url = 'https://api.ratingdog.cn/v1/QueryIssuerTradedHistoricalApilist?IssuerID={}'

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
        secondary = {}
        html_json = requests.get(url=url, headers=self.get_headers()).text
        html_py = json.loads(html_json)
        print(html_py)
        for i in html_py['rows']:
            secondary['BondCode'] = i['BondCode']
            secondary['ShortName'] = i['ShortName']
            secondary['TradedDate'] = i['TradedDate']
            secondary['ResidualMaturity'] = i['ResidualMaturity']
            secondary['TradedYTM'] = i['TradedYTM']
            secondary['PriceDiff'] = i['PriceDiff']
            secondary['YYDiff'] = i['YYDiff']
            secondary['YYRating'] = i['YYRating']
            secondary['TradedIntrinsic'] = i['TradedIntrinsic']
            secondary['CreditRating'] = i['CreditRating']
            secondary['IssueMethod'] = i['IssueMethod']
        print(secondary)
        return secondary

    def save_csv(self, result):
        keyword_list1 = ['BondCode', 'ShortName', 'TradedDate', 'ResidualMaturity', 'TradedYTM', 'PriceDiff', 'YYDiff',
                         'YYRating', 'TradedIntrinsic', 'CreditRating', 'IssueMethod']
        with open('二级成交.csv', 'a', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(keyword_list1)
        with open('二级成交.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, keyword_list1)
            # for row in result:
            writer.writerow(result)

    def sencodary_run(self, IssuerID_IssuerType):
        print(IssuerID_IssuerType)
        for j in IssuerID_IssuerType:
            result = self.parse(j[0])
            self.save_csv(result)
            time.sleep(random.uniform(1, 4))
            print("%s存入成功" % result)
