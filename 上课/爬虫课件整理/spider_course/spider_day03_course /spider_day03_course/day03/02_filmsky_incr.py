from urllib import request
import time
import random
from useragents import ua_list
import re
import pymysql
from hashlib import md5

class FilmSky(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.db = pymysql.connect(
            'localhost','root','123456','filmskydb',charset='utf8'
        )
        self.cursor = self.db.cursor()

    # 请求函数
    def get_html(self,url):
        headers = {'User-Agent':random.choice(ua_list)}
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        # utf-8不能识别 0xb5
        # 1. 查看网页源码,查看网站的编码
        # 2. decode()第2个参数:ignore,忽略掉特殊字符
        html = res.read().decode('gb2312','ignore')

        return html

    # 正则解析函数
    def re_func(self,re_bds,html):
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)

        return r_list

    # md5生成指纹函数
    def md5_string(self,string):
        s = md5()
        s.update(string.encode())
        md5_string = s.hexdigest()

        return md5_string

    # 解析:一级页面 - 详情页链接
    def parse_html(self,one_url):
        one_html = self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # one_list: ['/html/xxx/xxx','','']
        one_list = self.re_func(re_bds,one_html)
        for href in one_list:
            two_url = 'https://www.dytt8.net' + href
            # 如果 is_go_on(two_url)返回True,代表没抓过
            if self.is_go_on(two_url):
                # 在此,获取到此电影所有数据,然后再遍历下一个
                self.get_film_info(two_url)
                # 2.抓完1个电影信息后把指纹存到数据表中
                finger = self.md5_string(two_url)
                ins = 'insert into request_finger values(%s)'
                self.cursor.execute(ins,[finger])
                self.db.commit()
                # 随机休眠
                time.sleep(random.randint(1,2))

    # 判断two_url是否已经抓取过
    def is_go_on(self,two_url):
        # 先进行md5加密 - request_finger表中存的为指纹
        md5_two_url = self.md5_string(two_url)
        # 数据表中判断
        sel = 'select finger from request_finger where finger=%s'
        # execute()方法返回值: 受影响的条数,未查询到返回 0
        result = self.cursor.execute(sel,[md5_two_url])
        # result为0表示未抓过,返回True
        if not result:
            return True

    # 解析二级页面: 电影详情页函数
    def get_film_info(self,two_url):
        item = {}
        two_html = self.get_html(two_url)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
        # film_list: [('X战警','ftp://xxx.mkv')]
        film_list = self.re_func(re_bds,two_html)
        # 电影名称+下载链接
        item['name'] = film_list[0][0].strip()
        item['download'] = film_list[0][1].strip()
        print(item)
        ins = 'insert into filmtab values(%s,%s)'
        L = [ item['name'],item['download'] ]
        self.cursor.execute(ins,L)
        self.db.commit()

    # 入口函数
    def run(self):
        for page in range(1,201):
            url = self.url.format(page)
            self.parse_html(url)
        # 断开数据库
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    spider = FilmSky()
    spider.run()























