#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-3 下午2:45 
# @Author : Lattesea 
# @File : test2.py
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.ratingdog.cn/#/rating/rating?index=2')
# browser.get_cookies()
time.sleep(1)
button = browser.find_element_by_xpath("//div[@class='tc el-col el-col-8']")
button.click()
button_login = browser.find_element_by_xpath("//div[@class='el-col el-col-4 el-col-offset-2'][1]")
button_login.click()
input_phone_number = browser.find_element_by_xpath("//input[@placeholder='手机号码']")
input_phone_number.send_keys('18998261232')
input_password = browser.find_element_by_xpath("//input[@type='password']")
input_password.send_keys('tcpcl4bq')
button_login2 = browser.find_element_by_xpath("//div[@class='el-col el-col-12'][1]")
button_login2.click()
button_option1 = browser.find_element_by_xpath("//div[@class='highlight']/a/@href")
button_option1.click()

