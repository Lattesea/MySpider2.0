from urllib import request
import re
import time
import random
from useragents import ua_list
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 添加计数变量
        self.i = 0
        # 创建2个对象
        self.db = pymysql.connect(
            '127.0.0.1','root','123456','maoyandb',charset='utf8'
        )
        self.cursor = self.db.cursor()

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

    # # 保存 - execute()方法 [(),(),()]
    # def write_html(self, r_list):
    #     ins = 'insert into filmtab values(%s,%s,%s)'
    #     for r in r_list:
    #         L = [
    #             r[0].strip(),r[1].strip(),r[2].strip()[5:15]
    #         ]
    #         self.cursor.execute(ins,L)
    #         # 千万别忘: 提交到数据库执行
    #         self.db.commit()

    # 保存 - executemany()方法 [(),(),()]
    def write_html(self, r_list):
        L = []
        ins = 'insert into filmtab values(%s,%s,%s)'
        for r in r_list:
            t = (
                r[0].strip(), r[1].strip(), r[2].strip()[5:15]
            )
            L.append(t)
        self.cursor.executemany(ins, L)
        # 千万别忘: 提交到数据库执行
        self.db.commit()

    # 主函数
    def run(self):
        for offset in range(0,31,10):
            url = self.url.format(offset)
            self.get_html(url)
            # 随机休眠 - uniform生成随机浮点数
            time.sleep(random.uniform(1,2))
        print('数量:',self.i)
        # 所有页面数据抓取完成后再断开数据库连接
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))


















