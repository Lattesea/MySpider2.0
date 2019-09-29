#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-10 下午7:45 
# @Author : Lattesea 
# @File : 爬取当当百名榜书籍信息.py
"""
    使用selenium爬取当当网百名榜书籍信息
"""
from selenium import webdriver
import time
from lxml import etree
import csv

browser = webdriver.Chrome()
browser.get("http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1")
# browser.get_cookies()
time.sleep(1)
button_login1 = browser.find_element_by_xpath("//span[@id='nickname']/a[@class='login_link']")
button_login1.click()
close_button = browser.find_element_by_id("J_loginMaskClose")
close_button.click()
input_phone_number = browser.find_element_by_id("txtUsername")
input_phone_number.send_keys('18998261232')
time.sleep(0.2)
input_password = browser.find_element_by_id("txtPassword")
input_password.send_keys('hgx809695135')
time.sleep(10)
button_login2 = browser.find_element_by_id("submitLoginBtn")
button_login2.click()
# button_book = browser.find_element_by_name("nav1")
# button_book.click()
# button_list = browser.find_element_by_xpath("//div[@class='book_top ']/a[@class='more_top']")
# button_list.click()
for i in range(25):
    time.sleep(5)
    text = browser.page_source
    # print(text)
    html = etree.HTML(text)
    book_name = html.xpath("//div[@class='name']/a/text()")
    price = html.xpath("//span[@class='price_n']/text()")
    original_price = html.xpath("//span[@class='price_r']/text()")
    publisher = html.xpath("//div[@class='publisher_info'][2]/a/text()")
    # auther = html.xpath("//div[@class='publisher_info'][1]/text()")
    time1 = html.xpath("//div[@class='publisher_info'][2]/span/text()")
    result = zip(book_name, publisher, price, original_price, time1)
    with open('book.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(result)
        for i in result:
            print(i)
    next_button = browser.find_element_by_xpath(
        "//div[@class='bang_list_box']/div[@class='paginating']/ul[@class='paging']/li[@class='next']/a")
    next_button.click()
# price = browser.find_elements_by_xpath("//span[@class='price_n']")
# for i in price:
#     print(i.text)
