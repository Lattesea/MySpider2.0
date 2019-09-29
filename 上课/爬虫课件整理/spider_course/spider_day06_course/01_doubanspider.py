import requests
import json
from fake_useragent import UserAgent
import time
import random
import re

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?' \
                   'type={}&interval_id=100%3A90&action=&' \
                   'start={}&limit=20'
        self.i = 0

    # 获取随机请求头
    def get_headers(self):
        ua = UserAgent()
        headers = { 'User-Agent' : ua.random }
        return headers

    # 获取响应内容
    def get_html(self,url):
        html = requests.get(
            url=url,
            headers=self.get_headers()
        ).text
        return html

    # 提取数据 - 电影名称+评分
    def parse_page(self,url):
        html_json = self.get_html(url)
        # 把html_json转为python数据类型
        html_py = json.loads(html_json)
        for one_film in html_py:
            name = one_film['title']
            score = one_film['score']

            print(name,score)
            self.i += 1

    # 给定一个类别,能返回对应类型码
    def get_code(self,name):
        url = 'https://movie.douban.com/chart'
        html = self.get_html(url)
        re_bds = '<a href="/typerank.*?type=(.*?)&.*?>(.*?)</a>'
        pattern = re.compile(re_bds,re.S)
        # r_list: [('11','剧情'),('13','爱情'),()]
        r_list = pattern.findall(html)
        # name参数,如何根据name返回对应的类型码
        item = {}
        # 用于主函数中提示字符串
        menu = ''
        for r in r_list:
            item[r[1]] = r[0]
            # menu: 剧情|喜剧|爱情|动作|.....
            menu = menu + r[1] + '|'

        type_code = item[name]

        return type_code,menu


    # 获取某个类别电影总数函数
    def get_total(self,type_code):
        url = 'https://movie.douban.com/j/chart/' \
              'top_list_count?type={}&' \
              'interval_id=100%3A90'.format(type_code)
        html = self.get_html(url)
        html = json.loads(html)
        total = html['total']

        return total

    # 入口函数
    def run(self):
        # 单纯的想要获取menu
        type_code, menu = self.get_code('剧情')
        name = input(menu + '\n' + '请输入要抓取的电影类别:')
        # 通过用户输入,查找对应类型码
        type_code,menu = self.get_code(name)
        # 根据类型码计算此类型电影总数
        total = self.get_total(type_code)

        for start in range(0,total,20):
            url = self.url.format(type_code,start)
            self.parse_page(url)
            # 随机休眠
            time.sleep(random.randint(1,3))

        print('总数:',self.i)


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()































