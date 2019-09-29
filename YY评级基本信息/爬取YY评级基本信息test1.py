#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-2 下午2:46 
# @Author : Lattesea 
# @File : 爬取YY评级基本信息test1.py 
"""
    爬取YY评级基本信息:
    发行主体,
    主体评级,
    评级机构,
    第一大股东,
    企业性质,
    YY评级,
    YY行业,
    主体类型,
    信用分析,
    行业情况,
    股东背景,
    经营状况,
    财务情况,
    重点关注.
"""
import requests
from requests.exceptions import RequestException
from lxml import etree
import csv
import json
import re
import time


def get_one_page(url):
    """
    获取网页源码
    :param url:
    :return:
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/76.0.3809.132 Safari/537.36',

        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_index_page(text):
    """
        解析出IssuerID码
    :param text:
    :return:
    """
    IssuerID = re.findall('\w{32}', text)
    IssuerType = re.findall('(产业)|(城投)', text)
    return zip(IssuerID, IssuerType)


def parse_message_page_1001(text):
    """
        匹配基本信息
    :param text:
    :return:
    """
    try:
        result = []
        dict = json.loads(text)
        dict_rows = dict['rows']
        IssuerName = dict_rows['IssuerName']
        result.append(IssuerName)
        CorporateRating = dict_rows['CorporateRating']
        result.append(CorporateRating)
        RatingAgency = dict_rows['RatingAgency']
        result.append(RatingAgency)
        Holder = dict_rows['Holder']
        result.append(Holder)
        Industry = dict_rows['Industry']
        result.append(Industry)
        Nature = dict_rows['Nature']
        result.append(Nature)
        YYRating = dict_rows['YYRating']
        result.append(YYRating)
        IssuerType = dict_rows['IssuerType']
        result.append(IssuerType)
        CreditAnalysis = dict_rows['CreditAnalysis']
        result.append(CreditAnalysis)
        CtExtendInfo = dict_rows['CtExtendInfo']
        result.append(CtExtendInfo)
        dict_CyExtendInfo = dict_rows['CyExtendInfo']
        YYIndustry = dict_CyExtendInfo['YYIndustry']
        result.append(YYIndustry)
        IndustrylStatus = dict_CyExtendInfo['IndustrylStatus']
        result.append(IndustrylStatus)
        ShareholderBackground = dict_CyExtendInfo['ShareholderBackground']
        result.append(ShareholderBackground)
        OperatingStatus = dict_CyExtendInfo['OperatingStatus']
        result.append(OperatingStatus)
        FinancialStatus = dict_CyExtendInfo['FinancialStatus']
        result.append(FinancialStatus)
        Focus = dict_CyExtendInfo['Focus']
        result.append(Focus)
    except:
        print("不知道为啥")
    finally:
        return result


def parse_message_page_1002(text):
    """
        匹配基本信息
    :param text:
    :return:
    """
    try:
        result = []
        dict = json.loads(text)
        dict_rows = dict['rows']
        IssuerName = dict_rows['IssuerName']
        result.append(IssuerName)
        CorporateRating = dict_rows['CorporateRating']
        result.append(CorporateRating)
        RatingAgency = dict_rows['RatingAgency']
        result.append(RatingAgency)
        Holder = dict_rows['Holder']
        result.append(Holder)
        Industry = dict_rows['Industry']
        result.append(Industry)
        Nature = dict_rows['Nature']
        result.append(Nature)
        YYRating = dict_rows['YYRating']
        result.append(YYRating)
        IssuerType = dict_rows['IssuerType']
        result.append(IssuerType)
        CreditAnalysis = dict_rows['CreditAnalysis']
        result.append(CreditAnalysis)
        CtExtendInfo = dict_rows['CtExtendInfo']
        result.append(CtExtendInfo)
        dict_CtExtendInfo = dict_rows['CtExtendInfo']
        PlatformImportance = dict_CtExtendInfo['PlatformImportance']
        result.append(PlatformImportance)
        PrincipalBusiness = dict_CtExtendInfo['PrincipalBusiness']
        result.append(PrincipalBusiness)
        GDP = dict_CtExtendInfo['GDP']
        result.append(GDP)
        Revenue = dict_CtExtendInfo['Revenue']
        result.append(Revenue)
        YYRatio = dict_CtExtendInfo['YYRatio']
        result.append(YYRatio)
        IssuerCity = dict_CtExtendInfo['IssuerCity']
        result.append(IssuerCity)
        ADLevel = dict_CtExtendInfo['ADLevel']
        result.append(ADLevel)
    except:
        print("不知道为啥")
    finally:
        return result


def change_url(url, IssuerType):
    base_url1 = 'https://api.ratingdog.cn/v1/GetIssuerInfo?'
    base_url2 = 'IssuerType=1001'
    base_url3 = 'IssuerType=1002'
    if IssuerType == '产业':
        new_url = base_url1 + 'IssuerID=%s&' % url + base_url2
        return new_url
    elif IssuerType == '城投':
        new_url = base_url1 + 'IssuerID=%s&' % url + base_url3
        return new_url


def change_page(number):
    """
        翻页
    :param number:
    :return:
    """
    base_url1 = 'https://api.ratingdog.cn/v1/search?limit=10'
    base_url2 = '&type=3&qtext=&filter=%7B%7D'
    url = base_url1 + '&offset=%d' % number + base_url2
    return url


def save_to_csv(result, filename):
    with open('%s' % filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(result)


def main():
    for i in range(0, 4601, 10):
        # n = 0
        url = change_page(i)
        text = get_one_page(url)
        IssuerID = parse_index_page(text)
        for j in IssuerID:
            # print(j)
            for k in j[1]:
                # print(k)
                if k == '城投':
                    IssuerType = '城投'
                    message_url = change_url(j[0], IssuerType)
                    message_text = get_one_page(message_url)
                    result = parse_message_page_1002(message_text)
                    filename = 'data1002.csv'
                    # if i % 200 == 0:
                    #     n += 1
                    #     filename = 'data%d.csv' % n
                    save_to_csv(result, filename)
                    print(result)
                elif k == '产业':
                    IssuerType = '产业'
                    message_url = change_url(j[0], IssuerType)
                    message_text = get_one_page(message_url)
                    result = parse_message_page_1001(message_text)
                    filename = 'data1001.csv'
                    # if i % 200 == 0:
                    #     n += 1
                    #     filename = 'data%d.csv' % n
                    save_to_csv(result, filename)
                    print(result)
        # time.sleep(1)


if __name__ == '__main__':
    main()
    # url = 'https://api.ratingdog.cn/v1/search?limit=10&offset=10&type=3&qtext=&filter=%7B%7D&_=1567407226219'
    # url='https://api.ratingdog.cn/v1/GetIssuerInfo?IssuerID=d69e76b36dc04b26b11bf66c559b41d4&IssuerType=1001'
    # url = 'https://www.ratingdog.cn/#/rating/rating?index=2'
    # text = get_one_page(url)
    # html = 1
    # print(html)

    # url = 'https://api.ratingdog.cn/v1/search?limit=10&offset=20&type=3&qtext=&filter=%7B%7D'
    # text = get_one_page(url)
    # IssuerID = parse_index_page(text)
    # for i in IssuerID:
    #     print(i)

    # url = 'https://api.ratingdog.cn/v1/GetIssuerInfo?IssuerID=f1aa1dc9f04a4c118858750b95320da9&IssuerType=1001'
    # text = get_one_page(url)
    # result = parse_message_page(text)
    # print(result)
