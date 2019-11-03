#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-10-23 3:34
# @Author: Lattesea
# @File: 大众点评万达版.py
import requests
from fake_useragent import UserAgent
from lxml import etree


class DazhongSpider(object):
    def __init__(self):
        self.url = ''

    def get_headers(self):
        ua = UserAgent()
        headers = {

        }
        return headers

    def parse(self):
        pass
