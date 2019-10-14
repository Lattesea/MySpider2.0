#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-14 下午4:28 
# @Author : Lattesea 
# @File : 大数据平台test1.py 
import requests
from fake_useragent import UserAgent
import json


class DashujuSpider(object):
    def __init__(self):
        self.url = 'https://nqi.gmcc.net:20443/pro-adhoc/adhocquery'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": 4496,
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": "JSESSIONID=415DEAFFAD29553FDCAAC44A23563880; CASTGC=TGT-53036-mQ1uUgq9Ba13v43ji2Q9k9c2c2Y9dUDwgHJmsA2W6ZUiUBEFNO-cas",
            "Host": "nqi.gmcc.net:20443",
            "Origin": "https://nqi.gmcc.net:20443",
            "Referer": "https://nqi.gmcc.net:20443/pro-adhoc/adhocquery",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

    def parse(self):
        data = {
            "draw": "1",
            "columns[0][data]": "starttime",
            "columns[0][name]": "",
            "columns[0][searchable]": "true",
            "columns[0][orderable]": "true",
            "columns[0][search][value]": "",
            "columns[0][search][regex]": "false",
            "columns[1][data]": "endtime",
            "columns[1][name]": "",
            "columns[1][searchable]": "true",
            "columns[1][orderable]": "true",
            "columns[1][search][value]": "",
            "columns[1][search][regex]": "false",
            "columns[2][data]": "cgi",
            "columns[2][name]": "",
            "columns[2][searchable]": "true",
            "columns[2][orderable]": "true",
            "columns[2][search][value]": "",
            "columns[2][search][regex]": "false",
            "columns[3][data]": "city",
            "columns[3][name]": "",
            "columns[3][searchable]": "true",
            "columns[3][orderable]": "true",
            "columns[3][search][value]": "",
            "columns[3][search][regex]": "false",
            "columns[4][data]": "area",
            "columns[4][name]": "",
            "columns[4][searchable]": "true",
            "columns[4][orderable]": "true",
            "columns[4][search][value]": "",
            "columns[4][search][regex]": "false",
            "order[0][column]": "0",
            "order[0][dir]": "desc",
            "start": "0",
            "length": "200",
            "total": "0",
            "search[value]": "",
            "search[regex]": "false",
            'result': '{"result":[{"feildtype":"公共信息","table":"rnodbv2.v_a_adhoc_overview_lte_cell",'
                      '"tableName":"小区综合信息","datatype":"timestamp","columntype":"2","feildName":"开始时间","feild":"starttime","poly":"无","anyWay":"无","chart":"无","chartpoly":"无"},{"feildtype":"公共信息","table":"rnodbv2.v_a_adhoc_overview_lte_cell","tableName":"小区综合信息","datatype":"timestamp","columntype":"2","feildName":"结束时间","feild":"endtime","poly":"无","anyWay":"无","chart":"无","chartpoly":"无"},{"feildtype":"公共信息","table":"rnodbv2.v_a_adhoc_overview_lte_cell","tableName":"小区综合信息","datatype":"character varying","columntype":"2","feildName":"CGI","feild":"cgi","poly":"无","anyWay":"无","chart":"无","chartpoly":"无"},{"feildtype":"公共信息","table":"rnodbv2.v_a_adhoc_overview_lte_cell","tableName":"小区综合信息","datatype":"character varying","columntype":"2","feildName":"所属地市","feild":"city","poly":"无","anyWay":"无","chart":"无","chartpoly":"无"},{"feildtype":"公共信息","table":"rnodbv2.v_a_adhoc_overview_lte_cell","tableName":"小区综合信息","datatype":"character varying","columntype":"2","feildName":"所属区县","feild":"area","poly":"无","anyWay":"无","chart":"无","chartpoly":"无"}],"tableParams":{"supporteddimension":"","supportedtimedimension":"1"},"columnname":""}',
            'where': '[{"datatype":"timestamp","feild":"starttime","feildName":"","symbol":">=","val":"2019-10-13 '
                     '00:00:00","whereCon":"and","query":true},{"datatype":"timestamp","feild":"starttime","feildName":"","symbol":"<","val":"2019-10-14 23:59:59","whereCon":"and","query":true},{"datatype":"character","feild":"city","feildName":"","symbol":"in","val":"茂名","whereCon":"and","query":true}]',
            "indexcount": "0"
        }
        html_json = requests.post(url=self.url, headers=self.get_headers(), data=data).text
        print(html_json)
        # html_py = json.loads(html_json)
        # print(html_py)

    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = DashujuSpider()
    spider.run()
