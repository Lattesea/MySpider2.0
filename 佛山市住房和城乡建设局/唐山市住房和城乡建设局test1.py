#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-8-28 下午5:08 
# @Author : Lattesea 
# @File : 唐山市住房和城乡建设局.py 
"""
爬取唐山市住房和城乡建设局信息
"""
import requests
from requests.exceptions import RequestException
from lxml import etree
import csv


def get_one_index_page(url):
    """
        获取请求页的源码
    :param url:
    :return:
    """
    try:
        headers = {
            'User-Agent': 'Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / '
                          '76.0.3809.100Safari / 537.36',

        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_all_index_urls(text):
    """
        获取首页的所有详情的a链接,返回一个链接列表
    :param text:
    :return:
    """
    html = etree.HTML(text)
    details = html.xpath("//td[5]/a/@href")
    building = html.xpath("//td[6]/a/@href")
    return zip(details, building)


def parse_detail_page(text):
    """
        提取详情页信息
    :param text:
    :return: 售房单位,项目名称,坐落位置,预售证号,发证日期
    """
    html = etree.HTML(text)
    result = []
    housing_units = html.xpath("//tr[1]/td[4]/text()")
    result.append(housing_units[0])
    project_name = html.xpath("//tr[2]/td[2]/text()")
    result.append(project_name[0])
    location = html.xpath("//tr[3]/td[2]/text()")
    result.append(location[0])
    license = html.xpath("//tr[1]/td[2]/text()")
    result.append(license[0])
    date = html.xpath("//tr[4]/td[2]/text()")
    result.append(date[0])
    return result


def parse_building_list(text):
    """
        获取幢号
    :param text:
    :return:幢号列表
    """
    html = etree.HTML(text)
    building_number = html.xpath("//tr[position()>1]/td[1]/text()")
    building_list = html.xpath("//tr[position()>1]/td[7]/a/@href")
    return zip(building_number, building_list)


def parse_building_message(text):
    """
        获取楼房详细信息
    :param text:
    :return: 单元号,房名,建筑面积,套内面积,当前层,状态,是否抵押
    """
    list_result = []
    n = 0
    html = etree.HTML(text)
    message = html.xpath("//tr[position()>1]/td/text()")
    max_message = len(message)
    while n < max_message:
        list_result.append(message[n:n + 7])
        n += 7

    return list_result


# def parse_one_page(text):
#     html = etree.HTML(text)
#     id = html.xpath("//td[1]/text()")
#     unit = html.xpath("//td[2]/text()")
#     project_name = html.xpath("//td[3]/text()")
#     address = html.xpath("//td[4]/text()")
#     result = zip(id, unit[1::], project_name, address)
#     return result


def save_to_csv(result, filename):
    with open('%s' % filename, 'a') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(result)
        # for i in result:
        #     print(i)
        #     writer.writerow(i)


def get_index_url(n):
    """
        翻页
    :param n:
    :return:
    """
    return 'http://tp.tangshan.gov.cn:8090/wsyscx.jspx?pageindex=%d&type=1&typeval=' % n


def main1():
    n = 0
    for i in range(1, 33):
        buildingmessage2 = []
        buildingmessage3 = []
        url_index = get_index_url(i)  # 构建主页的链接
        text_index = get_one_index_page(url_index)  # 获取主页的源码
        url_details = parse_all_index_urls(text_index)  # 从主页源码中提取所有的a连接
        for i in url_details:  # 循环读取a连接访问详情页
            text_detail = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[0])  # 获取详情页的a链接,访问详情页获得源码
            # print(text_detail)
            buildingmessage1 = parse_detail_page(text_detail)  # 提取详情页的信息
            # print(type(buildingmessage1))
            text_building_list = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 访问楼盘信息页获得源码
            building_list = parse_building_list(text_building_list)  # 提取幢号和a链接

            # time.sleep(0.1)
            for i in building_list:
                buildingmessage2.append(i[0])  # 提取幢号
                text_message = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 获取幢号详情的源代码
                text_messages = parse_building_message(text_message)  # 提取幢号详情中所需要的信息
                # print(text_messages)
                # time.sleep(0.1)
                for i in text_messages:
                    for j in i:
                        buildingmessage3.append(j)
                    # print(buildingmessage1)
                    # print(buildingmessage2)
                    # print(buildingmessage3)
                    result = buildingmessage1 + buildingmessage2 + buildingmessage3
                    print(result)
                    n += 1
                    print("data1文件收集%d条" % n)
                    save_to_csv(result, filename='data1.csv')
                    buildingmessage3.clear()
                buildingmessage2.clear()


def main2():
    n = 0
    for i in range(33, 65):
        buildingmessage2 = []
        buildingmessage3 = []
        url_index = get_index_url(i)  # 构建主页的链接
        text_index = get_one_index_page(url_index)  # 获取主页的源码
        url_details = parse_all_index_urls(text_index)  # 从主页源码中提取所有的a连接
        for i in url_details:  # 循环读取a连接访问详情页
            text_detail = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[0])  # 获取详情页的a链接,访问详情页获得源码
            # print(text_detail)
            buildingmessage1 = parse_detail_page(text_detail)  # 提取详情页的信息
            # print(type(buildingmessage1))
            text_building_list = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 访问楼盘信息页获得源码
            building_list = parse_building_list(text_building_list)  # 提取幢号和a链接

            # time.sleep(0.1)
            for i in building_list:
                buildingmessage2.append(i[0])  # 提取幢号
                text_message = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 获取幢号详情的源代码
                text_messages = parse_building_message(text_message)  # 提取幢号详情中所需要的信息
                # print(text_messages)
                # time.sleep(0.1)
                for i in text_messages:
                    for j in i:
                        buildingmessage3.append(j)
                    # print(buildingmessage1)
                    # print(buildingmessage2)
                    # print(buildingmessage3)
                    result = buildingmessage1 + buildingmessage2 + buildingmessage3
                    print(result)
                    n += 1
                    print("data2文件收集%d条" % n)
                    save_to_csv(result, filename='data2.csv')
                    buildingmessage3.clear()
                buildingmessage2.clear()


def main3():
    n = 0
    for i in range(66, 99):
        buildingmessage2 = []
        buildingmessage3 = []
        url_index = get_index_url(i)  # 构建主页的链接
        text_index = get_one_index_page(url_index)  # 获取主页的源码
        url_details = parse_all_index_urls(text_index)  # 从主页源码中提取所有的a连接
        for i in url_details:  # 循环读取a连接访问详情页
            text_detail = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[0])  # 获取详情页的a链接,访问详情页获得源码
            # print(text_detail)
            buildingmessage1 = parse_detail_page(text_detail)  # 提取详情页的信息
            # print(type(buildingmessage1))
            text_building_list = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 访问楼盘信息页获得源码
            building_list = parse_building_list(text_building_list)  # 提取幢号和a链接

            # time.sleep(0.1)
            for i in building_list:
                buildingmessage2.append(i[0])  # 提取幢号
                text_message = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 获取幢号详情的源代码
                text_messages = parse_building_message(text_message)  # 提取幢号详情中所需要的信息
                # print(text_messages)
                # time.sleep(0.1)
                for i in text_messages:
                    for j in i:
                        buildingmessage3.append(j)
                    # print(buildingmessage1)
                    # print(buildingmessage2)
                    # print(buildingmessage3)
                    result = buildingmessage1 + buildingmessage2 + buildingmessage3
                    print(result)
                    n += 1
                    print("data3文件收集%d条" % n)
                    save_to_csv(result, filename='data3.csv')
                    buildingmessage3.clear()
                buildingmessage2.clear()


def main4():
    n = 0
    for i in range(99, 129):
        buildingmessage2 = []
        buildingmessage3 = []
        url_index = get_index_url(i)  # 构建主页的链接
        text_index = get_one_index_page(url_index)  # 获取主页的源码
        url_details = parse_all_index_urls(text_index)  # 从主页源码中提取所有的a连接
        for i in url_details:  # 循环读取a连接访问详情页
            text_detail = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[0])  # 获取详情页的a链接,访问详情页获得源码
            # print(text_detail)
            buildingmessage1 = parse_detail_page(text_detail)  # 提取详情页的信息
            # print(type(buildingmessage1))
            text_building_list = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 访问楼盘信息页获得源码
            building_list = parse_building_list(text_building_list)  # 提取幢号和a链接

            # time.sleep(0.1)
            for i in building_list:
                buildingmessage2.append(i[0])  # 提取幢号
                text_message = get_one_index_page('http://tp.tangshan.gov.cn:8090/' + i[1])  # 获取幢号详情的源代码
                text_messages = parse_building_message(text_message)  # 提取幢号详情中所需要的信息
                # print(text_messages)
                # time.sleep(0.1)
                for i in text_messages:
                    for j in i:
                        buildingmessage3.append(j)
                    # print(buildingmessage1)
                    # print(buildingmessage2)
                    # print(buildingmessage3)
                    result = buildingmessage1 + buildingmessage2 + buildingmessage3
                    print(result)
                    n += 1
                    print("data4文件收集%d条" % n)
                    save_to_csv(result, filename='data4.csv')
                    buildingmessage3.clear()
                buildingmessage2.clear()


# def main():
#     for i in range(4):
#         time.sleep(3)
#         main1()
#         main2()
#         main3()
#         main4()


if __name__ == '__main__':
    from multiprocessing import Process

    p_list = [main1, main2, main3, main4]
    for i in range(4):
        p = Process(target=p_list[i])
        p.start()

    # url = 'http://tp.tangshan.gov.cn:8090/wsyscx.jspx?pageindex=1&type=1&typeval='
    # # for i in range(1, 129):
    # #     url = get_all_pages(i)
    # #     text = get_one_index_page(url)
    # #     result = parse_one_page(text)
    # #     save_to_csv(result)
    # url = 'http://tp.tangshan.gov.cn:8090/wsyscxinfo.jspx?pid=3949'
    # # url='http://tp.tangshan.gov.cn:8090/wsysbudinglist.jspx?permitid=3911'
    # url = 'http://tp.tangshan.gov.cn:8090/wsysbudinghouse.jspx?item_code=00001494&build_code=0005'
    # text = get_one_index_page(url)
    # result = parse_building_message(text)
    # print(result)
    # main()
    # for i in range(1, 2):
    #     url_index = get_index_url(i)
    #     print(url_index)
    #     text_index = get_one_index_page(url_index)
    #     print(text_index)
    #     url_details = parse_detail_page(text_index)
    #     print(url_details)
    # result = parse_all_index_urls(text)
    # for i in result:
    #     print(i[0])
    # url = 'http://tp.tangshan.gov.cn:8090/wsysbudinghouse.jspx?item_code=00001378&build_code=0029'
    # text = get_one_index_page(url)
    # result = parse_building_message(text)
    # print(result)
