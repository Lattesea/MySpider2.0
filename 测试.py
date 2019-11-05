#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午2:17 
# @Author : Lattesea 
# @File : 测试.py

import requests
r=requests.get('http://www.baidu.com')
print(r.status_code)
