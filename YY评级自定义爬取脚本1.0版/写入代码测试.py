#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-18 下午7:27 
# @Author : Lattesea 
# @File : 写入代码测试.py 
import csv

keyword_list1 = ['RankingStr', 'LastTotalEquityScore', 'EBITDAScore',
                 'AverTotalProfitDefrayNonCurrentPLThreeYearsScore', 'EBITDAIBDebtScore',
                 'AssetLiabilityRatioScore', 'CurrentRatioScore', 'RealizableAssetShortTermIBDebtScore',
                 'ListedScore', 'CompanyNatureScore', 'FinCostsIBDebtScore']
with open('写入测试.csv', 'a', newline='')as f:
    writer = csv.writer(f)
    writer.writerow(keyword_list1)
