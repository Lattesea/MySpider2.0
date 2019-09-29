#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-24 下午3:03 
# @Author : Lattesea 
# @File : 爬取电影名称和链接.py 
"""
    爬取电影天堂2019年的电影名称和链接
"""
import requests
import csv
from fake_useragent import UserAgent
from lxml import etree
import re
import time
import random


class DianyingtiantangSpider(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        # self.url2 = 'https://www.dytt8.net/html/gndy/dyzz/20190918/59138.html'

    def get_headers(self):
        """
            构造请求头
        :return:
        """
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "UM_distinctid=16bdec86bc2679-07c211dd7aebc-15231708-1fa400-16bdec86bc3464; CNZZDATA1260535040=961678368-1562805532-https%253A%252F%252Fwww.baidu.com%252F%7C1562805532",
            "Host": "www.dytt8.net",
            "If-Modified-Since": "Thu, 19 Sep 2019 00:34:23 GMT",
            "If-None-Match": "80d1b3fb816ed51:326",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua.random
        }
        return headers

    def re_func(self, re_bds, html):
        """
            正则表达式解析出第一页的排名链接
        :param re_bds:
        :param html:
        :return:
        """
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_index_page(self, url):
        """
            请求解析第一页的链接
        :param url:
        :return:
        """
        text = requests.get(url=url, headers=self.get_headers())
        text.encoding = 'GBK'
        # print(text.text)
        re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # link = re.findall('<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>', text.text)
        # html = etree.HTML(text.text)
        # link = html.xpath("//ul/table[@class='tbspan'][1]/tbody/tr[4]/td/text()")
        link = self.re_func(re_bds, text.text)
        print(link)
        # print(text)
        return link

    def parse_two_page(self, url):
        """
            请求解析第二页的电影名和下载链接
        :param url:
        :return:
        """
        text = requests.get(url=url, headers=self.get_headers())
        # print(text.text)
        text.encoding = 'GBK'

        html = etree.HTML(text.text)
        movie = html.xpath('//*[@id="header"]/div/div[3]/div[3]/div[1]/div[2]/div[1]/h1/font/text()')
        download = html.xpath('//tbody/tr/td/a/@href')
        # movie=re.findall("",text.text)
        print(movie)
        print(download)
        # print(html)
        return (movie[0], download[0])

    def save_csv(self, result):
        """
            保存到csv文件
        :param result:
        :return:
        """
        with open('movie.csv', 'a', newline='')as f:
            writer = csv.writer(f)
            writer.writerows(result)

    def run(self):
        """
            主函数
        :return:
        """
        for i in range(1, 201):
            url1 = self.url.format(i)
            list_result = []
            link = self.parse_index_page(url1)
            for j in link:
                url2 = 'https://www.dytt8.net' + j
                try:
                    result = self.parse_two_page(url2)
                    print(result)
                    list_result.append(result)
                    time.sleep(random.uniform(1, 3))
                except Exception as err:
                    print(err)
            self.save_csv(list_result)
            print("第%s页保存成功" % i)


if __name__ == '__main__':
    spider = DianyingtiantangSpider()
    spider.run()
