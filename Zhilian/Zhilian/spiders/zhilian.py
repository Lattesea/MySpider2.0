# -*- coding: utf-8 -*-
"""
    每次记得都要打开二级页面复制里面的acw_sc__v2替换,这个是有时间限制的
"""

import scrapy
import json
from urllib import parse
import requests
from ..items import ZhilianItem
from lxml import etree
import re


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['www.zhaopin.com', 'fe-api.zhaopin.com', 'jobs.zhaopin.com']
    # start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=763&kw=python&kt=3']
    one_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=763&kw={}&kt=3'
    keyword = input("请输入工作类型:")

    def start_requests(self):
        headers = {
            "cookie": "sou_experiment=psapi; x-zp-client-id=6dde1cc6-a24b-49bf-c203-1f7cc437e18c; urlfrom2=121114583; adfcid2=www.baidu.com; adfbid2=0; sts_deviceid=16e4c760dab6a8-05a89cb8be675c-7711a3e-1327104-16e4c760dac8a0; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22%24device_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%7D; acw_tc=9dff8bcb15732408363682015e590e043186a9dd5ac8af4cd543618cbe; LastCity%5Fid=763; LastCity=%E5%B9%BF%E5%B7%9E; ZP_OLD_FLAG=false; CANCELALL=1; POSSPORTLOGIN=1; urlfrom=121114583; adfcid=www.baidu.com; adfbid=0; __utma=269921210.1266153240.1573240836.1573240836.1573279420.2; __utmc=269921210; __utmz=269921210.1573279420.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=269921210.1.10.1573279420; dywec=95841923; dywea=95841923.793204343791415700.1573240836.1573240836.1573279420.2; dywez=95841923.1573279420.2.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; dyweb=95841923.1.10.1573279420; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1570976764,1573240836,1573279420; sts_sg=1; sts_sid=16e4ec2ce81148-07d6d07fa47642-7711a3e-1327104-16e4ec2ce827c6; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2e2W0Wg_yswsuNNAgNN6TrjkxZv2vETEHMcan3liZ8PjUt0u48IIGOp4AdWiqwiQ%26wd%3D%26eqid%3De47e0d9f0017cc57000000065dc656ba; jobRiskWarning=true; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1573279427; sts_evtseq=4; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22d85620ba-c303-4f5a-8ca7-ac110e2f2d5a-sou%22%2C%22funczone%22:%22smart_matching%22}}",
            "origin": "https://sou.zhaopin.com",
            "referer": "https://sou.zhaopin.com/?jl=763&kw=python&kt=3",
        }
        keyword = parse.quote(self.keyword)
        for index in range(0, 991, 90):
            url = self.one_url.format(index, keyword)
            yield scrapy.Request(
                # headers=headers,
                url=url,
                callback=self.parse_one_page
            )

    def parse_one_page(self, response):
        html = response.text
        html = json.loads(html)
        cookies = {
            "sts_deviceid": "16e4c760dab6a8-05a89cb8be675c-7711a3e-1327104-16e4c760dac8a0",
            "JSloginnamecookie": "18998261232",
            "acw_sc__v2": "5dc7b4144787340af2e1bc1e1644dbe7ed9284df"
        }
        # 真的是卧槽了,cookies那么多参数只有三个是有用的,之后可以试试acw_sc__v2的破解,这样就不用爬一半就过期
        for job in html['data']['results']:
            item = ZhilianItem()
            item['jobname'] = job['jobName']  # 岗位名称
            item['company_name'] = job['company']['name']  # 公司名称
            item['company_type'] = job['company']['type']['name']  # 公司类型
            item['company_size'] = job['company']['size']['name']  # 公司大小
            item['city'] = job['city']['display']  # 城市
            item['updateDate'] = job['updateDate']  # 更新日期
            item['salary'] = job['salary']  # 薪资
            item['eduLevel'] = job['eduLevel']['name']  # 学历
            item['workingExp'] = job['workingExp']['name']  # 工作经验
            item['welfare'] = job['welfare']  # 福利
            item['url'] = job['positionURL']
            url = job['positionURL']
            # headers["referer"] = url
            # print(item)

            yield scrapy.Request(
                cookies=cookies,
                url=url,
                meta={'item': item},
                callback=self.parse_two_page
            )

    def parse_two_page(self, response):
        item = response.meta['item']
        # text=requests.get()
        # html = etree.HTML(response.text)
        item['people'] = response.xpath("//ul[@class='summary-plane__info']/li[4]/text()").extract()
        # print(response.text)
        # item['people'] = re.findall('招(.*?)人', response.text)
        item['dult'] = response.xpath("//div[@class='describtion']/div[@class='describtion__detail-content']/p/text()").extract()
        yield item
