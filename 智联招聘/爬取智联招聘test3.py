#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-23 下午5:27 
# @Author : Lattesea 
# @File : 爬取智联招聘test3.py 
import requests
from fake_useragent import UserAgent
import json

class ZhilianzhaopingSpider(object):
    def __init__(self):
        self.url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90' \
                   '&cityId={}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={' \
                   '}' \
                   '&kt=3&_v=0.77373093&x-zp-page-request-id=0b5f2633ddbd456297d1e7225d573313-1568688746815-57677&x-zp-client-id=0e4725ac-38db-4df7-90f1-4889de4921f8'
        self.cityId = {'北京': 530, '上海': 538, '深圳': 765, '广州': 763, '天津': 531, '成都': 801, '杭州': 653, '武汉': 736,
                       '大连': 600, '长春': 613,
                       '南京': 635, '济南': 702, '青岛': 703, '苏州': 639, '沈阳': 599, '西安': 854, '郑州': 719, '长沙': 749,
                       '重庆': 551, '哈尔滨': 622,
                       '无锡': 636, '宁波': 654, '福州': 681, '厦门': 682, '石家庄': 565, '合肥': 664, '惠州': 773}

    def get_one_headers(self):
        ua=UserAgent()
        headers={
            # ":authority": "sou.zhaopin.com",
            # ":method": "GET",
            # ":path": "/?jl=763&kw=%E8%B4%A8%E9%87%8F&kt=3",
            # ":scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "x-zp-client-id=0e4725ac-38db-4df7-90f1-4889de4921f8; sts_deviceid=16bdeedbdad1e9-00fdc8bb66702a-15231708-2073600-16bdeedbdae3e5; adfbid2=0; acw_tc=2760820915685967672826439e3c8a2b0f3c644706237911551130294b3083; sou_experiment=unexperiment; LastCity=%E5%B9%BF%E5%B7%9E; LastCity%5Fid=763; urlfrom2=121114583; adfcid2=www.baidu.com; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d379af1d9507-0b28d6a31ad2af-30750f58-2073600-16d379af1da6e4%22%2C%22%24device_id%22%3A%2216d379af1d9507-0b28d6a31ad2af-30750f58-2073600-16d379af1da6e4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; urlfrom=121114583; adfcid=www.baidu.com; adfbid=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568595964,1568688664,1568773029,1569229916; dywea=95841923.1452550701810909700.1568595964.1568773029.1569229916.4; dywec=95841923; dywez=95841923.1569229916.4.4.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; dyweb=95841923.1.10.1569229916; sts_sg=1; sts_sid=16d5d6448ae5d3-0358311cfc21da-30750f58-2073600-16d5d6448af5eb; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DQROlnlpmFc5Qt4GfMmYDiI2vD1aME_nhJ0f752nYGLk76AaPQ-XYvgcsLQ257sm3%26wd%3D%26eqid%3Df4ff854500085c5e000000065d888c54; jobRiskWarning=true; __utma=269921210.1365653252.1568595964.1568773029.1569229916.4; __utmc=269921210; __utmz=269921210.1569229916.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=269921210.1.10.1569229916; ZP_OLD_FLAG=false; POSSPORTLOGIN=8; CANCELALL=0; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1569229935; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%225b112558-ca89-430f-9abb-1d8407d65ed9-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=4",
            "referer": "https://www.zhaopin.com/",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": ua.random
        }

    def get_two_headers(self,url):
        ua=UserAgent()
        headers = {
            # ":authority": "jobs.zhaopin.com",
            # ":method": "GET",
            # ":path": "/CC141212849J00329043005.htm",
            # ":scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "x-zp-client-id=0e4725ac-38db-4df7-90f1-4889de4921f8; sts_deviceid=16bdeedbdad1e9-00fdc8bb66702a-15231708-2073600-16bdeedbdae3e5; adfbid2=0; sou_experiment=unexperiment; LastCity=%E5%B9%BF%E5%B7%9E; LastCity%5Fid=763; acw_tc=2760823f15685969430117169eb4e537c93815853ce63f742ab9bc708953f7; urlfrom2=121114583; adfcid2=www.baidu.com; urlfrom=121114583; adfcid=www.baidu.com; adfbid=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568595964,1568688664,1568773029,1569229916; dywea=95841923.1452550701810909700.1568595964.1568773029.1569229916.4; dywec=95841923; dywez=95841923.1569229916.4.4.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; dyweb=95841923.1.10.1569229916; sts_sg=1; sts_sid=16d5d6448ae5d3-0358311cfc21da-30750f58-2073600-16d5d6448af5eb; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DQROlnlpmFc5Qt4GfMmYDiI2vD1aME_nhJ0f752nYGLk76AaPQ-XYvgcsLQ257sm3%26wd%3D%26eqid%3Df4ff854500085c5e000000065d888c54; jobRiskWarning=true; __utma=269921210.1365653252.1568595964.1568773029.1569229916.4; __utmc=269921210; __utmz=269921210.1569229916.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=269921210.1.10.1569229916; ZP_OLD_FLAG=false; POSSPORTLOGIN=8; CANCELALL=0; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1569229952; acw_sc__v2=5d888cba452ef9d542e2225f1f093c4192c50ce1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d379af1d9507-0b28d6a31ad2af-30750f58-2073600-16d379af1da6e4%22%2C%22%24device_id%22%3A%2216d379af1d9507-0b28d6a31ad2af-30750f58-2073600-16d379af1da6e4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22f1422eea-17d4-4fa7-85e9-9c11932f1baa-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%228e91984f-a0b8-472e-965e-00162e31de12-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_evtseq=12",
            "referer": url,
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": ua.random
        }
        return headers

    def get_one_page(self, url):
        html_json = requests.get(url=url, headers=self.get_one_headers()).text
        html_py = json.loads(html_json)
        return html_py