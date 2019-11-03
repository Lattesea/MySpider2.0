#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-18 下午5:52 
# @Author : Lattesea 
# @File : financial_spider.py 
import requests
import json
import csv
from fake_useragent import UserAgent
import time
import random


class YYpingjiSpider_financial(object):
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
        financial = {}
        html_json = requests.get(url=url, headers=self.get_headers()).text
        html_py = json.loads(html_json)
        print(html_py)
        for i in html_py['rows']:
            financial['RankingStr'] = i['RankingStr']
            financial['LastTotalEquityScore'] = i['LastTotalEquityScore']
            financial['EBITDAScore'] = i['EBITDAScore']
            financial['AverTotalProfitDefrayNonCurrentPLThreeYearsScore'] = i[
                'AverTotalProfitDefrayNonCurrentPLThreeYearsScore']
            financial['AverOperNetCashThreeYearsIBDebtScore'] = i['AverOperNetCashThreeYearsIBDebtScore']
            financial['EBITDAIBDebtScore'] = i['EBITDAIBDebtScore']
            financial['AssetLiabilityRatioScore'] = i['AssetLiabilityRatioScore']
            financial['CurrentRatioScore'] = i['CurrentRatioScore']
            financial['RealizableAssetShortTermIBDebtScore'] = i['RealizableAssetShortTermIBDebtScore']
            financial['ListedScore'] = i['ListedScore']
            financial['CompanyNatureScore'] = i['CompanyNatureScore']
            financial['FinCostsIBDebtScore'] = i['FinCostsIBDebtScore']

        print(financial)
        return financial

    def save_csv(self, result):
        keyword_list1 = ['RankingStr', 'LastTotalEquityScore', 'EBITDAScore',
                         'AverTotalProfitDefrayNonCurrentPLThreeYearsScore', 'EBITDAIBDebtScore',
                         'AssetLiabilityRatioScore', 'CurrentRatioScore', 'RealizableAssetShortTermIBDebtScore',
                         'ListedScore', 'CompanyNatureScore', 'FinCostsIBDebtScore']
        with open('财务评分.csv', 'a', newline='')as f:
            writer = csv.writer(f)
            writer.writerow(keyword_list1)
        with open('财务评分.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, keyword_list1)
            # for row in result:
            writer.writerow(result)

    def financial_run(self, IssuerID_IssuerType):
        print(IssuerID_IssuerType)
        for j in IssuerID_IssuerType:
            result = self.parse(j[0])
            self.save_csv(result)
            time.sleep(random.uniform(1, 4))
            print("%s存入成功" % result)
