#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 爬取YY评级基本信息.py
# @Author: lattesea
# @Date  : 2019/10/7
# @Desc  :
import requests
import json
import csv
from fake_useragent import UserAgent
import time
import random


class YYpingjiSpider_basic():
    def __init__(self):
        self.url = 'https://api.ratingdog.cn/v1/search?limit=10&offset=0&type=3&qtext=&filter=%7B%7D&_=1570391570681'
        self.url2 = 'https://api.ratingdog.cn/v1/GetIssuerInfo?IssuerID={}&IssuerType=1001'
        self.url3 = 'https://api.ratingdog.cn/v1/GetIssuerInfo?IssuerID={}&IssuerType=1002'

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

    def parse_basic_message_1002(self, IssuerID):
        url = self.url3.format(IssuerID)
        basic_message = {}
        html_json = requests.get(url=url, headers=self.get_headers()).text
        html_py = json.loads(html_json)
        for i in html_py['rows']:
            basic_message['IssuerName'] = html_py['rows']['IssuerName']
            basic_message['CorporateRating'] = html_py['rows']['CorporateRating']
            basic_message['RatingAgency'] = html_py['rows']['RatingAgency']
            basic_message['Holder'] = html_py['rows']['Holder']
            basic_message['Industry'] = html_py['rows']['Industry']
            basic_message['Nature'] = html_py['rows']['Nature']
            basic_message['YYRating'] = html_py['rows']['YYRating']
            basic_message['IssuerType'] = html_py['rows']['IssuerType']
            basic_message['CreditAnalysis'] = html_py['rows']['CreditAnalysis']
            basic_message['PlatformImportance'] = html_py['rows']['CtExtendInfo']['PlatformImportance']
            basic_message['PrincipalBusiness'] = html_py['rows']['CtExtendInfo']['PrincipalBusiness']
            basic_message['GDP'] = html_py['rows']['CtExtendInfo']['GDP']
            basic_message['Revenue'] = html_py['rows']['CtExtendInfo']['Revenue']
            basic_message['YYRatio'] = html_py['rows']['CtExtendInfo']['YYRatio']
            basic_message['IssuerCity'] = html_py['rows']['CtExtendInfo']['IssuerCity']
            basic_message['ADLevel'] = html_py['rows']['CtExtendInfo']['ADLevel']
        print(basic_message)
        return basic_message

    def parse_basic_message_1001(self, IssuerID):
        url = self.url2.format(IssuerID)
        basic_message = {}
        html_json = requests.get(url=url, headers=self.get_headers()).text
        html_py = json.loads(html_json)
        for i in html_py['rows']:
            basic_message['IssuerName'] = html_py['rows']['IssuerName']
            basic_message['CorporateRating'] = html_py['rows']['CorporateRating']
            basic_message['RatingAgency'] = html_py['rows']['RatingAgency']
            basic_message['Holder'] = html_py['rows']['Holder']
            basic_message['Industry'] = html_py['rows']['Industry']
            basic_message['Nature'] = html_py['rows']['Nature']
            basic_message['YYRating'] = html_py['rows']['YYRating']
            basic_message['IssuerType'] = html_py['rows']['IssuerType']
            basic_message['CreditAnalysis'] = html_py['rows']['CreditAnalysis']
            basic_message['YYIndustry'] = html_py['rows']['CyExtendInfo']['YYIndustry']
            basic_message['YYIndustryId'] = html_py['rows']['CyExtendInfo']['YYIndustryId']
            basic_message['IndustrylStatus'] = html_py['rows']['CyExtendInfo']['IndustrylStatus']
            basic_message['ShareholderBackground'] = html_py['rows']['CyExtendInfo']['ShareholderBackground']
            basic_message['OperatingStatus'] = html_py['rows']['CyExtendInfo']['OperatingStatus']
            basic_message['FinancialStatus'] = html_py['rows']['CyExtendInfo']['FinancialStatus']
            basic_message['Focus'] = html_py['rows']['CyExtendInfo']['Focus']
        print(basic_message)
        return basic_message

    def save_csv_1001(self, result):
        keyword_list1 = ['IssuerName', 'CorporateRating', 'RatingAgency', 'Holder', 'Industry', 'Nature', 'YYRating',
                         'IssuerType', 'CreditAnalysis', 'YYIndustry', 'YYIndustryId', 'IndustrylStatus',
                         'ShareholderBackground', 'OperatingStatus', 'FinancialStatus', 'Focus']

        with open('1001.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, keyword_list1)
            # for row in result:
            writer.writerow(result)

    def save_csv_1001_title(self):
        keyword_list1 = ['IssuerName', 'CorporateRating', 'RatingAgency', 'Holder', 'Industry', 'Nature', 'YYRating',
                         'IssuerType', 'CreditAnalysis', 'YYIndustry', 'YYIndustryId', 'IndustrylStatus',
                         'ShareholderBackground', 'OperatingStatus', 'FinancialStatus', 'Focus']
        with open('1001.csv', 'a', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(keyword_list1)

    def save_csv_1002(self, result):
        keyword_list2 = ['IssuerName', 'CorporateRating', 'RatingAgency', 'Holder', 'Industry', 'Nature', 'YYRating',
                         'IssuerType', 'CreditAnalysis', 'PlatformImportance', 'PrincipalBusiness', 'PrincipalBusiness',
                         'GDP', 'Revenue', 'YYRatio', 'IssuerCity', 'ADLevel']

        with open('1002.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, keyword_list2)
            # for row in result:
            writer.writerow(result)

    def save_csv_1002_title(self):
        keyword_list2 = ['IssuerName', 'CorporateRating', 'RatingAgency', 'Holder', 'Industry', 'Nature', 'YYRating',
                         'IssuerType', 'CreditAnalysis', 'PlatformImportance', 'PrincipalBusiness', 'PrincipalBusiness',
                         'GDP', 'Revenue', 'YYRatio', 'IssuerCity', 'ADLevel']
        with open('1002.csv', 'a', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(keyword_list2)

    def basic_run(self, IssuerID_IssuerType):
        print(IssuerID_IssuerType)
        self.save_csv_1001_title()
        self.save_csv_1002_title()
        for j in IssuerID_IssuerType:
            if j[1] == '产业':
                result = self.parse_basic_message_1001(j[0])
                self.save_csv_1001(result)
            elif j[1] == '城投':
                result = self.parse_basic_message_1002(j[0])
                self.save_csv_1002(result)
            time.sleep(random.uniform(1, 4))

# if __name__ == '__main__':
#     spider = YYpingjiSpider()
#     spider.run()
