#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-08 23:41
# @Author: Lattesea
# @File: run.py
from scrapy import cmdline

cmdline.execute('scrapy crawl tianqi -o tianqi.csv'.split())
