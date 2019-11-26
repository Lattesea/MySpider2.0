import requests
from fake_useragent import UserAgent
from lxml import etree


class LianghuaSpider(object):
    def __init__(self):
        self.url = 'https://cn.tradingview.com/chart/lx92Cj8S/'

    def get_headers(self):
        ua = UserAgent()
        headers = {

        }

        return headers

    def parse(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    spider = LianghuaSpider()
    spider.run()
