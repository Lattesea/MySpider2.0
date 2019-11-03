#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-18 下午5:14 
# @Author : Lattesea 
# @File : history_spider.py 
import requests
import json
import csv
from fake_useragent import UserAgent
import time
import random


class YYpingjiSpider_history(object):
    def __init__(self):
        self.url = 'https://api.ratingdog.cn/v1/GetIssuerYYRatingApi?IssuerID={}'

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
        history = {}
        html_json = requests.get(url=url, headers=self.get_headers()).text
        html_py = json.loads(html_json)
        print(html_py)
        for i in html_py['rows']:
            history['IssuanceCode'] = i['IssuanceCode']
            history['ShortName'] = i['ShortName']
            history['PriceRange'] = i['PriceRange']
            history['YYRating'] = i['YYRating']
            history['Term'] = i['Term']
            history['Couponrate'] = i['Couponrate']
            history['StartDateOfIssue'] = i['StartDateOfIssue']
        print(history)
        return history

    def save_csv(self, result):
        keyword_list1 = ['IssuanceCode', 'ShortName', 'PriceRange', 'YYRating', 'Term', 'Couponrate',
                         'StartDateOfIssue']
        with open('历史.csv', 'a', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(keyword_list1)
        with open('历史.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, keyword_list1)
            writer.writerow(result)

    def history_run(self, IssuerID_IssuerType):
        print(IssuerID_IssuerType)
        for j in IssuerID_IssuerType:
            result = self.parse(j[0])
            self.save_csv(result)
            time.sleep(random.uniform(1, 4))
            print("%s存入成功" % result)
