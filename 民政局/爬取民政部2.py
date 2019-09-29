#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-18 上午10:10 
# @Author : Lattesea 
# @File : 爬取民政部2.py 
from selenium import webdriver
import pymysql


class MinzhengjuSpider(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.browser = webdriver.Chrome(options=options)
        self.db = pymysql.connect('localhost',
                                  'root',
                                  '123456',
                                  'govdb',
                                  charset='utf8'
                                  )
        self.cursor = self.db.cursor()
        self.province_list = []
        self.city_list = []
        self.country_list = []

    def get_code(self):
        all_handlers = self.browser.window_handles
        self.browser.switch_to_window(all_handlers[1])
        tr_list = self.browser.find_element_by_xpath("tr[@height='19']")
        for tr in tr_list:
            code = tr.find_element_by_xpath('./td[2]').text.strip()
            name = tr.find_element_by_xpath('./td[3]').text.strip()
            print(name, code)

    def get_page(self):
        # browser = webdriver.Chrome()
        self.browser.get(self.url)
        td = self.browser.find_element_by_xpath(
            '//td[@class="arlisttd"]/a[contains(@title,"代码")]'
        )
        two_url = td.get_attribute('href')
        if result:
            print("无需爬取")
        else:
            td.click()
            self.get_code()
            dele = 'delete from version'
            ins = 'insert into version values(%s)'
            self.cursor.execute(dele)
            self.cursor.execute(ins, [two_url])
            self.db.commit()

    def run(self):
        self.get_page()


if __name__ == '__main__':
    spider = MinzhengjuSpider()
    spider.run()
