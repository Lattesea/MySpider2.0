#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/9/8 19:47 
# @Author : 国鑫 
# @Site :  
# @File : test2.py 
# @Software: PyCharm
import requests
import time
import random
from fake_useragent import UserAgent
import re
from requests.exceptions import RequestException
from lxml import etree
import csv
from pyquery import PyQuery as pq


class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://gz.lianjia.com/ershoufang/'
        self.address = ['tianhe', 'yuexiu', 'liwan', 'haizhu', 'panyu', 'baiyun', 'huangpugz',
                        'conghua',
                        'zengcheng', 'huadou', 'nansha', 'nanhai', 'shunde']

    def get_headers(self):
        """
            随机产生请求头
        :return:
        """
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        return headers

    def get_page(self, url):
        """
            获取网页源代码
        :param url:
        :return:
        """
        while True:
            try:
                headers = self.get_headers()
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response.text
                return None
            except RequestException as err:
                print(err)

    def parse_index_link(self, text):
        """
            解析索引页,获得a链接和价格
        :param text:
        :return:
        """
        html = etree.HTML(text)
        link = html.xpath("//div[@class='title']/a/@href")
        # price = html.xpath("//div[@class='priceInfo']/div[@class='totalPrice']/span/text()")
        return link

    # def parse_index_price(self, text):
    #     html = etree.HTML(text)
    #     price = html.xpath("//div[@class='priceInfo']/div[@class='totalPrice']/span/text()")
    #     return price

    def parse_index_parse_number(self, text):
        """
            解析索引页获得最大页数
        :param text:
        :return:
        """
        html = etree.HTML(text)
        number1 = html.xpath("//div[@class='page-box house-lst-page-box']/@page-data")[0]
        number2 = eval(number1)
        number = number2["totalPage"]
        if number == None:
            number = 1
            return number
        return number

    def parse_message_page(self, text):
        """
            匹配房子信息
        :param text:
        :return:
        """
        html = etree.HTML(text)
        ID = html.xpath("//div[@class='houseRecord']/span[@class='info']/text()")
        Direction = html.xpath("//div[@class='type']/div[@class='mainInfo']/text()")
        District = html.xpath("//div[@class='areaName']/span[@class='info']/a[2]/text()")
        Elevator = html.xpath("//div[@class='base']/div[@class='content']/ul/li[11]/text()")
        Floor1 = html.xpath("//div[@class='room']/div[@class='subInfo']/text()")
        Floor = list(map(lambda item: re.findall('\d+', item), Floor1))
        Garden = html.xpath("//div[@class='communityName']/a[1]/text()")
        Layout = html.xpath("//div[@class='room']/div[@class='mainInfo']/text()")
        doc = pq(html)
        Price = doc(".price .total")
        Region = html.xpath("//div[@class='areaName']/span[@class='info']/a[1]/text()")
        Renovation1 = html.xpath("//div[@class='type']/div[@class='subInfo']/text()")
        Renovation = list(Renovation1[0].split('/')[-1:])
        Size1 = html.xpath("//div[@class='area']/div[@class='mainInfo']/text()")
        # Size = list(map(lambda item: re.findall('^[+-]?(0|([1-9]\d*))(\.\d+)?$', item), Size1))
        InsideSize1 = html.xpath("//div[@class='base']/div[@class='content']/ul/li[5]/text()")
        # InsideSize = list(map(lambda item: re.findall('^[+-]?(0|([1-9]\d*))(\.\d+)?$', item), InsideSize1))
        Year1 = html.xpath("//div[@class='area']/div[@class='subInfo']/text()")
        Year = list(map(lambda item: re.findall('\d+', item), Year1))
        if len(Year[0]) == 0:
            Year = '未知'
            return Direction[0], District[0], Elevator[0], Floor[0][0], Garden[0], ID[0], Layout[0], Price.text(), \
                   Region[
                       0], \
                   Renovation[
                       0], Size1[0], InsideSize1[0], Year
        return Direction[0], District[0], Elevator[0], Floor[0][0], Garden[0], ID[0], Layout[0], Price.text(), Region[
            0], \
               Renovation[
                   0], Size1[0], InsideSize1[0], Year[0][0]
        # return Price

    def save_to_csv(self, filename, result):
        """
        存入cav文件
        :param filename:
        :param result:
        :return:
        """

        with open('%s' % filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, dialect='excel')
            writer.writerow(result)

    # def run(self):
    #     """
    #         主函数
    #     :return:
    #     """
    #     for a in self.address:
    #         url1 = self.url + a + '/'
    #         text_index1 = self.get_page(url1)
    #         total_page_number = self.parse_index_parse_number(text_index1)
    #         for i in range(1, total_page_number):
    #             url2 = self.url + '%s' % a + '/pg%s' % i
    #             text_index = self.get_page(url2)
    #             link = self.parse_index_parse(text_index)
    #             for j in link:
    #                 url3 = j[0]
    #                 text_message = self.get_page(url3)
    #                 try:
    #                     message = self.parse_message_page(text_message)
    #                     for k in message:
    #                         k = list(k)
    #                         k.append(j[1])
    #                         print(k)
    #                         self.save_to_csv(filename='%s.csv' % a, result=k)
    #                         time.sleep(random.randint(1, 3))
    #                 except Exception as err:
    #                     print(err)
    def run(self, a):
        # a = 'huangpugz'
        url1 = self.url + a + '/'
        text_index1 = self.get_page(url1)
        total_page_number = self.parse_index_parse_number(text_index1)
        print(total_page_number)
        for i in range(1, total_page_number + 1):
            # n = 0
            list_message = []
            url2 = self.url + '%s' % a + '/pg%s' % i
            print(url2)
            text_index = self.get_page(url2)
            link = self.parse_index_link(text_index)
            # price = self.parse_index_price(text_index)
            print(link)
            # print(price)
            for j in link:
                print(j)
                text_message = self.get_page(j)
                try:
                    message = self.parse_message_page(text_message)
                    print(message)
                    # for k in message:
                    # message1 = list(message)
                    # print(type(message1))
                    # message1.append(price[n])
                    # n += 1
                    # print(message1)
                    list_message.append(message)
                except Exception as err:
                    print(err)
            for k in list_message:
                self.save_to_csv(filename='%s.csv' % a, result=list(k))
            list_message.clear()
            # time.sleep(random.randint(1, 3))
            foo = [0.1, 0.5, 0.4, 0.3]
            time.sleep(random.choice(foo))
            # except Exception as err:
            #     print(err)


if __name__ == '__main__':
    # from multiprocessing import Process

    spider = LianjiaSpider()

    list_address = ['huadou', 'nansha', 'nanhai', 'shunde']
    # other = ['haizhu', 'panyu', 'baiyun', 'huangpugz',
    #          'conghua',
    #          'zengcheng']
    for i in list_address:
        spider.run(i)
    # p_list = [spider.run('tianhe'), spider.run('yuexiu'), spider.run('liwan'), spider.run('huangpugz')]
    # p_list2 = [spider.run('panyu'), spider.run('baiyun'), spider.run('conghua'), spider.run('zengcheng')]
    # p_list3 = [spider.run('huadu'), spider.run('nansha'), spider.run('nanhai'), spider.run('shunde')]
    # # begin = time.time()

    # for i in range(4):
    #     p = Process(target=p_list[i])
    #     p.start()
    # stop = time.time()
    # print('执行时间:%.2f' % (stop - begin))
    # 测试能否返回网页源代码
    # lianjia = LianjiaSpider()
    # url = lianjia.url + '/tianhe/'
    # text = lianjia.get_page(url)
    # print(text)

    # 测试能否匹配出首页的所有a链接
    # lianjia = LianjiaSpider()
    # url = lianjia.url + '/tianhe/'
    # text = lianjia.get_page(url)
    # link = lianjia.parse_index_parse(text)
    # number = lianjia.parse_index_parse_number(text)
    # print(link)
    # print(number)

    # 测试能否匹配房子信息
    # lianjia = LianjiaSpider()
    # url = lianjia.url + '/108400186340.html'
    # text = lianjia.get_page(url)
    # result = lianjia.parse_message_page(text)
    # print(result)
    # lianjia.save_to_csv(result=result, filename='test.csv')
    # for i in result:
    #     print(i)

# lianjia = LianjiaSpider()
# url1 = lianjia.url + '/tianhe/'
# text1 = lianjia.get_page(url1)
# link = lianjia.parse_index_parse(text1)

# url2 = lianjia.url + '/108400186340.html'
# text2 = lianjia.get_page(url2)
# result = lianjia.parse_message_page(text2)
# for i in link[1]:
#     print(i)
#     for j in result:
#         j = list(j)
#         j.append(i)
#         print(j)
