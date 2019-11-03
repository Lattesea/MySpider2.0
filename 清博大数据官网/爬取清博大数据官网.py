"""
    根据搜索关键词爬取信息
"""
import requests
from fake_useragent import UserAgent
from lxml import etree

class QinghuaSpider(object):
    def __init__(self):
        self.url = ''

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "visitor_type=old; acw_tc=76b20fed15713126281494867e310346713b1dce0aa91be23c3126069d7a9f; _csrf-frontend=b3b2f4b7e13132c2ce5bec3fe989bf376547f788f8fb9a91671f52ba23a664dca%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22zAIIaWjgSMnXcm0scrREwy39a7OwYm-u%22%3B%7D; Hm_lvt_293b2731d4897253b117bb45d9bb7023=1571312630; 53gid2=10888828375004; 53gid0=10888828375004; 53gid1=10888828375004; 53revisit=1571312630621; 53kf_72213613_from_host=www.gsdata.cn; 53kf_72213613_land_page=http%253A%252F%252Fwww.gsdata.cn%252F; kf_72213613_land_page_ok=1; 53uvid=1; onliner_zdfq72213613=0; 53kf_72213613_keyword=http%3A%2F%2Fwww.gsdata.cn%2F; _gsdataCL=WzAsIjE4OTk4MjYxMjMyIiwiMjAxOTEwMTcxOTQ2MzAiLCJhOWUxOTVhYzZmM2Q3YWVmNDRjYjg5ODc0ZTk4OTRhYiIsMjM1MjUwXQ%3D%3D; _gsdataOL=235250%3B18998261232%3B%7B%220%22%3A%22%22%2C%221%22%3A%22%22%2C%222%22%3A%22%22%2C%223%22%3A%22%22%2C%224%22%3A%22%22%2C%225%22%3A%22%22%2C%2299%22%3A%2220191017%22%7D%3B4f2cd0b9020ac3c0ef8869bcb975f952; _identity-frontend=34e74e27a96b7c33181abc0f341a5e8935489a2381d60b40f3899251e536f624a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A28%3A%22%5B%22409077%22%2C%22test+key%22%2C604800%5D%22%3B%7D; visitor_type=old; Hm_lpvt_293b2731d4897253b117bb45d9bb7023=1571312835; PHPSESSID=c0s3l4kic085pt3prcom1j7na4",
            "Host": "www.gsdata.cn",
            "Referer": "http://www.gsdata.cn/query/arc?q=%E8%88%AA%E7%A9%BA%E5%8F%91%E5%8A%A8%E6%9C%BA",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua.random
        }
        return headers

    def parse(self, keyword):
        params = {
            "q": keyword
        }
        text=requests.get(url=self.url,headers=self.get_headers(),params=params).text
        html=etree.HTML(text)
