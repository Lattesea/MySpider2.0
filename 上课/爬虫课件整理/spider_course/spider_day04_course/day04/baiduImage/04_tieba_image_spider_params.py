import requests
from lxml import etree
import time
import random
from urllib import  parse

class TiebaImageSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'
        self.headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)' }

    # 功能函数1: 获取html
    def get_html(self,url,params={}):
        res = requests.get(url=url,params=params,headers=self.headers)
        html = res.content

        return html

    # 功能函数2: 解析
    def xpath_func(self,html,xpath_bds):
        parse_obj = etree.HTML(html)
        r_list = parse_obj.xpath(xpath_bds)

        return r_list

    # 做事情
    def parse_html(self,url,params):
        # 1. 先提取帖子链接
        one_html = self.get_html(url,params).decode()
        xpath_bds = '//li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/@href'
        # tlink_list: ['/html/xxx','/html/xxx','']
        tlink_list = self.xpath_func(one_html,xpath_bds)
        # 2.for遍历
        for tlink in tlink_list:
            tlink = 'http://tieba.baidu.com' + tlink
            # 对1个帖子链接做完所有事情
            # 向帖子发请求+提取图片链接+向图片发请求+保存图片
            self.get_image(tlink)

    # 向帖子发请求+提取图片链接+向图片发请求+保存图片
    def get_image(self,tlink):
        html = self.get_html(tlink).decode()
        # xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        img_link_list = self.xpath_func(html,xpath_bds)
        for img_link in img_link_list:
            # 保存图片
            self.save_image(img_link)

    def save_image(self,img_link):
        html = self.get_html(img_link)
        filename = img_link[-10:]
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')


    def run(self):
        name = input('贴吧名:')
        start = int(input('起始页:'))
        end = int(input('终止页:'))

        for page in range(start,end+1):
            pn = (page-1)*50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            self.parse_html(self.url,params)

if __name__ == '__main__':
    spider = TiebaImageSpider()
    spider.run()




























