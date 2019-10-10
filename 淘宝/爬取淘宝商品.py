#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-10 上午10:05 
# @Author : Lattesea 
# @File : 爬取淘宝商品.py 
from selenium import webdriver
import time
from lxml import etree
import re

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
login = browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
login.click()
time.sleep(20)
browser.find_element_by_id('q').send_keys("胸罩")
browser.find_element_by_class_name('btn-search').click()
time.sleep(10)
text = browser.page_source
html = etree.HTML(text)
name = html.xpath("//div[@class='row row-2 title']/a/text()")
name = list(map(lambda item: re.sub('\s+', '', item), name))
name = list(filter(None, name))
price = html.xpath("//div[@class='price g_price g_price-highlight']/strong/text()")
price = list(map(lambda item: re.sub('\s+', '', item), price))
price = list(filter(None, price))
count = html.xpath("//div[@class='row row-1 g-clearfix']/div[@class='deal-cnt']/text()")
count = list(map(lambda item: re.sub('\s+', '', item), count))
count = list(filter(None, count))
shop = html.xpath("//div[@class='shop']/a[@class='shopname J_MouseEneterLeave J_ShopInfo']/span[2]/text()")
shop = list(map(lambda item: re.sub('\s+', '', item), shop))
shop = list(filter(None, shop))
result = zip(name, price, count, shop)
for i in result:
    print(i)
