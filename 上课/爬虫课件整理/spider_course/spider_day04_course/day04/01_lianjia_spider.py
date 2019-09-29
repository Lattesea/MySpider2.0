import requests
from fake_useragent import UserAgent
from lxml import etree
import random
import time

class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'

    # 功能函数1: 获取随机User-Agent
    def get_headers(self):
        ua = UserAgent()
        headers = { 'User-Agent': ua.random }
        return headers

    # 获取页面
    def get_html(self,url):
        # 设置超时时间为5秒,尝试测试为3
        for i in range(3):
            try:
                res = requests.get(url=url,headers=self.get_headers(),timeout=5)
                res.encoding = 'utf-8'
                html = res.text
                return html
            except Exception as e:
                print('Failed,Retry:',i)
                continue

    # 解析页面
    def parse_html(self,url):
        # html返回值有2种: 1-html 2-None
        html = self.get_html(url)
        if html:
            parse_obj = etree.HTML(html)
            # 1. 基准xpath: li节点对象列表
            li_list = parse_obj.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            # 2. for循环依次遍历每个li节点,获取1个房源所有数据
            item = {}
            for li in li_list:
                # 名称

                re_bds = './/a[@data-el="region"]/text()'
                name_list = li.xpath(re_bds)
                item['name'] = [ name_list[0].strip() if name_list else None ][0]

                # 户型+面积+方位+精装
                # info_list: ['','三室两厅','100.99平米','南北','精装']
                re_bds = './/div[@class="houseInfo"]/text()'
                info_list = li.xpath(re_bds)
                info_list = [ info_list[0].split('|') if info_list else None ][0]
                if len(info_list) == 5:
                    item['model'] = info_list[1].strip()
                    item['area'] = info_list[2].strip()[:-2]
                    item['direction'] = info_list[3].strip()
                    item['perfect'] = info_list[4].strip()
                else:
                    item['model']=item['area']=item['direction']=item['perfect'] = None

                # 自己完成: 用列表推导式处理可能发生的异常？？？
                # 楼层+地区+总价+单价
                item['floor'] = li.xpath('.//div[@class="positionInfo"]/text()')[0].strip().split('-')[0].strip()
                item['address'] = li.xpath('.//div[@class="positionInfo"]/a/text()')[0].strip()
                item['total'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
                item['unit'] = li.xpath('.//div[@class="unitPrice"]/span/text()')[0].strip()[2:-4]

                print(item)

    def run(self):
        for pg in range(1,101):
            url = self.url.format(pg)
            self.parse_html(url)
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()


































