#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-07 17:59
# @Author: Lattesea
# @File: 爬取网易buff平台饰品市场.py
import requests
from fake_useragent import UserAgent
import json
import csv
import time


class BuffSpider(object):
    def __init__(self):
        self.url = 'https://buff.163.com/api/market/goods?game=csgo&page_num={}&_=1573121034530'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "nts_mail_user=18998261232@163.com:-1:1; mail_psc_fingerprint=dfc2187400fc0f4331d96a087e1ad5bb; _ntes_nnid=da2079b0513cd7c1fcefa4d65cfb098a,1568818466755; _ntes_nuid=da2079b0513cd7c1fcefa4d65cfb098a; Device-Id=cUhnNyNGkuWzSfAaO84U; csrf_token=3114229e66bb2d698590db5f1adfdc3294cc8d28; game=csgo; _ga=GA1.2.1043927110.1573120436; _gid=GA1.2.837896144.1573120436; NTES_YD_SESS=t3m0VRziMdtogEmsA7eyAGsmFIZccoy_F5R1p9JEpcN8uWdmu57zsx5tRUB9E2B6WGr6rERTPkJ11jCqZv1lAj3ebUfuEy5F4bMLGAs5gz6LOYBMI3CNkVPxLlxSEtYp7F8ttoJJLrE7xt1G5ie4bX1yqs2YjdN1k7Nz9Vq0eVU7M2VWc8GrHkmEaeCc...gTvbRyqLCyP0k8Ki0p_tLbh64lCzvZ.65SV1LDwyp3VH0b; S_INFO=1573121009|0|3&80##|18998261232; P_INFO=18998261232|1573121009|0|netease_buff|00&99|null&null&null#gud&440100#10#0#0|&0||18998261232; session=1-TwHM0kcWI0z6KwKpvEepCY0dysZSoMhEvYPBmGBfmRZO2043572780; Locale-Supported=zh-Hans; _gat_gtag_UA_109989484_1=1",
            "Host": "buff.163.com",
            "Referer": "https://buff.163.com/market/?game=csgo",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": ua.random,
            "X-Requested-With": "XMLHttpRequest"
        }
        return headers

    def parse(self, number):
        response = requests.get(url=self.url.format(number), headers=self.get_headers()).text
        html = json.loads(response)
        list_result = []
        for i in html['data']['items']:
            dict_result = {}
            dict_result['name'] = i['name']
            dict_result['quick_price'] = i['quick_price']
            dict_result['sell_num'] = i['sell_num']
            list_result.append(dict_result)
        print(list_result)
        return list_result

    def save(self, result, page):
        keyword_list = ['name', 'quick_price', 'sell_num']
        for i in result:
            with open('result.csv', 'a', newline='', encoding='GB18030') as f:
                # 注意编码的问题
                writer = csv.DictWriter(f, keyword_list)
                writer.writerow(i)
        print("%s页写入成功" % page)

    def run(self):
        try:
            for page in range(1, 656):
                result = self.parse(page)
                self.save(result, page)
                time.sleep(0.5)
        except Exception as err:
            print(err)
        # for page in range(1, 656):
        #     result = self.parse(page)
        #     self.save(result, page)
        #     time.sleep(0.5)


if __name__ == '__main__':
    spider = BuffSpider()
    spider.run()
