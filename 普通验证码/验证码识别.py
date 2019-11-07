#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-06 17:09
# @Author: Lattesea
# @File: 验证码识别.py
import requests
from fake_useragent import UserAgent
import json
import base64
import urllib.request, urllib.parse


class BaiduSpider(object):
    def __init__(self):
        self.url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        self.key = 'EYb372x8lvKK9c5dBUXhwzFV'
        self.secret = 'M9X5TSh3lBvsXphfOaEdqYqnToB1VoAo'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def get_accesstoken(self):
        res = requests.post(self.url.format(self.key, self.secret), headers=self.get_headers())
        content = res.text
        if (content):
            return json.loads(content)["access_token"]
