#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-21 下午3:04 
# @Author : Lattesea 
# @File : 爬取大众点评评论.py 
import requests
import re
from fake_useragent import UserAgent
from lxml import etree
import time
import json


class DazhongSpider(object):
    def __init__(self):
        self.url = 'https://m.dianping.com/shop/66250176/review_all?source=pc_jump'
        self.svg_url = 'https://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/bcf0ab33f6b1258eb8d3a297e33f26a1.css'
        self.json_url = 'https://m.dianping.com/isoapi/module'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "_lxsdk_cuid=16b6d90060dc8-0c483b10b50692-15231708-1fa400-16b6d90060dc8; _lxsdk=16b6d90060dc8-0c483b10b50692-15231708-1fa400-16b6d90060dc8; _hc.v=eeb15112-318a-a2dc-33c8-2679134462ee.1560911284; s_ViewType=10; cy=4; cye=guangzhou; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; dper=9d7cb8868867648f5d1932800f94703b2f2bb536767d1c0cb0fa14d864389647bbca602bf75fd65691c4af3aa632a9b26cab4f8117026d68523ebfb68e5039ded5a373453a22982a9a7d8222f27124d79b7c6a0692b32977c1af77bc01f6f43b; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3896667530; ctu=51ed98c68ae176af9e3e6a65b79a06e90fef4061fcf29e09c4f4594c3fae69e8; uamo=18998261232; _lxsdk_s=16ded9db300-c00-2bc-cbb%7C%7C1",
            "Host": "m.dianping.com",
            "Referer": "https://www.dianping.com/shop/66250176/review_all",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-site",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
        }
        return headers

    def parse(self):
        params = {"moduleInfoList": [{"moduleName": "reviewlist",
                                      "query": {"shopId": "66250176", "offset": 10, "limit": 10, "type": 1,
                                                "pageDomain": "m.dianping.com"}}], "pageEnName": "shopreviewlist"}
        html_json = requests.post(url=self.url, headers=self.get_headers(), params=params).text
        # print(html_json)
        # html_py = json.loads(html_json)
        # print(html_py)
        # for i in html_py['data']['moduleInfoList']:
        #     print(i)
        html = etree.HTML(html_json)
        # print(html_py)
        name = html.xpath(
            "//a[@class='comment-item'][1]/div[@class='comment-detail']/div[@class='comment']/div[@class='userNameLine']/div[@class='left-part']/div[@class='username']/text()")
        message = html.xpath(
            "//a[@class='comment-item'][1]/div[@class='comment-detail']/div[@class='comment']/div[@class='comment-entry not-spread']/text()")
        date = html.xpath(
            "//a[@class='comment-item'][1]/div[@class='comment-detail']/div[@class='comment']/div[@class='userNameLine']/div[@class='addTime']/text()")
        price = html.xpath(
            "//a[@class='comment-item'][1]/div[@class='comment-detail']/div[@class='comment']/div[@class='starLine']/span[@class='avg-price']/text()")
        read = html.xpath(
            "//a[@class='comment-item'][1]/div[@class='comment-detail']/div[@class='info']/span[1]/text()")
        star = html.xpath(
            "//a[@class='comment-item'][1]/div[@class='comment-detail']/div[@class='info']/span[2]/text()")
        # dianping=html.xpath("//div[@class='reviews-items']/ul/li[2]/div[@class='main-review']/div[
        # @class='review-truncated-words']/text()")
        print(name)
        print(message)
        print(date)
        print(price)
        print(read)
        print(star)
        # print(message)

    def svg(self):
        text = requests.get(url=self.svg_url, headers=self.get_headers()).text
        # print(text)
        html = etree.HTML(text)
        address = html.xpath("//html/body/pre/text()")
        print(address)

    def run(self):
        self.parse()
        # self.svg()


if __name__ == '__main__':
    spider = DazhongSpider()
    spider.run()
