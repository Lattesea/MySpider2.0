from urllib import request
import re
import time
import random
from useragents import ua_list
import pymongo

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 添加计数变量
        self.i = 0
        # 创建3个对象
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['filmtab']


    # 请求
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # 直接调用解析函数
        self.parse_html(html)

    # 解析
    def parse_html(self,html):
        # r_list: [('月光宝盒',' 周星驰','1994-01-01'),(),()]
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        # 直接调用写入函数
        self.write_html(r_list)

    # 保存
    def write_html(self, r_list):
        for r in r_list:
            item = {}
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()[5:15]
            # 插入到mongodb数据库
            self.myset.insert_one(item)

    # 主函数
    def run(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 随机休眠 - uniform生成随机浮点数
            time.sleep(random.uniform(1,2))
        print('数量:',self.i)


if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))


















