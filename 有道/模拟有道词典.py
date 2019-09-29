#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午1:21 
# @Author : Lattesea 
# @File : 模拟有道词典.py 
import time
import requests
import re
import random
from hashlib import md5
import json


class YdSpider(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

        self.headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9",
                        "Connection": "keep-alive",
                        "Content-Length": "251",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Cookie": "OUTFOX_SEARCH_USER_ID=1685565644@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1063294248.3998312; _ntes_nnid=ab5591368febf89a099e9d0635ffd823,1559559603665; JSESSIONID=aaaXPocCxqKtac2Nu2J0w; ___rl__test__cookies=1568264661768",
                        "Host": "fanyi.youdao.com",
                        "Origin": "http://fanyi.youdao.com",
                        "Referer": "http://fanyi.youdao.com/",
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
                        "X-Requested-With": "XMLHttpRequest"}

    def get_ts_salt_sign(self, word):
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    def attack_yd(self, word):
        ts, salt, sign = self.get_ts_salt_sign(word)

        data = {"i": word,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": salt,
                "sign": sign,
                "ts": ts,
                "bv": "e10af5f03f8c56ddb58d31d96e6b4c95",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlME"}
        res = requests.post(self.url, data=data, headers=self.headers)
        html = res.json()
        result = html['translateResult']
        print(res.text)

    def run(self):
        word = input("请输入单词:")
        self.attack_yd(word)


if __name__ == '__main__':
    spider = YdSpider()
    spider.run()
