#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-9 下午7:39 
# @Author : Lattesea 
# @File : 爬取河北新闻网投诉信息.py 
import requests
import random
from fake_useragent import UserAgent
from lxml import etree
import csv
import time


class HebeitousuSpider(object):
    def __init__(self):
        self.url = 'http://yglz.tousu.hebnews.cn/l-1001-5-'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def get_hidden(self):
        """
            构建post请求的一部分
        :return:
        """
        try:
            response = requests.post(self.url)
            html = response.content.decode("utf-8")
        except Exception as e:
            print(e)

        tree = etree.HTML(html)  # 解析html
        hids = tree.xpath('//input[@type="hidden"]')  # 获取隐藏域

        # 声明一个字典，用来存储后面的数据
        common_param = {}
        # 循环取值
        for ipt in hids:
            common_param.update(
                {ipt.get("name"): ipt.get("value")})
        return common_param

    def parse(self, number, common_param):
        """
            构建完整的post请求,并解析页面
        :param number:
        :param common_param:
        :return:
        """

        common_param.update({"__CALLBACKPARAM": f"Load|*|{number}",
                             "__CALLBACKID": "__Page",
                             "__EVENTTARGET": "",
                             "__EVENTARGUMENT": ""})
        text = requests.post(url=self.url, headers=self.get_headers(), data=common_param).text
        html = etree.HTML(text)

        unit = html.xpath("//div[@class='listcon']/span[1]/p/a/text()")
        # print(unit)
        type = html.xpath("//div[@class='listcon']/span[2]/p/text()")
        # print(type)
        topic = html.xpath("//div[@class='listcon']/span[3]/p/a/text()")
        # print(topic)
        date = html.xpath("//div[@class='listcon']/span[4]/p/text()")
        # print(date)
        result = zip(unit, type, topic, date)
        # print(result)
        return result

    def save(self, result):
        """
            将数据存进csv文件
        :param result:
        :return:
        """
        with open('result.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

    def run(self):
        """
            主函数
        :return:
        """
        common_param = self.get_hidden()

        for number in range(1, 972):
            list_result = []
            try:
                result = self.parse(number=number, common_param=common_param)
                for i in result:
                    list_result.append(i)
                print(list_result)
                self.save(list_result)
                print("第%d页写入成功" % number)
                time.sleep(random.uniform(1, 3))
            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    spider = HebeitousuSpider()
    spider.run()
