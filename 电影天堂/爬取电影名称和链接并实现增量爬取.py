#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-25 上午11:17 
# @Author : Lattesea 
# @File : 爬取电影名称和链接并实现增量爬取.py 
import requests
import re
from fake_useragent import UserAgent
import random
import time
import pymysql
from hashlib import md5
from lxml import etree


class DianyingtiantangSpider(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='filmskydb',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def get_headers(self):
        """
            构建请求头
        :return:
        """
        ua = UserAgent()
        headers = {
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "zh-CN,zh;q=0.9",
            # "Cache-Control": "max-age=0",
            # "Connection": "keep-alive",
            # "Cookie": "UM_distinctid=16bdec86bc2679-07c211dd7aebc-15231708-1fa400-16bdec86bc3464; CNZZDATA1260535040=961678368-1562805532-https%253A%252F%252Fwww.baidu.com%252F%7C1562805532",
            # "Host": "www.dytt8.net",
            # "If-Modified-Since": "Thu, 19 Sep 2019 00:34:23 GMT",
            # "If-None-Match": "80d1b3fb816ed51:326",
            # "Sec-Fetch-Mode": "navigate",
            # "Sec-Fetch-Site": "none",
            # "Sec-Fetch-User": "?1",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua.random
        }
        return headers

    def parse_page(self, url):
        """
            解析一级页面
        :param url:
        :return:
        """
        text = requests.get(url=url, headers=self.get_headers())
        text.encoding = 'GBK'
        # 正则匹配第一页的二级页面链接
        re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        pattern = re.compile(re_bds, re.S)
        link_list = pattern.findall(text.text)
        for link in link_list:
            two_url = 'https://www.dytt8.net' + link
            # 生成指纹
            s = md5()
            s.update(two_url.encode())
            two_url_md5 = s.hexdigest()
            # 引入函数判断链接在数据库中是不是存在
            if self.judge_repetition(two_url_md5):
                self.parse_two_page(two_url)
                # 将指纹保存在数据库中
                ins = 'insert into request_finger values(%s)'
                self.cursor.execute(ins, [two_url_md5])
                # 切记要提交至数据库执行
                self.db.commit()
                # 随机产生爬取时间间隔
                time.sleep(random.uniform(1, 3))

    def judge_repetition(self, two_url_md5):
        """
            指纹判断
        :param two_url_md5:
        :return:
        """
        sel = 'select finger from request_finger where finger=%s'
        result = self.cursor.execute(sel, [two_url_md5])
        if not result:
            return True

    def parse_two_page(self, two_url):
        """
            提取二级页面的信息
        :param two_url:
        :return:
        """
        text = requests.get(url=two_url, headers=self.get_headers())
        text.encoding = 'GBK'

        html = etree.HTML(text.text)
        movie = html.xpath('//*[@id="header"]/div/div[3]/div[3]/div[1]/div[2]/div[1]/h1/font/text()')
        download = html.xpath('//tbody/tr/td/a/@href')
        # print(movie)
        # print(download)
        # return (movie[0], download[0])
        ins = 'insert into filmtab values(%s,%s)'
        film_list = movie + download
        self.cursor.execute(ins, film_list)
        self.db.commit()
        print(film_list)

    def run(self):
        """
            主函数
        :return:
        """
        for page in range(1, 201):
            one_url = self.url.format(page)
            self.parse_page(one_url)
            time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    spider = DianyingtiantangSpider()
    spider.run()
