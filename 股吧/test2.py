#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-5 上午11:37 
# @Author : Lattesea 
# @File : test2.py 
"""
    爬取股吧所有的文章标题,日期,作者,阅读数,评论数
"""
import requests
from requests.exceptions import RequestException
from lxml import etree
import csv


def get_one_index_page(url):
    """
        获取请求页的源码
    :param url:
    :return:
    """
    try:
        headers = {
            'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                          '76.0.3809.100Safari / 537.36',

        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(text):
    """
        解析网页源代码
    :param text:
    :return:
    """
    html = etree.HTML(text)
    title_name = html.xpath("//span[@class='l3 a3']/a/text()")
    # author = html.xpath("//span[@class='l4 a4']/a/font/text()")
    read_count = html.xpath("//span[@class='l1 a1']/text()")
    comments = html.xpath("//span[@class='l2 a2']/text()")
    time = html.xpath("//span[@class='l5 a5']/text()")

    return zip(title_name, read_count[1::], comments[1::], time[1::])


def change_page(number):
    """
        翻页
    :param number:
    :return:
    """
    base_url = 'http://guba.eastmoney.com/'
    url = base_url + 'list,zssh000016_%d.html' % number
    return url


def save_to_csv(result, filename):
    """
        保存
    :param result:
    :param filename:
    :return:
    """
    with open('%s' % filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(result)
        print(result)


# def main():
#     list01 = []
#     for i in range(265, 271):
#         number = change_page(i)
#         text = get_one_index_page(number)
#         result = parse_page(text)
#         for i in result:
#             list01.append(i)
#             save_to_csv(list01, 'data.csv')
#             list01.clear()

def main():
    n = 1
    for i in range(1, 270):
        if i % 20 == 0:
            n += 1
        number = change_page(i)
        text = get_one_index_page(number)
        result = parse_page(text)
        for i in result:
            save_to_csv(i, 'data%s.csv' % n)


if __name__ == '__main__':
    main()
    # url = 'http://guba.eastmoney.com/list,zssh000016_265.html'
    # text = get_one_index_page(url)
    # result = parse_page(text)
    # print(result)

    # url = 'http://guba.eastmoney.com/list,zssh000016_265.html'
    # text = get_one_index_page(url)
    # result = parse_page(text)
    # for i in result:
    #     print(i)
