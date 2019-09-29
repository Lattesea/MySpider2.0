# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import YoudaoItem
import time
import random
from hashlib import md5

class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    word = input('请输入要翻译的单词:')

    def start_requests(self):
        post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        ts,salt,sign = self.get_salt_sign_ts(self.word)
        formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "a4f4c82afd8bdba188e568d101be3f53",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        # post请求: scrapy.FormRequest()
        # get请求:  scrapy.Request()
        yield scrapy.FormRequest(
            url=post_url,
            formdata=formdata,
            callback=self.parse
        )


    def get_salt_sign_ts(self,word):
        # ts
        ts = str(int(time.time()*1000))
        # salt
        salt = ts + str(random.randint(0,9))
        # sign
        string = "fanyideskweb" + word + salt + \
                              "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts,salt,sign

    def parse(self, response):
        print(response.text)
        item = YoudaoItem()
        html = json.loads(response.text)
        item['result'] = html['translateResult'][0][0]['tgt']

        yield item














