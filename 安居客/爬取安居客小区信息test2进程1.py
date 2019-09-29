#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-23 上午9:34 
# @Author : Lattesea 
# @File : 爬取安居客小区信息test2.py
"""
    爬取安居客所有小区信息
"""
import requests
from fake_useragent import UserAgent
from lxml import etree
import csv
import re
import time
import random


class AnjukeSpider(object):
    def __init__(self):
        self.url = 'https://qd.anjuke.com/community/p{}/'

    def get_headers(self):
        """
            构建请求头
        :return:
        """
        ua = UserAgent()
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "aQQ_ajkguid=534DDCC9-5DBA-263A-CF4D-SX0716083828; isp=true; 58tj_uuid=e559fdad-fdb9-4a73-8c60-9e6e3bf82987; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1563237510; als=0; _ga=GA1.2.1881437242.1569052175; ctid=30; wmda_uuid=edd62dcc1e73bddc16beeb56087fd1f8; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; sessid=F6826357-F68F-1E17-B5A1-99FEA17341CA; lps=http%3A%2F%2Fwww.anjuke.com%2F%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DcuNIKoO-jX3CGzD7komT_lY2umPIHgZjjBdMMdFnpZHirHVPOLorVTafN32HS5R_%26ck%3D7150.2.84.414.190.439.289.917%26shh%3Dwww.baidu.com%26sht%3D02003390_42_hao_pg%26wd%3D%26eqid%3Dc2951ba5003c81ad000000065d881f86; twe=2; wmda_session_id_6289197098934=1569202063874-b62b0050-2be7-3851; _gid=GA1.2.388348263.1569202065; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DcuNIKoO-jX3CGzD7komT_lY2umPIHgZjjBdMMdFnpZHirHVPOLorVTafN32HS5R_%2526ck%253D7150.2.84.414.190.439.289.917%2526shh%253Dwww.baidu.com%2526sht%253D02003390_42_hao_pg%2526wd%253D%2526eqid%253Dc2951ba5003c81ad000000065d881f86; new_uv=3; new_session=0",
            "referer": "https://qd.anjuke.com/community/?from=navigation",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": ua.random
        }
        return headers

    def get_link(self, url):
        """
            解析页面获取每个小区的二级页面链接和价格
        :param url:
        :return:
        """
        text = requests.get(url=url, headers=self.get_headers()).text
        html = etree.HTML(text)
        link = html.xpath("//h3/a/@href")
        price = html.xpath('//*[@id="list-content"]/div/div[2]/p[1]/strong/text()')
        print(link)
        print(price)
        for i in zip(link, price):
            print(i)
        return zip(link, price)

    def parse_message(self, url, price):
        """
            二级页面解析需要的信息
        :param url:
        :param price:
        :return:
        """
        dict_result = {'小区': '-', '地址': '-', '价格': '-', '物业类型：': '-', '物业费：': '-', '总建面积：': '-', '总户数：': '-',
                       '建造年代：': '-',
                       '停车位：': '-',
                       '容积率：': '-',
                       '绿化率：': '-',
                       '开发商：': '-', '物业公司：': '-', '所属商圈：': '-', '二手房房源数：': '-', '租房源数：': '-', '相关学校：': '-'}

        text = requests.get(url=url, headers=self.get_headers()).text
        html = etree.HTML(text)
        table1 = html.xpath('/html/body/div[2]/div[3]/div[1]/h1//text()')  # 提取小区名和地址
        table1 = list(map(lambda item: re.sub('\s+', '', item), table1))  # 去掉换行符制表符
        table1 = list(filter(None, table1))  # 去掉上一步产生的空元素
        dict_result['小区'] = table1[0]
        dict_result['地址'] = table1[1]
        dict_result['价格'] = price
        table2 = html.xpath('//*[@id="basic-infos-box"]/dl//text()')
        table2 = list(map(lambda item: re.sub('\s+', '', item), table2))
        table2 = list(filter(None, table2))
        table2_list1 = table2[::2]
        table2_list2 = table2[1::2]
        table2_list3 = zip(table2_list1, table2_list2)
        for j in table2_list3:
            dict_result[j[0]] = j[1]
        # price = html.xpath('//*[@id="basic-infos-box"]/div[1]/span[1]/text()')  #价格数据在json文件里面,所以这个没办法匹配到
        # dict_result['价格'] = price[0]
        table3 = html.xpath('//*[@id="basic-infos-box"]/div[2]//text()')
        table3 = list(map(lambda item: re.sub('\s+', '', item), table3))
        table3 = list(filter(None, table3))
        table3_list1 = table3[::2]
        table3_list2 = table3[1::2]
        table3_list3 = zip(table3_list1, table3_list2)
        for j in table3_list3:
            dict_result[j[0]] = j[1]
        print(dict_result)
        return dict_result

    def save_csv(self, result):
        """
            将信息保存进入csv文件
        :param result:
        :return:
        """
        headers = {'小区', '地址', '价格', '物业类型：', '物业费：', '总建面积：', '总户数：',
                   '建造年代：',
                   '停车位：',
                   '容积率：',
                   '绿化率：',
                   '开发商：', '物业公司：', '所属商圈：', '二手房房源数：', '租房源数：', '相关学校：'}
        with open('青岛.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, headers)
            # writer.writeheader()
            for row in result:
                writer.writerow(row)

    def run(self):
        """
            主函数
        :return:
        """
        C = 1
        for i in range(1, 101):  # 总的272页
            url = self.url.format(i)
            link = self.get_link(url)
            list_result = []
            for j in link:
                try:
                    result = self.parse_message(j[0], j[1])
                    time.sleep(round(random.randint(1, 3), C))
                    list_result.append(result)
                except Exception as err:
                    print(err)
            self.save_csv(list_result)
            print("第%s页储存成功" % i)

        # url = 'https://qd.anjuke.com/community/view/875393?from=Filter_1&hfilter=filterlist'
        # self.parse_message(url)
        # self.get_link()


if __name__ == '__main__':
    spider = AnjukeSpider()
    spider.run()
