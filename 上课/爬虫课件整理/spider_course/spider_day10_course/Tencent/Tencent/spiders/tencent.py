# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import requests
import json
from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn'
    keyword = input('请输入职位类别:')

    # 重写start_requests() - 生成url地址交给调度器
    def start_requests(self):
        keyword = parse.quote(self.keyword)
        total = self.get_total(keyword)
        for index in range(1,total):
            url = self.one_url.format(keyword,index)
            yield scrapy.Request(
                url=url,
                callback=self.parse_one_page
            )

    # 获取总页数: 解析一级页面第1页的json数据
    def get_total(self,keyword):
        url = self.one_url.format(keyword,1)
        html = requests.get(url=url).json()
        count = html['Data']['Count']
        if count % 10 == 0:
            total = count // 10
        else:
            total = count // 10 + 1

        return total

    # 解析一级页面函数: 提取 postId
    def parse_one_page(self,response):
        # 获取响应内容:response.text -> json格式字符串
        html = response.text
        html = json.loads(html)
        for job in html['Data']['Posts']:
            # 创建item对象
            item = TencentItem()
            post_id = job['PostId']
            # 详情页地址+入调度器
            url = self.two_url.format(post_id)
            yield scrapy.Request(
                url=url,
                meta={'item':item},
                callback=self.parse_two_page
            )
    # 解析二级页面,提取具体数据
    def parse_two_page(self,response):
        item = response.meta['item']
        html = json.loads(response.text)['Data']
        item['job_name'] = html['RecruitPostName']
        item['job_type'] = html['CategoryName']
        item['job_duty'] = html['Responsibility']
        item['job_require'] = html['Requirement']
        item['job_address'] = html['LocationName']
        item['job_time'] = html['LastUpdateTime']

        yield item




















