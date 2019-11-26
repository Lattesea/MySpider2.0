import requests
from fake_useragent import UserAgent
import json


class LianghuaSpider(object):
    def __init__(self):
        self.url = ''

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "user-agent": ua.random
        }
        return headers

    def parse(self):
        response = requests.get(url=self.url, headers=self.get_headers()).text
        html = json.loads(response)
        print(html)
        return html

    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = LianghuaSpider()
    spider.run()
