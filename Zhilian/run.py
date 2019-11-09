#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-09 17:37
# @Author: Lattesea
# @File: run.py
from scrapy import cmdline

cmdline.execute('scrapy crawl zhilian -o zhilian.csv'.split())
