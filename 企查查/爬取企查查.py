#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-27 下午4:45 
# @Author : Lattesea 
# @File : 爬取企查查.py 
"""
    爬取企查查广州企业工商信息
"""
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
import time
import random


class QichachaSpider(object):
    def __init__(self):
        self.url = 'https://www.qichacha.com/g_GD_440100'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "zg_did=%7B%22did%22%3A%20%2216cd284fbf6ed-0edcf64c04eb71-30760d58-1fa400-16cd284fbf7587%22%7D; UM_distinctid=16cd284ffae4fd-0e8c4f756defd7-30760d58-1fa400-16cd284ffaf66c; _uab_collina=156690002758679334643286; acw_tc=7909f41715669000278057978ebccb8a7e75b65e66aa1c3fe0426874b2; QCCSESSID=c9sdu76ekeu2mi9ptm2tncg9f2; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1567170376,1569486079,1569570761; CNZZDATA1254842228=165282389-1566898255-%7C1569573108; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201569572788145%2C%22updated%22%3A%201569573812405%2C%22info%22%3A%201569486079205%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22901aae3b279bb2ae973eef6fc2e6efe0%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1569573813",
            "Host": "www.qichacha.com",
            "Referer": "https://www.qichacha.com/",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua.random
        }
        return headers

    def get_headers2(self):
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "zg_did=%7B%22did%22%3A%20%2216cd284fbf6ed-0edcf64c04eb71-30760d58-1fa400-16cd284fbf7587%22%7D; UM_distinctid=16cd284ffae4fd-0e8c4f756defd7-30760d58-1fa400-16cd284ffaf66c; _uab_collina=156690002758679334643286; acw_tc=7909f41715669000278057978ebccb8a7e75b65e66aa1c3fe0426874b2; QCCSESSID=c9sdu76ekeu2mi9ptm2tncg9f2; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1567170376,1569486079,1569570761; CNZZDATA1254842228=165282389-1566898255-%7C1569573108; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201569572788145%2C%22updated%22%3A%201569573812405%2C%22info%22%3A%201569486079205%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%22901aae3b279bb2ae973eef6fc2e6efe0%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1569573813",
            "Host": "www.qichacha.com",
            "Referer": "https://www.qichacha.com/g_GD_440100",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua.random
        }
        return headers

    def parse_index_page(self):
        text = requests.get(url=self.url, headers=self.get_headers()).text
        html = etree.HTML(text)
        name = html.xpath('//*[@id="searchlist"]/table/tbody/tr/td[2]/a//text()')
        name = ''.join(name)
        link = html.xpath('//*[@id="searchlist"]/table/tbody/tr/td[2]/a/@href')
        print(name, link)

        return zip(name, link)

    def parse_two_page(self, url):
        text = requests.get(url=url, headers=self.get_headers2()).text
        # print(text)
        html = etree.HTML(text)
        message = html.xpath('//*[@id="company-top"]/div[2]/div[2]/div[3]//text()')
        print(message)
        message = list(map(lambda item: re.sub('\s+', '', item), message))
        print(message)
        message = list(filter(None, message))
        print(message)
        message.remove('附近企业')
        message.remove('编辑企业信息')
        print(message)
        # return message
        table1 = html.xpath('//*[@id="Cominfo"]/table//text()')
        # print(table1)
        table1 = list(map(lambda item: re.sub('\s+', '', item), table1))
        # print(table1)
        table1 = list(filter(None, table1))
        print(table1)

    def run(self):
        links = self.parse_index_page()
        for link in links:
            url = 'https://www.qichacha.com' + link[1]
            self.parse_two_page(url)
            time.sleep(random.uniform(2, 4))


if __name__ == '__main__':
    spider = QichachaSpider()
    spider.run()
