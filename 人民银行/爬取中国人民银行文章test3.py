#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-12 0:43
# @Author: Lattesea
# @File: 爬取中国人民银行文章test3.py
import requests
import re
import execjs
from fake_useragent import UserAgent
from lxml import etree


# js = '''
# var jsdom = require("C:\/Program Files\/nodejs\/node_modules\jsdom");
# var {
# 	JSDOM
# } = jsdom;
# var dom = new JSDOM();
#
# window = dom.window;
# document = window.document;
# window.decodeURIComponent = decodeURIComponent;

class Zhongguospider(object):
    def __init__(self):
        self.url = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/index.html'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def parse(self):
        response = requests.session().get(url=self.url, headers=self.get_headers()).text
        js=re.findall('<script type="text/javascript"(.*?)/script>',response,re.S)
        print(js)

    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = Zhongguospider()
    spider.run()
