#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 19-11-18 下午5:37
# @Author : Lattesea
# @File : 爬取人民邮电出版社经管书籍.py
import requests
import json
from fake_useragent import UserAgent


class RenminSpider(object):
    def __init__(self):
        self.url = 'https://ptpress.com.cn/bookinfo/getBookListForEBTag'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "74",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "gr_user_id=7abace4a-7d31-496e-ad26-a9471db9b044; gr_session_id_9311c428042bb76e=bdf6ef7f-f0fe-4044-afaa-4a297675e371; gr_session_id_9311c428042bb76e_bdf6ef7f-f0fe-4044-afaa-4a297675e371=true; JSESSIONID=784187530EA185098EE7D9369191A688",
            "Host": "ptpress.com.cn",
            "Origin": "https://ptpress.com.cn",
            "Referer": "https://ptpress.com.cn/shopping/search?tag=search&orderStr=hot&level1=75424c57-6dd7-4d1f-b6b9-8e95773c0593",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": ua.random,
            "X-Requested-With": "XMLHttpRequest",
        }
        return headers

    def parse(self):
        data = {
            "page": "1",
            "rows": "18",
            "bookTagId": "75424c57 - 6dd7 - 4d1f - b6b9 - 8e95773c0593",
            "orderStr": "hot"
        }
        reponse = requests.get(url=self.url, headers=self.get_headers(), data=data,verify=False).text
        print(reponse)
        result = json.loads(reponse)
        print(result)


    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = RenminSpider()
    spider.run()
