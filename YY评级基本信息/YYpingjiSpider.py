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
from YYpingji_ui import *
import os
from basic_information_spider import YYpingjiSpider_basic
from valuation_spider import YYpingjiSpider_valuation
from secondary_spider import YYpingjiSpider_secondary
from history_spider import YYpingjiSpider_history
from financial_spider import YYpingjiSpider_financial


class YYpingjiSpider(object):
    def __init__(self):
        self.url = 'https://api.ratingdog.cn/v1/autocomplete?'
        self.url2 = 'https://api.ratingdog.cn/v1/search?'
        self.ui = YYpingjipage()

    def get_headers(self):
        """
            构建一部分请求参数
        :return:
        """
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
        """
            构建返回所有条件数据的请求头参数
        :param keyword:
        :return:
        """
        timestamp = str(int(time.time() * 1000))
        kw = {
            "limit": "100",
            "offset": "0",
            "type": "3",
            "qtext": keyword,
            "filter": "{}",
            "_": timestamp
        }
        return kw

    def search_params(self, keyword):
        """
            构建搜索的请求头
        :param keyword:
        :return:
        """
        kw = {
            "qtext": keyword,
            "type": "4",
            "filter": "{}"
        }
        return kw

    def parse(self, keyword):
        html_json = requests.get(url=self.url, params=self.params(keyword), headers=self.get_headers()).text
        html_py = json.loads(html_json)
        print(html_py)

    def query_page_select(self):
        """
            查询界面菜单栏的选择
        :return:
        """
        keyword = self.ui.query_page()
        if keyword == '1':
            return self.main_query_show()
        elif keyword == '2':
            self.ui.YY_level_page()
        elif keyword == '3':
            self.ui.listed_page()
        elif keyword == '4':
            self.ui.enterprise_nature_page()
        elif keyword == '5':
            return self.keyword_query_show()

    def main_query_show(self):
        select = self.ui.main_types_page()

        timestamp = str(int(time.time() * 1000))
        filter=None
        if select == ' ':
            self.query_page_select()
        elif select == '1':
            filter = '1002'

        elif select == '2':
            filter = '1001'

        params = {
            "limit": "100",
            "offset": "0",
            "type": "3",
            "qtext": "",
            "filter": "{'IssuerType': %s}" % filter,
            "_": timestamp
        }
        html_json = requests.get(url=self.url2, )

    def keyword_query_show(self):
        """
            获得关键字搜索的数据
        :return:
        """
        keyword = self.ui.keyword_query()
        if keyword == ' ':
            self.query_page_select()
        params = self.params(keyword)
        html_json = requests.get(url=self.url2, headers=self.get_headers(), params=params).text
        html_py = json.loads(html_json)
        IssuerID_list = []
        for i in html_py['rows']:
            print(i)
            IssuerID_list.append((i['IssuerID'], i['IssuerType']))
        print(IssuerID_list)
        return IssuerID_list

    def crawler_select(self, IssuerID_list):
        select = self.ui.crawler_page()
        if select == '1':
            basic = YYpingjiSpider_basic()
            basic.basic_run(IssuerID_IssuerType=IssuerID_list)
        elif select == '2':
            valuation = YYpingjiSpider_valuation()
            valuation.valuation_run(IssuerID_IssuerType=IssuerID_list)
        elif select == '3':
            secondary = YYpingjiSpider_secondary()
            secondary.sencodary_run(IssuerID_IssuerType=IssuerID_list)
        elif select == '4':
            history = YYpingjiSpider_history()
            history.history_run(IssuerID_IssuerType=IssuerID_list)
        elif select == '5':
            financial = YYpingjiSpider_financial()
            financial.financial_run(IssuerID_IssuerType=IssuerID_list)

    def run(self):
        button = self.ui.index_page()
        if button == '1':
            IssuerID_list = self.query_page_select()
            print(IssuerID_list)
            self.crawler_select(IssuerID_list)


if __name__ == '__main__':
    # print(int(time.time() * 1000))
    spider = YYpingjiSpider()
    # spider.index_page()
    spider.run()
