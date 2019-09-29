import requests
from lxml import etree
from fake_useragent import UserAgent
import os

class CodeSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1905/13_redis/'
        self.auth = ('tarenacode','code_2013')

    def get_headers(self):
        ua = UserAgent()
        headers = { 'User-Agent':ua.random }
        return headers

    def parse_html(self):
        # 1. 获取响应
        html = requests.get(
            url=self.url,
            auth=self.auth,
            headers=self.get_headers()
        ).text
        # 2. 解析数据
        parse_obj = etree.HTML(html)
        # href_list: ['..','day01','redis_day01.zip']
        href_list = parse_obj.xpath('//a/@href')
        # 只提取 .zip 或者 .rar 或者 .tar.gz 的
        for href in href_list:
            if href.endswith('.zip') or href.endswith('.rar') or href.endswith('.tar.gz'):
                self.save_file(href)


    def save_file(self,href):
        # href: redis_day01.zip
        # 想办法创建对应文件夹
        base_directory = '/home/tarena/code/'
        directory = base_directory + \
                '/'.join(self.url.split('/')[3:-1]) + '/'

        if not os.path.exists(directory):
            os.makedirs(directory)

        # 下载链接
        file_url = self.url + href
        html = requests.get(
            url=file_url,
            auth=self.auth,
            headers=self.get_headers()
        ).content
        # filename: /home/tarena/code/AIDCode/AID1905/
        # 13_redis/redis_day01.zip
        filename = directory + href
        with open(filename,'wb') as f:
            f.write(html)
        print(href,'下载成功')

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = CodeSpider()
    spider.run()
























