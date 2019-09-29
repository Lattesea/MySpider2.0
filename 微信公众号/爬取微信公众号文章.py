#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-17 下午6:00 
# @Author : Lattesea 
# @File : 爬取微信公众号文章.py 
import requests
import csv
import random
import time
from fake_useragent import UserAgent
import json


class WeixingongzhonghaoSpider(object):
    def __init__(self):
        self.url = 'https://mp.weixin.qq.com/cgi-bin/appmsg'

    def get_headers(self, number):
        ua = UserAgent()
        headers = {'User-Agent': ua.random,
                   'Cookie': "noticeLoginFlag=1; RK=7I4gfI3ZQF; ptcz=9a5055feaf5d9317241baacbc611cf87e56aada3f6bf7933d8fdf1ec8d02c6cc; pgv_pvi=7335965696; pgv_pvid=2710863603; pgv_flv=32.0 r0; eas_sid=m1i596p0U4v7R3K2N1P2r1O930; tvfe_boss_uuid=c8dddab409702850; o_cookie=809695135; uin_cookie=o0809695135; ied_qq=o0809695135; pac_uid=1_809695135; ua_id=jlcQ6Uu2kUq2R9jrAAAAAAOuybK_XycaZ5oNMOwM1n8=; noticeLoginFlag=1; mm_lang=zh_CN; pgv_si=s9744411648; uuid=a6b9e30c0f3c4e4f3b97f589cfe0a7a7; bizuin=3573685930; ticket=b4c38515441666a6671f1bb7b79181eb14c6ee51; ticket_id=gh_53b196a21b22; cert=2OxCwCA7obP1mLfBgajDbXiHUrlMjai_; data_bizuin=3573685930; data_ticket=bMVMuBMMmsgdQdhjHtdh20qsnWMbRrX14bn2m08QzTVbXLziBZUHIUZ0vQG89aQN; slave_sid=OEN0UV9QZU1UZUVITWhsWVFxZHFqX1pQQnpUelRuVVlPeWM0Y0RzU0dzdlR2V05qbTNjMzlCNkFqUlZOM2xmcWJzaUdFQ1BmQXNLd2ZWT2FEMDhhcWFySVlpcnk4UzZ4NTlkd1dJQklJZGlGTkhESGlPM3FuSjlmOERDbGNJY1pYZ1lsNWZLUlpuaW5leTdm; slave_user=gh_53b196a21b22; xid=b5ac932ac1a774501305c8dd416bc94b; openid2ticket_oqh4C1fNsjjECxlwVP0mILPeOj5I=lwWG5Soghge+AQxq8Y6o8COGCtWFPBfyJ7en0cHNwEo="
                   }
        self.params = {
            "token": "836816546",
            "lang": "zh_CN",
            "f": "json",
            "ajax": "1",
            # "random": "0.41128823139554127",
            "action": "list_ex",
            "begin": number,
            "count": "5",
            "query": "",
            "fakeid": "MTI2NzIyNzM0MQ==",
            "type": "9",
        }
        result = {'headers': headers, 'params': self.params}
        return result

    def get_page(self, number):
        list_result = []
        dict_result = {}
        html_json = requests.get(url=self.url, headers=self.get_headers(number)['headers'], params=self.get_headers()[
            'params']).text
        html_py = json.loads(html_json)
        print(html_py)
        for message in html_py['app_msg_list']:
            dict_result['title'] = message['title']
            dict_result['link'] = message['link']
            list_result.append(dict_result)
        return list_result

    def save_csv(self, result):
        with open('电脑爱好者.csv', 'a')as f:
            writer = csv.writer(f)
            writer.writerrows(result)

    def run(self):
        for i in range(0, 80, 5):
            self.get_page(i)


if __name__ == '__main__':
    spider = WeixingongzhonghaoSpider()
    spider.run()
