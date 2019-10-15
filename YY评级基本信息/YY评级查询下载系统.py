#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-15 下午2:18 
# @Author : Lattesea 
# @File : YY评级查询下载系统.py 
"""
    该套系统用于用户查询YY评级信息,并且下载保存为文件
"""
import requests
from fake_useragent import UserAgent
import time
import json


class YYpingjiSpider(object):
    def __init__(self):
        self.url = ''

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

    def params(self, keyword):
        timestamp = str(int(time.time() * 1000))
        kw = {
            "limit": "10",
            "offset": "0",
            "type": "3",
            "qtext": keyword,
            "filter": "{}",
            "_": timestamp
        }
        return kw

    def parse(self):
        html_json = requests.get(url=self.url, params=self.params(), headers=self.get_headers()).text
        html_py = json.loads(html_json)
        print(html_py)

    def index_page(self):
        print("***************************")
        print("*** 欢迎使用YY评级查询系统 ***")
        print("*-------------------------*")
        print("*          功能            *")
        print("*         1.查询           *")
        print("*         2.下载           *")
        print("***************************")
        select = input("请选择功能:")
        return select

    def query_page(self):
        print("***************************")
        print("*         查询界面         *")
        print("*-------------------------*")
        print("***    输入空格返回上一级  ***")
        print("***************************")
        keyword = input("请输入查询关键字:")
        if keyword == ' ':
            self.index_page()
        return keyword

    def run(self):
        button = self.index_page()
        if button == '1':
            self.query_page()


if __name__ == '__main__':
    # print(int(time.time() * 1000))
    spider = YYpingjiSpider()
    # spider.index_page()
    spider.run()
