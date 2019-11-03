#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午2:17 
# @Author : Lattesea 
# @File : 测试.py

# list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in list01:
#     print(i)
str_example = input("请输入字符串")
result = 0
for i in str_example:
    try:
        int(i)
        result += int(i)
    except:
        continue
print(result)
# import re
#
# str_example = input("请输入字符串")
# number = re.findall('[0-9]', str_example)
# result = 0
# for i in number:
#     result += int(i)
# print(result)
