#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import etree
import csv,re,random,time
import json
from selenium import webdriver
from time import sleep

#引入了队列
from multiprocessing import Queue
#ThreadPoolExecutor包引入线程池
from concurrent.futures import ThreadPoolExecutor

# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#解决编译出现的问题



#post请求
def get_headers(url):

    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    ]

    cookies = [
        "_ga=GA1.2.1094979457.1568989202; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2287a6e9e6b7da038ac749582d31b5c46b%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A12%3A%22172.31.23.86%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A114%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F77.0.3865.90+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1568989260%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A13%3A%22premiumHideAd%22%3Bb%3A1%3B%7D93c9b7457c5ab7a98b5d7ab9ff97dcad; _gid=GA1.2.1283642204.1569078022; sc_is_visitor_unique=rx11875557.1569146713.DB52CE9EBD704F646BE961A47F9E64FB.4.4.3.3.3.3.2.1.1; _gat=1",
    ]
    headers = {
        "Accept":'*/*',
        "Cache-Control":'max-age=0',
        "Accept-Encoding":'gzip, deflate',
        "Accept-Language":'zh-CN,zh;q=0.9',
        "Connection":'keep-alive',
        "Upgrade-Insecure-Requests":'1',
        "Content-Length":'22',
        "Host":'www.spotrac.com',
        "Origin":'https://www.spotrac.com',
        "Referer":url,
        "User-Agent": random.choice(agents),
        "Cookie":random.choice(cookies)

    }

    body = {
        "ajax": "true",
        "mobile": 'false'
    }
    try:
        res = requests.post(url, headers=headers,data=body)
        res.encoding = res.apparent_encoding
        print(res.status_code)
        # html = etree.HTML(res.text)
        return res.text
    except:
        print('打开不了网址...')


#get
def get_headers2(url):

    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    ]

    cookies = [
        "_ga=GA1.2.1094979457.1568989202; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2287a6e9e6b7da038ac749582d31b5c46b%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A12%3A%22172.31.23.86%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A114%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F77.0.3865.90+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1568989260%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A13%3A%22premiumHideAd%22%3Bb%3A1%3B%7D93c9b7457c5ab7a98b5d7ab9ff97dcad; _gid=GA1.2.1283642204.1569078022; sc_is_visitor_unique=rx11875557.1569161515.DB52CE9EBD704F646BE961A47F9E64FB.5.5.4.3.3.3.2.1.1",
        "_ga=GA1.2.1094979457.1568989202; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2287a6e9e6b7da038ac749582d31b5c46b%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A12%3A%22172.31.23.86%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A114%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F77.0.3865.90+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1568989260%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A13%3A%22premiumHideAd%22%3Bb%3A1%3B%7D93c9b7457c5ab7a98b5d7ab9ff97dcad; _gid=GA1.2.1283642204.1569078022; sc_is_visitor_unique=rx11875557.1569148682.DB52CE9EBD704F646BE961A47F9E64FB.4.4.3.3.3.3.2.1.1",
        "_ga=GA1.2.1094979457.1568989202; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2287a6e9e6b7da038ac749582d31b5c46b%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A12%3A%22172.31.23.86%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A114%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F77.0.3865.90+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1568989260%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A13%3A%22premiumHideAd%22%3Bb%3A1%3B%7D93c9b7457c5ab7a98b5d7ab9ff97dcad; _gid=GA1.2.1283642204.1569078022; sc_is_visitor_unique=rx11875557.1569148410.DB52CE9EBD704F646BE961A47F9E64FB.4.4.3.3.3.3.2.1.1",
    ]
    headers = {
        "Accept":'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        "Cache-Control":'max-age=0',
        "Accept-Encoding":'gzip, deflate',
        "Accept-Language":'zh-CN,zh;q=0.9',
        "Connection":'keep-alive',
        "Upgrade-Insecure-Requests":'1',
        "sec-fetch-mode":'navigate',
        "sec-fetch-site":'none',
        "sec-fetch-user":'?1',
        "Host":'www.spotrac.com',
        "Referer":'https://sou.zhaopin.com/?jl=639&kw=%E8%B4%A8%E9%87%8F&kt=3',
        "User-Agent": random.choice(agents),
        "Cookie":random.choice(cookies)

    }

    # time.sleep(random.random())
    try:
        res = requests.get(url, headers=headers)
        res.encoding = res.apparent_encoding

        print(res.status_code)
        # html = etree.HTML(res.text)
        return res.text
    except:
        print('打开不了网址...')



#表格1的
def save_url1(data2):
    print('正在将产品地址数据存进文件...')
    with open("表1.csv", "a",newline='',encoding="utf-8") as f:
        fieldnames= ['name','','product_url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data2)
        print("OK")

#获得所有得Url
def all_url(url):
    # page = all_page(url)
    for i2 in range(1,2):
        data2 = {
            "url":url,
            "num":str(i2),
        }
        get_data2(data2)
        # queue_list.put(data2)

def get_data2(data2):
    url2 = data2["url"]
    i = data2['num']
    print('正在爬取第%s页的数据' % i, url2)
    try:
        res = get_headers(url2)
        # print(res)
        html = etree.HTML(res)
        # print(html)
        results = html.xpath('//td[@class="rank-name player noborderright"]/h3[1]')
        print(len(results))
        for result in results:
            url = result.xpath('./a[1]/@href')[0]
            name = result.xpath('normalize-space(./a[1]/text())')
            data3 = {
                "url":url,
                "name":name
            }
            print(data3)
            # get_data1(data3)
            queue_list.put(data3)#想线程，就开这个，不想就注释掉

    except:
        pass
#获取运动员的基本信息
def get_data1(data):
    keys = ["name","view","age","exp","Drafted","Country","Agent(s)"]
    values = [data["name"]]
    name = data["name"]
    url = data["url"]
    html = etree.HTML(get_headers2(url))
    get_data3(html,name)#第二张表格和第三张表格
    try:
        for i in range(1,4):
            v1 = ''.join(html.xpath('//div[@class="player-details"]/div[1]/div[1]/span[{}]/text()'.format(i))).strip()
            values.append(v1)
        for j in range(1,4):
            v2 = ''.join(html.xpath('//div[@class="player-details"]/div[1]/div[2]/span[{}]/text()'.format(j))).strip()
            values.append(v2)
    except:
        pass
    finally:
        data1 = dict(zip(keys,values))
        data11={
            "keys":keys,
            "values":data1
        }
        print(data1)
        save_field1(data11)#第一个表格信息

#表三的信息
def get_data3(html,name):

    # print(values)


    tables3 = html.xpath('//ul[@class="cd-tabs-content"]/li[1]/table[3]//table[@class="salaryTable current"][1]/tbody//tr')
    num = len(tables3)
    tables2 = tables3[0:num-2]
    j=1
    print(tables2)
    for table2 in tables2:
        keys = ["名字", "个人简介", "合同", "签约奖金", "平均工资", "自由球员"]
        values = [name]
        he_content = ''.join(html.xpath('//ul[@class="cd-tabs-content"]/li[1]/p[1]/text()')).strip()
        values.append(he_content)
        table1 = html.xpath('//ul[@class="cd-tabs-content"]/li[1]/table[1]//td/span[2]/text()')
        values += table1

        for i in range(1,11):
            keys.append(i)
            v = ''.join(table2.xpath('./td[{}]//text()'.format(i))).strip()
            values.append(v)
        j2 = 1
        for table3 in tables3:
            if j2 == num - 1:
                hetong = ''.join(table3.xpath('./td//text()')).strip()
                # print(hetong2)
                # print('+++++++')
                keys.append("9")
                values.append(hetong)
            j2 += 1

        hetong_laiyuan = ''.join(html.xpath('//div[@class="site-source"]//text()')).strip()
        keys.append("10")
        values.append(hetong_laiyuan)

        # print(values)
        data = dict(zip(keys,values))
        print(data)
        data2 = {
            "keys":keys,
            "values":data
        }

        save_field2(data2)

    # hetong_laiyuan2 = ''.join(html.xpath('//ul[@class="cd-tabs-content"]/li[1]/table[@class="salaryTable salaryInfo hidden-xs"][2]//td/span[2]/text()')).strip()
    # print(hetong_laiyuan2)

    tables5 =  html.xpath('//ul[@class="cd-tabs-content"]/li[1]/table[@class="playerTable rtable"][2]//table[@class="salaryTable current"]/tbody//tr')
    # print(tables5)
    num2 = len(tables5)
    tables4 = tables5[0:num2 - 2]
    # print(tables4)
    for table4 in tables4:
        keys2 = ["名字", "合同时间", "合同", "签约奖金", "平均工资", "自由球员"]
        values2 = [name]
        he_time = ''.join(html.xpath('//span[@class="contract-type-years"]/text()')).strip()
        # print(he_time)
        values2.append(he_time)


        table7 = html.xpath('//ul[@class="cd-tabs-content"]/li[1]/table[@class="salaryTable salaryInfo hidden-xs"][2]//td/span[2]/text()')
        values2 += table7

        for i2 in range(1,8):
            keys2.append(i2)
            v2 = ''.join(table4.xpath('./td[{}]//text()'.format(i2))).strip()
            values2.append(v2)

        j=1
        for table5 in tables5:
            if j==num2-1:
                hetong2 = ''.join(table5.xpath('./td//text()')).strip()
                # print(hetong2)
                # print('+++++++')
                keys2.append("9")
                values2.append(hetong2)
            if j == num2:
                hetong_laiyuan2 = ''.join(html.xpath('//td[@class="premiumstop"]/p/text()')).strip()
                keys2.append(hetong_laiyuan2)
                values2.append(hetong_laiyuan2)
            j+=1

        # print(values2)
        data3 = dict(zip(keys2, values2))
        print(data3)
        data4 = {
            "keys": keys2,
            "values": data3
        }
        # print('------------------------------------')
        # print(data3)
        save_field4(data4)


# 存储信息
def save_field4(data4):
    # 存储数据
    print('正在将数据存进文件...')
    with open("2019运动员的第三张表格的信息.csv", "a", newline='', encoding="utf-8") as f:
        fieldnames = data4["keys"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data4["values"])
        print("OK...")

def save_field1(data1):
    print('正在将数据存进文件...')
    with open("2019运动员的第一张表格信息.csv", "a", newline='', encoding="utf-8") as f:
        fieldnames = data1['keys']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data1["values"])
        print("OK...")

#存储信息
def save_field2(data2):
    # 存储数据
    print('正在将数据存进文件...')
    with open("2019运动员的第二张表格的基本信息.csv", "a",newline='',encoding="utf-8") as f:
        fieldnames = data2['keys']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data2["values"])
        print("OK...")

# 存储信息3
def save_field3(data3):
    # 存储数据
    print('正在将数据存进文件...')
    with open("运动员的url.csv", "a", newline='', encoding="utf-8") as f:
        fieldnames = ["url","name"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data3["values"])
        print("OK...")
    # broswer.quit()
if __name__ == '__main__':
    # 创建队列
    queue_list = Queue()
    # get_area()
    # get_headers(url)
    url = 'https://www.spotrac.com/mlb/rankings/2019/contract-value/'
    # all_page(url)
    all_url(url)
    ##实现多线程抓取，引入了线程池
    pool = ThreadPoolExecutor(max_workers=3)
    while queue_list.qsize() > 0:
        pool.submit(get_data1, queue_list.get())
2