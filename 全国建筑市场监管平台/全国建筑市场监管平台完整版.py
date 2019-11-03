#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-02 14:54
# @Author: Lattesea
# @File: 全国建筑市场监管平台完整版.py
import requests
import execjs
from fake_useragent import UserAgent
import json
import csv
import time


class JianguanSpider(object):
    def __init__(self):
        self.url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/project/list?pg={}&pgsz=15&total=450'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def parse_link(self, number):
        response = requests.get(url=self.url.format(number), headers=self.get_headers()).text
        print(response)
        return response

    def parse_js(self, response):
        js = '''
        function Aes(data) {
            console.info(data)
            var CryptoJS = require('C:\/Program Files\/nodejs\/node_modules\/crypto-js')
            var u = CryptoJS.enc.Utf8.parse('jo8j9wGw%6HbxfFn'),
                d = CryptoJS.enc.Utf8.parse('0123456789ABCDEF');
            e = CryptoJS.enc.Hex.parse(data);
            n = CryptoJS.enc.Base64.stringify(e);
            return CryptoJS.AES.decrypt(n, u, {
                iv: d,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            }).toString(CryptoJS.enc.Utf8)

        }

        '''
        ctx = execjs.compile(js)
        dic = ctx.call('Aes', response)
        # print(dic)
        result = json.loads(dic)
        # print(result)

        result_list = []
        for data in result['data']['list']:
            result_dict = {}
            result_dict['LASTUPDATEDATE'] = data['LASTUPDATEDATE']
            result_dict['PRJNUM'] = data['PRJNUM']
            result_dict['PRJNAME'] = data['PRJNAME']
            result_dict['DATALEVEL'] = data['DATALEVEL']
            result_dict['BUILDCORPNAME'] = data['BUILDCORPNAME']
            result_dict['PROVINCE'] = data['PROVINCE']
            result_dict['ID'] = data['ID']
            result_dict['RN'] = data['RN']
            result_dict['PRJTYPENUM'] = data['PRJTYPENUM']
            result_dict['IS_FAKE'] = data['IS_FAKE']
            result_list.append(result_dict)
        print(result_list)
        return result_list

    def save(self, result, page):
        keyword_list = ['LASTUPDATEDATE', 'PRJNUM', 'PRJNAME', 'DATALEVEL', 'BUILDCORPNAME', 'PROVINCE', 'ID', 'RN',
                        'PRJTYPENUM', 'IS_FAKE']
        with open('result.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, keyword_list)
            for row in result:
                writer.writerow(row)
            print("第%s页保存成功" % page)

    def run(self):
        for i in range(0, 31):
            response = self.parse_link(i)
            result = self.parse_js(response)
            self.save(result, i + 1)
            time.sleep(3)


if __name__ == '__main__':
    spider = JianguanSpider()
    spider.run()
