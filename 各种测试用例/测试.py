#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午2:17 
# @Author : Lattesea 
# @File : 测试.py
import uiautomator2 as u2
from time import sleep

d = u2.connect('127.0.0.1')
# print(d.info)
# d.click(0.306, 0.597)
# sleep(10)
d(resourceId="com.ss.android.ugc.aweme:id/ao0").click()
d.send_keys("女仆", clear=True)
sleep(2)
d.click(0.462, 0.211)
sleep(2)
d(scrollable=True).scroll.toEnd(60)