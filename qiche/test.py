#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-10-27 19:12
# @Author: Lattesea
# @File: test.py
# import execjs
#
# js = '''
# function add(a,b){return a + b}
#
# '''
# ctx = execjs.compile(js)
# dic = ctx.call('add', 1, 2)
# print(dic)
# import re

string = '45dsjaio846ajdsio13'
# result = len(re.findall('[0-9]', str01))
# print(result)
number = 0
for i in string:
    try:
        int(i)
        number += 1
    except:
        continue
print(number)
