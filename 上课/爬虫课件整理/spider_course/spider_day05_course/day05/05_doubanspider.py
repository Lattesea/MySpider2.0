import requests


class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/' \
                   'top_list?type=11&interval_id=' \
                   '100%3A90&action=&start={}&limit=20'
        self.headers = { 'User-Agent':'Mozilla/5.0' }

    def get_data(self):
        for i in range(0,41,20):
            url = self.url.format(i)
            self.parse_html(url)

    def parse_html(self,url):
        html = requests.get(
            url=url,
            headers=self.headers
        ).json()
        # 解析并提取数据: html:[{},{},{}]
        for film in html:
            name = film['title']
            score = film['score']
            print(score,name)

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.get_data()




















