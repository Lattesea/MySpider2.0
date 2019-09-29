#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-3 上午9:35 
# @Author : Lattesea 
# @File : 爬取office模板.py 
"""

"""
import requests
from requests.exceptions import RequestException
from lxml import etree
import os
import time


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
            'Accept-Language': 'zh-CN,zh;q = 0.9'

        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_index_urls(text):
    """
        获取首页所有的a链接
    :param text:
    :return:
    """
    html = etree.HTML(text)
    index_url = html.xpath("//a[@class='odcom-template-category-link']/@href")
    return index_url


def parse_type_page_urls(text):
    """
        解析网页获取所有类别的链接
    :param text:
    :return:
    """
    # re.findall(r'')
    html = etree.HTML(text)
    type_page_urls = html.xpath('//a[@class="odcom-template-item-anchor"]/@href')
    # time.sleep(3)
    # type_page_urls = html.xpath('//a')
    return type_page_urls


def change_type_page(number, type_page_url):
    """
        实现每个类型页中的翻页
    :param number:
    :param type_page_url:
    :return:
    """
    base_url = 'https://templates.office.com'
    url = base_url + type_page_url + 'page=%s' % number
    return url


def count_page_number(text):
    """
        计算每一个类型的页数
    :param text:
    :return:
    """
    html = etree.HTML(text)
    page_number = html.xpath("//ul[@class='m-pagination']/li[last()-1]/a/text()")
    return page_number


def get_download_url(text):
    """
        获取下载页的下载链接
    :param text:
    :return:
    """
    html = etree.HTML(text)
    download_url = html.xpath(
        "//a[@class='c-button odcom-template-details-action-button "
        "odcom-template-details-action-button-primary']/@href")
    filename = html.xpath("//a[@data-bi-slot='2']/text()")
    template_name = html.xpath("//h1[@id='tempTitle']/text()")
    filetype = html.xpath("//p[@class='odcom-core-app-label']/text()")
    return zip(download_url, filename, template_name, filetype)


def judge_filetype(filename, filetype):
    """
        判断文件类型
    :param filename:
    :param filetype:
    :return:
    """
    if filetype == 'Excel':
        return filename + '.xlsx'
    elif filetype == 'Word':
        return filename + '.docx'
    elif filetype == 'PowerPoint':
        return filename + '.potx'


def save_template(download_url, filename, template_name, filetype):
    """
        下载模板
    :param download_url:
    :param filename:
    :param template_name:
    :param filetype:
    :return:
    """
    # if not os.path.exists(filename):
    #     os.mkdir(filename)
    try:
        response = requests.get(download_url)
        if response.status_code == 200:
            if not os.path.exists(template_name):
                template_name = judge_filetype(template_name, filetype)
                with open(template_name, 'wb') as f:
                    f.write(response.content)
                    print("完成")
        else:
            print('%s下载完成', template_name)
    except requests.ConnectionError:
        print('%s下载失败' % template_name)
        # return zip(filename, template_name)


def main(start, end):
    index_url = 'https://templates.office.com'
    text_index = get_one_index_page(index_url)  # 获取主页页面
    type_urls = parse_index_urls(text_index)  # 获取主页所有的类型的链接
    for i in type_urls[start:end]:  # 遍历类型链接列表
        type_url = 'https://templates.office.com' + i
        text_type = get_one_index_page(type_url)  # 获取一个类型页面
        page_number = count_page_number(text_type)  # 计算一个类型总的页面数
        for j in range(1, int(page_number[0]) + 1):
            if j == 1:
                type_url2 = 'https://templates.office.com/zh-cn/%e4%b8%9a%e5%8a%a1'
            else:
                type_url2 = change_type_page(j, i)
            print(type_url2)
            text_type2 = get_one_index_page(type_url2)
            download_page_url = parse_type_page_urls(text_type2)
            for k in download_page_url:
                url = 'https://templates.office.com' + k
                print(url)
                down_page = get_one_index_page(url)
                try:
                    down_url = get_download_url(down_page)
                    print(down_url)
                    for z in down_url:
                        save_template(z[0], z[1], z[2], z[3])
                        time.sleep(1)
                except:
                    print("没有数据")


if __name__ == '__main__':
    main(0, 62)
# from multiprocessing import Process
#
# p_list = []
# for i in range(0, 62, 5):
#     p = Process(target=main, args=(i, i + 5))
#     p.start()

# url = 'https://templates.office.com/'
# text = get_one_index_page(url)
# index_url = parse_index_urls(text)
# print(index_url)

# url = 'https://templates.office.com/zh-cn/%e4%b8%9a%e5%8a%a1'
# text = get_one_index_page(url)
# type_page_urls = parse_type_page_urls(text)
# print(type_page_urls)

# url = 'https://templates.office.com/zh-cn/%e4%b8%9a%e5%8a%a1'
# text = get_one_index_page(url)
# print(text)

# url = 'https://templates.office.com/zh-cn/%e4%b8%9a%e5%8a%a1'
# text = get_one_index_page(url)
# number = count_page_number(text)
# print(number)

# url = 'https://templates.office.com/zh-cn/%e8%b4%b9%e7%94%a8%e6%97%a5%e8%ae%b0%e8%b4%a6-tm00000074'
# text = get_one_index_page(url)
# download_url = get_download_url(text)
# print(download_url)

# url = 'https://templates.office.com/zh-cn/%e8%b4%b9%e7%94%a8%e6%97%a5%e8%ae%b0%e8%b4%a6-tm00000074'
# text = get_one_index_page(url)
# filename = save_template(text)
# for i in filename:
#     print(i)
