import requests
import json
import time
from fake_useragent import UserAgent
import pymysql
from hashlib import md5
import csv
import random


class Research_report_spider(object):
    def __init__(self):
        self.url = 'https://api.ratingdog.cn/v1/search?'
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='hebeidb',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://www.ratingdog.cn",
            "Referer": "https://www.ratingdog.cn/",
            "Sec-Fetch-Mode": "cors",
            "User-Agent": ua.random
        }
        return headers

    def parse(self):
        timestamp = str(int(time.time() * 1000))
        params = {
            "limit": "200",
            "offset": "0",
            "type": "4",
            "qtext": "",
            "filter": "",
            "_": timestamp
        }
        report_list = []
        report = {}
        html_json = requests.get(url=self.url, headers=self.get_headers(), params=params).text
        html_py = json.loads(html_json)
        print(html_py)
        for i in html_py['rows']:
            report['ReportTitle'] = i['ReportTitle']
            report['Description'] = i['Description']
            report['IssuerName'] = i['IssuerName']
            report['Industry'] = i['Industry']
            report['ShareholderBackground'] = i['ShareholderBackground']
            report['WebOficeApiUUID'] = i['WebOficeApiUUID']
            report['YYRating'] = i['YYRating']
            report['ID'] = i['ID']
            report['Area'] = i['Area']
            report['ResearchDate'] = i['ResearchDate']
            report_list.append(report)
        print(report_list)
        return report_list

    def create_finger(self, report_list):
        report_list_result = []
        for i in report_list:
            url = 'https://api.ratingdog.cn/v1/getResearchDocurl?id={}&type=1'.format(i['ID'])
            s = md5()
            s.update(url.encode())
            url_md5 = s.hexdigest()
            if self.judge(url_md5):
                ins = 'insert into request_finger values(%s)'
                self.cursor.execute(ins, [url_md5])
                self.db.commit()
                report_list_result.append(i)
        return report_list_result

    def judge(self, url_md5):
        sel = 'select finger from request_finger where finger=%s'
        result = self.cursor.execute(sel, [url_md5])
        if not result:
            return True

    def save(self, result):
        """
            将数据存进csv文件
        :param result:
        :return:
        """
        keyword_list = ['ReportTitle', 'Description', 'IssuerName', 'Industry', 'ShareholderBackground',
                        'WebOficeApiUUID', 'YYRating', 'ID', 'Area', 'ResearchDate']
        with open('report.csv', 'a', newline='')as f:
            writer = csv.DictWriter(f, keyword_list)
            writer.writerow(result)

    def report_run(self):
        try:
            result1 = self.parse()
            result2 = self.create_finger(result1)
            print(result2)
            self.save(result2)
            print("写入成功")
            time.sleep(random.uniform(1, 3))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    spider = Research_report_spider()
    spider.parse()
