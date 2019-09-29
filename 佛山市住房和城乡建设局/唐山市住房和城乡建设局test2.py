#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-8-28 下午8:18 
# @Author : Lattesea 
# @File : 唐山市住房和城乡建设.py 
from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser.get('http://tp.tangshan.gov.cn:8090/wsyscx.jspx?pageindex=2&type=1&typeval=')
    td = browser.find_elements_by_tag_name('td')
    print()


except Exception as err:
    print(err)
browser.close()