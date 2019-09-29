# -*- coding: utf-8 -*-
import scrapy
import json
from urllib import parse
import requests
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn'
    # start_urls = ['http://hr.tencent.com/']
    keyword = input("请输入工作类型:")

    def start_requests(self):
        keyword = parse.quote(self.keyword)
        total = self.get_total(keyword)
        for index in range(1, total):
            url = self.one_url.format(keyword, index)
            yield scrapy.Request(
                url=url,
                callback=self.parse_one_page
            )

    def get_total(self, keyword):
        url = self.one_url.format(keyword, 1)
        html = requests.get(url=url).json()
        count = html['Data']['Count']
        if count % 10 == 0:
            total = count // 10
        else:
            total = count // 10 + 1
        return total

    def parse_one_page(self, response):
        html = response.text
        html = json.loads(html)
        for job in html['Data']['Posts']:
            item=TencentItem()
            post_id = job['PostId']
            url = self.two_url.format(post_id)
            yield scrapy.Request(
                url=url,
                meta={'item': item},
                callback=self.parse_two_page
            )

    def parse_two_page(self, response):
        item = response.meta['item']
        html = json.loads(response.text)['Data']

        item['job_name'] = html['RecruitPostName']
        item['job_type'] = html['CategoryName']
        item['job_duty'] = html['Responsibility']
        item['job_require'] = html['Requirement']
        item['job_address'] = html['LocationName']
        item['job_time'] = html['LastUpdateTime']

        yield item
