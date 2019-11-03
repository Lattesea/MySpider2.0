#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tiyu2.py
# @Author: lattesea
# @Date  : 2019/9/21
# @Desc  :
import requests
import csv
from fake_useragent import UserAgent
import random
from lxml import etree
from pyquery import PyQuery as pq
import re


class TiyuSpider(object):
    def __init__(self):
        self.url = 'https://www.spotrac.com/mlb/rankings/2019/contract-value/'
        self.url2 = 'https://www.spotrac.com/mlb/los-angeles-angels/mike-trout-8553/'

    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        return headers

    def parse_one_page(self):
        k = {
            'ajax': 'true',
            'mobile': 'false'
        }
        text = requests.post(url=self.url, headers=self.get_headers(), data=k).text
        html = etree.HTML(text)
        link = html.xpath("//tr/td[@class='rank-name player noborderright']/h3/a[@class='team-name']/@href")
        print(link)
        return link

    def parse_two_page(self, url):
        text = requests.get(url, headers=self.get_headers()).text
        html = etree.HTML(text)
        dict_message = {'player': '-', 'field': '-', 'age': '-', 'exp': '-', 'Drafted:': '-', 'Country:': '-',
                        'College:': '-', 'Agent(s):': '-', 'current_info': '-', 'Contract:': '-', 'SigningBonus:': '-',
                        'AverageSalary:': '-', 'FreeAgent:': '-',
                        'current_contract_table12': '-', 'Contract:_previous': '-', 'SigningBonus_previous': '-',
                        'AverageSalary_previous': '-', 'FreeAgent:_previous': '-',
                        'previous contracts_table2': '-'}
        player = html.xpath(
            "//div[@id='main']/header[@class='player']/div[@class='player-details']/h1[@class='player-name']//text()")
        table1 = html.xpath('//*[@id="main"]/header/div[2]/div/div[1]//text()')
        table1 = list(map(lambda item: re.sub('\s+', '', item), table1))
        table1 = list(filter(None, table1))
        table2 = html.xpath('//*[@id="main"]/header/div[2]/div/div[2]//text()')
        table2 = list(map(lambda item: re.sub('\s+', '', item), table2))
        table2 = list(filter(None, table2))
        table3 = html.xpath("//li[@id='contracts']/p/text()")
        table3 = list(map(lambda item: re.sub('\s+', '', item), table3))
        table3 = list(filter(None, table3))
        table4 = html.xpath('//*[@id="contracts"]/table[1]/tbody/tr//text()')
        table4 = list(map(lambda item: re.sub('\s+', '', item), table4))
        table4 = list(filter(None, table4))
        table5 = html.xpath('//*[@id="contracts"]/table[3]/tbody/tr/td/table/tbody//text()')
        table5 = list(map(lambda item: re.sub('\s+', '', item), table5))
        table5 = list(filter(None, table5))
        table6 = html.xpath('//*[@id="contracts"]/table[last()-2]/tbody/tr//text()')
        table6 = list(map(lambda item: re.sub('\s+', '', item), table6))
        table6 = list(filter(None, table6))
        table7 = html.xpath('//*[@id="contracts"]/table[last()-1]/tbody/tr/td/table/tbody//text()')
        table7 = list(map(lambda item: re.sub('\s+', '', item), table7))
        table7 = list(filter(None, table7))
        dict_message['player'] = player[0]
        dict_message['field'] = table1[0]
        dict_message['age'] = table1[2]
        dict_message['exp'] = table1[4]
        print(table2)
        list1 = table2[::2]
        list2 = table2[1::2]
        list3 = zip(list1, list2)
        for i in list3:
            dict_message[i[0]] = i[1]

            # if i == 'Drafted:':
            #     dict_message['drafted'] = next(table2)
            # if i == 'College:':
            #     dict_message['college'] = next(table2)
            # if i == 'Agent(s):':
            #     dict_message['agent(s)'] = next(table2)
            # if i == 'Country:':
            #     dict_message['country'] = next(table2)

        # dict_message['field_age_exp'] = table1
        # dict_message['Drafted..'] = table2
        dict_message['current_info'] = table3
        # dict_message['current_contract_table1'] = table4
        if table4[0] != 'Contract:':
            table4 = ['Contract:', '-', 'SigningBonus:', '-', 'AverageSalary:', '-', 'FreeAgent:', '-']
        list4 = table4[::2]
        list5 = table4[1::2]
        list6 = zip(list4, list5)
        for j in list6:
            dict_message[j[0]] = j[1]
        dict_message['current_contract_table12'] = table5
        # dict_message['previous contracts_table1'] = table6
        if table6[0] != 'Contract:':
            table6 = ['Contract:', '-', 'SigningBonus', '-', 'AverageSalary', '-', 'FreeAgent:', '-']
        list7 = table6[::2]
        list7_change = []
        for z in list7:
            list7_change.append(z + '_previous')
        list8 = table6[1::2]
        list9 = zip(list7_change, list8)
        for k in list9:
            dict_message[k[0]] = k[1]
        dict_message['previous contracts_table2'] = table7
        return [dict_message]

    def save_csv(self, result):
        headers = ['player', 'field', 'age', 'exp', 'Drafted:', 'Country:',
                   'College:', 'Agent(s):', 'current_info', 'Contract:', 'SigningBonus:', 'AverageSalary:',
                   'FreeAgent:',
                   'current_contract_table12', 'Contract:_previous', 'SigningBonus_previous',
                   'AverageSalary_previous', 'FreeAgent:_previous', 'previous contracts_table2']
        with open('tiyu19改.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, headers)
            # writer.writeheader()
            for row in result:
                writer.writerow(row)

    def run(self):
        link = self.parse_one_page()
        for i in link:
            # try:
            result = self.parse_two_page(i)
            self.save_csv(result)
            print("写入成功")
            # except:
            #     print("不知道为啥")


if __name__ == '__main__':
    spider = TiyuSpider()
    spider.run()
