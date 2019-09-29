#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-27 下午3:02 
# @Author : Lattesea 
# @File : 爬取豆瓣teacher.py 
import requests
import time
import random
import re
from fake_useragent import UserAgent


class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0

    # 获取随机headers
    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}

        return headers

    # 获取页面
    def get_page(self, params):
        headers = self.get_headers()
        res = requests.get(url=self.url, params=params, headers=headers)
        res.encoding = 'utf-8'
        # 返回 python 数据类型
        html = res.json()
        self.parse_page(html)

    # 解析并保存数据
    def parse_page(self, html):
        item = {}
        # html为大列表 [{电影1信息},{},{}]
        for one in html:
            # 名称 + 评分
            item['name'] = one['title'].strip()
            item['score'] = float(one['score'].strip())
            # 打印测试
            print(item)
            self.i += 1

    # 获取电影总数
    def total_number(self, type_number):
        # F12抓包抓到的地址
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_number)
        headers = self.get_headers()
        html = requests.get(url=url, headers=headers).json()
        total = int(html['total'])

        return total

    # 获取所有电影的名字和对应type值
    def get_all_type_films(self):
        # 获取 类型和类型码
        url = 'https://movie.douban.com/chart'
        headers = self.get_headers()
        html = requests.get(url=url, headers=headers).text
        re_bds = r'<a href=.*?type_name=(.*?)&type=(.*?)&.*?</a>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        # 存放所有类型和对应类型码大字典
        type_dict = {}
        menu = ''
        for r in r_list:
            type_dict[r[0].strip()] = r[1].strip()
            # 获取input的菜单，显示所有电影类型
            menu += r[0].strip() + '|'

        return type_dict, menu

    # 主函数
    def main(self):
        # 获取type的值
        type_dict, menu = self.get_all_type_films()
        menu = menu + '\n请做出你的选择:'
        name = input(menu)
        type_number = type_dict[name]
        # 获取电影总数
        total = self.total_number(type_number)
        for start in range(0, (total + 1), 20):
            params = {
                'type': type_number,
                'interval_id': '100:90',
                'action': '',
                'start': str(start),
                'limit': '20'
            }
            # 调用函数,传递params参数
            self.get_page(params)
            # 随机休眠1-3秒
            time.sleep(random.randint(1, 3))
        print('电影数量:', self.i)


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.main()
