#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-24 下午9:23 
# @Author : Lattesea 
# @File : 爬取人民银行文章test2.py 
"""
    使用selenium爬取人民银行文章
"""
from selenium import webdriver
import time
from lxml import etree
import csv


class RenminyinhangSpider(object):
    def __init__(self):
        # self.url = 'http://www.pbc.gov.cn'
        self.url = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index{}.html'
        self.browser = webdriver.Chrome(
            executable_path="C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")  # 生成浏览器对象

    def parse_index_page(self, number):
        self.browser.get(self.url.format(number))
        text = self.browser.page_source
        html = etree.HTML(text)
        link = html.xpath("//div[@id='11040']/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/font["
                          "@class='newslist_style']/a/@href")
        title = html.xpath(
            "//div[@id='11040']/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/font[@class='newslist_style']/a/text()")
        time = html.xpath(
            "//div[@id='11040']/div[2]/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/span[@class='hui12']/text()")
        print(title)
        print(time)
        print(link)
        result = zip(title, time, link)
        return result

    def paging(self):
        button_next = self.browser.find_element_by_xpath(
            '//*[@id="11040"]/div[2]/div[2]/table/tbody/tr/td[1]/a[3]')
        button_next.click()

    def save(self, result):
        with open("result.csv", mode='a', newline='',encoding='GB18030')as f:
            writer = csv.writer(f)
            writer.writerows(result)

    def run(self):
        for i in range(1, 256):
            result = self.parse_index_page(i)
            self.save(result)
            self.paging()
            time.sleep(2)


if __name__ == '__main__':
    spider = RenminyinhangSpider()
    spider.run()
