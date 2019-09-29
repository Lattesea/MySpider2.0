from urllib import request
import time
import random
from useragents import ua_list
import re

class FilmSky(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

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

    # 解析:一级页面 - 详情页链接
    def parse_html(self,one_url):
        one_html = self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # one_list: ['/html/xxx/xxx','','']
        one_list = self.re_func(re_bds,one_html)
        for href in one_list:
            two_url = 'https://www.dytt8.net' + href
            # 在此,获取到此电影所有数据,然后再遍历下一个
            self.get_film_info(two_url)
            # 随机休眠
            time.sleep(random.randint(1,2))

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

    # 入口函数
    def run(self):
        for page in range(1,201):
            url = self.url.format(page)
            self.parse_html(url)

if __name__ == '__main__':
    spider = FilmSky()
    spider.run()























