#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-24 下午5:18 
# @Author : Lattesea 
# @File : teacher_code.py 
from urllib import request
import re
from fake_useragent import UserAgent
import time
import random


class FilmSkySpider(object):
    def __init__(self):
        # 一级页面url地址
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

    # 获取html功能函数
    def get_html(self, url):
        ua=UserAgent()
        headers = {
            'User-Agent':ua.random
        }
        req = request.Request(url=url, headers=headers)
        print(type(req))
        res = request.urlopen(req)
        # 通过网站查看网页源码,查看网站charset='gb2312'
        # 如果遇到解码错误,识别不了一些字符,则 ignore 忽略掉
        html = res.read().decode('gb2312', 'ignore')
        print(html)

        return html

    # 正则解析功能函数
    def re_func(self, re_bds, html):
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)

        return r_list

    # 获取数据函数 - html是一级页面响应内容
    def parse_page(self, one_url):
        html = self.get_html(one_url)
        re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # one_page_list: ['/html/xxx','/html/xxx','/html/xxx']
        one_page_list = self.re_func(re_bds, html)

        for href in one_page_list:
            two_url = 'https://www.dytt8.net' + href
            self.parse_two_page(two_url)
            # uniform: 浮点数,爬取1个电影信息后sleep
            time.sleep(random.uniform(1, 3))

    # 解析二级页面数据
    def parse_two_page(self, two_url):
        item = {}
        html = self.get_html(two_url)
        re_bds = r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
        # two_page_list: [('名称1','ftp://xxxx.mkv')]
        two_page_list = self.re_func(re_bds, html)

        item['name'] = two_page_list[0][0].strip()
        item['download'] = two_page_list[0][1].strip()

        print(item)

    def main(self):
        for page in range(1, 201):
            one_url = self.url.format(page)
            self.parse_page(one_url)
            # uniform: 浮点数
            time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    spider = FilmSkySpider()
    spider.main()
