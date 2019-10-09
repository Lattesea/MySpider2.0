#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-9 下午7:39 
# @Author : Lattesea 
# @File : 爬取河北新闻网投诉信息.py 
import requests
import random
from fake_useragent import UserAgent
from lxml import etree

class HebeitousuSpider(object):
    def __init__(self):
        self.url='http://yglz.tousu.hebnews.cn/l-1001-5-'

    def get_headers(self):
        ua=UserAgent()
        headers={

        }