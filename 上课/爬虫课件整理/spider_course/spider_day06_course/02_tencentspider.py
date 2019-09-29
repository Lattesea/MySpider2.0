import requests
import json
import random
import time
from fake_useragent import UserAgent
from urllib import parse

class TencentSpider(object):
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'

    # headers
    def get_headers(self):
        ua = UserAgent()
        headers = { 'User-Agent' : ua.random }
        return headers

    # 获取json数据
    def get_json(self,url):
        html_json = requests.get(
            url=url,
            headers=self.get_headers()
        ).text
        html_json = json.loads(html_json)
        return html_json

    # 解析+提取数据
    def parse_html(self,one_url):
        one_html = self.get_json(one_url)
        # for遍历每一个职位的postId
        for one in one_html['Data']['Posts']:
            postId = one['PostId']
            # 拼接详情页URL+获取所有数据
            two_url = self.two_url.format(postId)
            self.parse_two_page(two_url)

    # 解析二级页面
    def parse_two_page(self,two_url):
        two_html = self.get_json(two_url)

        item = {}
        item['name'] = two_html['Data']['RecruitPostName']
        item['requirement'] = two_html['Data']['Requirement']
        item['response'] = two_html['Data']['Responsibility']

        print(item)

    # 获取总页数
    def get_total(self,keyword):
        url = self.one_url.format(keyword,1)
        html = self.get_json(url)
        total = html['Data']['Count'] // 10 + 1

        return total

    # 入口函数
    def run(self):
        keyword = input('请输入职位类别:')
        keyword = parse.quote(keyword)

        total = self.get_total(keyword)
        print(total)
        for index in range(1,total+1):
            one_url = self.one_url.format(keyword,index)
            self.parse_html(one_url)
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    spider = TencentSpider()
    spider.run()






















































