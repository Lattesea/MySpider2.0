#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午2:17 
# @Author : Lattesea 
# @File : 测试.py

import requests
from lxml import etree
import re

url = "https://jobs.zhaopin.com/CC143220695J00189726615.htm"
headers = {
    "cookie": "sts_deviceid=16e4c760dab6a8-05a89cb8be675c-7711a3e-1327104-16e4c760dac8a0; JSloginnamecookie=18998261232; "
              # "JSpUserInfo=2f79277359665464547155685f6a4e7953735166566452715c68526a36792d73596654645c715c68506a4279517352665464567156685b6a41792673296658645c715568506a4c795a735166546457715068296a0b7912734a6606640b710868526a29793773596654645f7124683d6a477952735466486452714568586a4279597355665e6425712968546a4b7958733166246459712f68206a4a79557350665564517156685f6a43795b735f66306430715868586a417930732d66586451715568596a4b795373566655645f717; "
              # "sensorsdata2015jssdkcross=4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%2C%22first_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%7D; "
              # "zp_src_url=ww.baidu.com%2Flink%22%7D%2C%22first_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%7D; "
              # "jobRiskWarning=true; privacyUpdateVersion=2; "
              # "Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1573364414; "
              "acw_sc__v2=5dc7ab50bb25d441031653b7466f31a0ef15948b; "
              # "ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%222fac61b3-46b4-42ca-a959-d54a245f140e-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22dcb8b61d-93b8-4fd7-8040-aa05285c7b09-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}"
    # "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"
}

# headers["referer"]=url
response = requests.get(url=url, headers=headers).text
html=etree.HTML(response)
people1=html.xpath("//ul[@class='summary-plane__info']/li[4]/text()")
# print(response)
print(people1)
people = re.findall('<li>招(.*?)人</li>', response)
print(people)
