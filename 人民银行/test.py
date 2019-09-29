#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-20 下午8:15 
# @Author : Lattesea 
# @File : test.py
import execjs

with open('js', 'r') as f:
    js = f.read()

obj = execjs.compile(js)
result = obj.eval('string')
print(result)