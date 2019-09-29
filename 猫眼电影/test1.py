#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-4 下午6:35 
# @Author : Lattesea 
# @File : test1.py 
"""
    用xpath爬取猫眼电影
"""
import requests
from requests.exceptions import RequestException
from lxml import etree
import csv
import re


def get_page(url):
    """
        获取网页的源代码
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
    movie_name = html.xpath("//p[@class='name']/a/text()")
    actor = html.xpath("//p[@class='star']/text()")
    actor = list(map(lambda item: re.sub('\s+', '', item), actor))
    time = html.xpath("//p[@class='releasetime']/text()")
    grade1 = html.xpath("//p[@class='score']/i[@class='integer']/text()")
    grade2 = html.xpath("//p[@class='score']/i[@class='fraction']/text()")
    new = [grade1[i] + grade2[i] for i in range(min(len(grade1), len(grade2)))]
    ranking = html.xpath("///dd/i/text()")
    return zip(ranking, movie_name, actor, time, new)


def change_page(number):
    """
        翻页
    :param number:
    :return:
    """
    base_url = 'https://maoyan.com/board/4'
    url = base_url + '?offset=%s' % number
    return url


def save_to_csv(result, filename):
    """
        保存
    :param result:
    :param filename:
    :return:
    """
    with open('%s' % filename, 'a') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(result)


def main():
    """
    主函数
    :return:
    """
    for i in range(0, 100, 10):
        url = change_page(i)
        text = get_page(url)
        result = parse_page(text)
        print(result)
        # for j in result:
        #     save_to_csv(j, filename='message.csv')


if __name__ == '__main__':
    main()
    # url = 'https://maoyan.com/board/4'
    # text = get_page(url)
    # print(text)

    # url = 'https://maoyan.com/board/4'
    # text = get_page(url)
    # movie_name = parse_page(text)
    # print(movie_name)

    # url = 'https://maoyan.com/board/4'
    # text = get_page(url)
    # actor = parse_page(text)
    # for i in actor:
    #     print(i)
    # print(re.sub('\s', '', str(actor)))
    # print(re.split(r'\\n', str(actor)))
    # print(list(map(lambda item: re.sub('\s+', '', item), actor)))
