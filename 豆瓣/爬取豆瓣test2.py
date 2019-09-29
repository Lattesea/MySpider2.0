#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-27 上午11:38 
# @Author : Lattesea 
# @File : 爬取豆瓣test2.py 
import requests
from fake_useragent import UserAgent
import json


class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        # 返回电影信息的链接
        self.url2 = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=60&limit=20'
        # 返回电影总数的链接
        self.url3 = 'https://movie.douban.com/j/chart/top_list_count?type=11&interval_id=100%3A90'
        self.url4 = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1'
        self.i = 0

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "bid=LIjHECwiqx8; douban-fav-remind=1; "
                      "acw_tc=2760823d15682778903202703e4d80a50a682a65f113a246f78daf9597bbf7; ll=118281; "
                      "_vwo_uuid_v2=DDF227ECBE4CA85C8A663EC3A8DA27A98|af0d67a30ee8055abf40ef6b7c323e37; acw_sc__v3=5d8da960f361c5b476ef5bb3838a11989eac6e2e; acw_sc__v2=5d8da95fc256b073a36cdba9db155954dc579050; ap_v=0,6.0; __utma=30149280.1542742931.1568277891.1568637520.1569565044.6; __utmb=30149280.0.10.1569565044; __utmc=30149280; __utmz=30149280.1569565044.6.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.343267989.1568277891.1568637520.1569565044.6; __utmb=223695111.0.10.1569565044; __utmc=223695111; __utmz=223695111.1569565044.6.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1569565044%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D-_vZNQxBgOoI1iqsArm6T5Z4iiQd_VmuHKjCkFPk8TJyZAHhCTxmXLl5r34lIEIW%26wd%3D%26eqid%3D80596205000ff7b1000000065d8da970%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=ac6757b02b1fdcd9.1568277892.6.1569565106.1568637522.",
            "Host": "movie.douban.com",
            "Referer": "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": ua.random,
            "X-Requested-With": "XMLHttpRequest",
        }
        return headers

    def parse_page(self, url):
        # dict_movie = {}
        list_movie = []
        html_json = requests.get(url=url, headers=self.get_headers()).text
        # print(html_json)
        html_py = json.loads(html_json)
        # print(html_py)
        for data in html_py:
            # dict_movie['title'] = data['title']
            # dict_movie['actor'] = data['actors']
            title = data['title']
            actors = data['actors']
            # list_movie.append(dict_movie)
            list_movie.append((title, actors))
            # list_movie.append(title)
        # print(list_movie)
        # return list_movie
        print(list_movie)

    def run(self):
        self.parse_page(self.url2)


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()
