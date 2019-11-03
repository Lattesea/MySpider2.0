#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 19-10-16 下午2:44
# @Author : Lattesea
# @File : YY评级下载系统界面.py
"""
    界面
"""


class YYpingjipage(object):
    def index_page(self):
        """
            一级页面:功能选择页面
        :return:
        """
        print("***************************")
        print("*** 欢迎使用YY评级下载系统 ***")
        print("*-------------------------*")
        print("*          功能            *")
        print("*      1.YY评级下载        *")
        print("*      2.调研报告下载       *")
        print("***************************")
        select = input("请选择功能:")
        return select


    def query_page(self):
        print("***************************")
        print("*         查询界面         *")
        print("*-------------------------*")
        print("***    1.根据主体类型     ***")
        print("***    2.根据YY等级      ***")
        print("***    3.根据是否上市     ***")
        print("***    4.根据企业性质     ***")
        print("***    5.根据关键字       ***")
        print("***    输入空格返回上一级  ***")
        print("***************************")
        keyword = input("请输入查询根据:")
        return keyword


    def main_types_page(self):
        print("***************************")
        print("*         主体类型         *")
        print("*-------------------------*")
        print("*         1.城投           *")
        print("*         2.产业           *")
        print("*     输入空格返回上一级     *")
        print("***************************")
        type = input("请输入主体类型:")
        return type

    def YY_level_page(self):
        print("***************************")
        print("*          YY等级          *")
        print("*-------------------------*")
        print("*         1.1/10          *")
        print("*         2.2/10          *")
        print("*         3.3/10          *")
        print("*         4.4/10          *")
        print("*         5.5/10          *")
        print("*         6.6/10          *")
        print("*         7.7/10          *")
        print("*         8.8/10          *")
        print("*         9.9/10          *")
        print("*         10.10/10        *")
        print("*     输入空格返回上一级     *")
        print("***************************")
        level = input("请输入YY等级:")
        return level

    def listed_page(self):
        print("***************************")
        print("*         是否上市         *")
        print("*-------------------------*")
        print("*         1.已上市         *")
        print("*         2.未上市         *")
        print("*     输入空格返回上一级     *")
        print("***************************")
        listed = input("请输入上市情况:")
        return listed

    def enterprise_nature_page(self):
        print("***************************")
        print("*         企业性质         *")
        print("*-------------------------*")
        print("*          1.国企          *")
        print("*          2.民营          *")
        print("*     输入空格返回上一级     *")
        print("***************************")
        enterprise = input("请选择企业性质:")
        return enterprise

    def keyword_query(self):
        print("***************************")
        print("*         关键字查询        *")
        print("*-------------------------*")
        print("*      请输入搜索关键字      *")
        print("*     输入空格返回上一级     *")
        print("***************************")
        keyword = input(":")
        return keyword

    def crawler_page(self):
        print("***************************")
        print("*         爬取界面         *")
        print("*-------------------------*")
        print("***    1.爬取基本信息     ***")
        print("***    2.爬取估值数据     ***")
        print("***    3.爬取二级成交     ***")
        print("***    4.爬取历史评级     ***")
        print("***    5.爬取财务评分     ***")
        print("***    输入空格返回上一级  ***")
        print("***************************")
        crawler = input("请输入爬取的信息")
        return crawler
