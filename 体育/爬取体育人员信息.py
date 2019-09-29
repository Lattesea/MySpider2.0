#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 爬取体育人员信息.py
# @Author: lattesea
# @Date  : 2019/9/20
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
        text = requests.get(self.url, headers=self.get_headers()).text
        html = etree.HTML(text)
        link = html.xpath("//tr/td[@class='rank-name player noborderright']/h3/a[@class='team-name']/@href")
        print(link)
        return link

    def parse_two_page(self, url):
        text = requests.get(url, headers=self.get_headers())
        # doc = pq(text)

        html = etree.HTML(text.text)
        dict_message = {}
        player = html.xpath(
            "//div[@id='main']/header[@class='player']/div[@class='player-details']/h1[@class='player-name']/text()")
        now_age = html.xpath(
            "//div[@class='player-info']/div[@class='player-option medium']/span[@class='player-item'][1]/text()")
        exp = html.xpath(
            "//div[@class='player-info']/div[@class='player-option medium']/span[@class='player-item'][2]/text()")
        drafted = html.xpath(
            "//div[@class='player-info']/div[@class='player-option large']/span[@class='player-item'][1]/text()")
        country = html.xpath(
            "//div[@class='player-info']/div[@class='player-option large']/span[@class='player-item'][2]/text()")
        agents = html.xpath(
            "//div[@class='player-info']/div[@class='player-option large']/span[@class='player-item'][3]/text()")
        dict_message['player'] = player[0]
        dict_message['now_age'] = now_age[0]
        dict_message['exp'] = exp[0]
        dict_message['drafted'] = drafted[0]
        dict_message['country'] = country[0]
        dict_message['agents'] = agents[0]
        field = html.xpath(
            "//div[@class='player-info']/div[@class='player-option medium']/span[@class='player-item position']/text()")
        dict_message['field'] = field[0]
        message = html.xpath("//li[@id='contracts']/p/text()")
        dict_message['message'] = message[0]
        current_contract = html.xpath(
            "//li[@id='contracts']/table[@class='salaryTable salaryInfo hidden-xs'][1]/tbody/tr[@class='notop']/td[@class='contract-item'][1]/span/text()")
        dict_message['current_contract'] = current_contract[1]
        current_signing_bonus = html.xpath(
            "//li[@id='contracts']/table[@class='salaryTable salaryInfo hidden-xs'][1]/tbody/tr[@class='notop']/td[@class='contract-item'][2]/span/text()")
        dict_message['current_signing_bonus'] = current_signing_bonus[1]
        current_average_salary = html.xpath(
            "//li[@id='contracts']/table[@class='salaryTable salaryInfo hidden-xs'][1]/tbody/tr[@class='notop']/td[@class='contract-item'][3]/span/text()")
        dict_message['current_average_salary'] = current_average_salary[1]
        current_free_agent = html.xpath(
            "//li[@id='contracts']/table[@class='salaryTable salaryInfo hidden-xs'][1]/tbody/tr[@class='notop']/td[@class='contract-item noright']/span/text()")
        dict_message['current_free_agent'] = current_free_agent[1]
        current_year = html.xpath(
            "//table[@class='playerTable rtable'][1]/tbody/tr/td[@class='playercontracttable']/table[@class='salaryTable current']/tbody/tr[@class='salaryRow']/td/a/text()")
        current_age = html.xpath(
            "//table[@class='playerTable rtable'][1]/tbody/tr/td[@class='playercontracttable']/table[@class='salaryTable current']/tbody/tr[@class='salaryRow']/td[3]/span[@class='info']/text()")
        current_base_salary = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr/td[5]/span/text()")
        current_signing_bonus = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr/td[6]/span/text()")
        luxury_tax_salary = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr/td[7]/span/text()")
        dict_message['luxury_tax_salary'] = luxury_tax_salary[0]
        current_payroll_salary = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr/td["
                                            "8]/span/text()")
        current_adjusted_salary = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr/td["
                                             "9]/span/text()")
        yearly_cash1 = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr/td[10]/span[1]/text()")
        yearly_cash2 = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr/td[10]/span[2]/text()")
        current_yearly_cash = [i + j for i, j in zip(yearly_cash1, yearly_cash2)]
        list1 = []
        for i in zip(current_year, current_age, current_base_salary, current_signing_bonus, current_payroll_salary,
                     current_adjusted_salary, current_yearly_cash):
            list1.append(i)
        re_bds = '<div class="contract-details">.*?<ul>(.*?)</ul>'
        contract_note = re.compile(re_bds, re.S)
        print(html)
        r_list = contract_note.findall(str(html))
        dict_message['contract_note'] = contract_note
        sources = html.xpath("//*[@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr[15]/td/div/a/text()|//*["
                             "@id='contracts']/table[3]/tbody/tr/td/table/tbody/tr[16]/td/div/a/text()")
        dict_message['sources'] = sources
        previous_contarct = html.xpath("//*[@id='contracts']/table[5]/tbody/tr/td[1]/span[2]/text()")
        previous_signing_bonus = html.xpath('//*[@id="contracts"]/table[5]/tbody/tr/td[2]/span[2]/text()')
        previous_average_salary = html.xpath('//*[@id="contracts"]/table[5]/tbody/tr/td[3]/span[2]/text()')
        previous_free_agent = html.xpath('//*[@id="contracts"]/table[5]/tbody/tr/td[4]/span[2]/text()')
        dict_message['previous_contarct'] = previous_contarct[0]
        dict_message['previous_signing_bonus'] = previous_signing_bonus[0]
        dict_message['previous_average_salary'] = previous_average_salary[0]
        dict_message['previous_free_agent'] = previous_free_agent[0]
        previous_year = html.xpath('//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr/td[1]/a[2]/text()')
        previous_age = html.xpath('//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr/td[3]/text()')
        previous_base_salary = html.xpath('//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr/td[4]/span/text()')
        previous_signing_bonus1 = html.xpath(
            '//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr/td[5]/span/text()')
        previous_total_salary = html.xpath('//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr/td[6]/span/text()')
        previous_yearly_cash1 = html.xpath(
            '//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr/td[7]/span[1]/text()')
        previous_yearly_cash2 = html.xpath(
            '//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr/td[7]/span[2]/text()')
        previous_yearly_cash = [i + j for i, j in zip(previous_yearly_cash1, previous_yearly_cash2)]
        list2 = []
        for j in zip(previous_year, previous_age, previous_base_salary, previous_signing_bonus1, previous_total_salary,
                     previous_yearly_cash):
            list2.append(j)
        trade = html.xpath('//*[@id="contracts"]/table[7]/tbody/tr/td/table/tbody/tr[7]/td/div/ul/li/text()')
        dict_message['trade'] = trade
        dict_message['current_message'] = list1
        dict_message['previous_message'] = list2
        # print(player, age, exp, drafted, country, agents, field, message, current_contract,
        #       current_contract_signing_bonus, current_contract_average_salary, current_contract_free_agent)

        # print(dict_message)
        print(r_list)
        # return [dict_message]

    def save_csv(self, result):
        headers = ['player', 'now_age', 'exp', 'drafted', 'country', 'agents', 'field', 'message', 'current_contract',
                   'current_signing_bonus', 'current_average_salary', 'current_free_agent', 'luxury_tax_salary',
                   'contract_note', 'sources', 'previous_contarct', 'previous_signing_bonus', 'previous_average_salary',
                   'previous_free_agent', 'trade', 'current_message', 'previous_message']
        with open('tiyu.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            for row in result:
                writer.writerow(row)

    def run(self):
        link = self.parse_one_page()
        # for i in link:
        #     try:
        #         result = self.parse_two_page(i)
        #         # self.save_csv(result)
        #         # print("写入成功")
        #     except:
        #         print("不知道为啥")
        for i in link:
            self.parse_two_page(i)


if __name__ == '__main__':
    spider = TiyuSpider()
    spider.run()
