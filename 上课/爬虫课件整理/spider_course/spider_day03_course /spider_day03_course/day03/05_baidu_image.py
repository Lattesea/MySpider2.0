import requests
from useragents import ua_list
import time
import random
import re
import os
from urllib import parse

class BaiduImageSpider(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?' \
                   'tn=baiduimage&word={}'
        # 计数
        self.i = 1

    # 获取图片
    def get_image(self,url,word):
        headers = { 'User-Agent':random.choice(ua_list) }
        # 1. 获取图片链接列表
        html = requests.get(url=url,headers=headers).text
        pattern = re.compile('"middleURL":"(.*?)"',re.S)
        img_link_list = pattern.findall(html)
        # 创建对应文件夹,用来保存图片 /home/tarena/images/名字
        directory = '/home/tarena/images/{}/'.format(word)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 2. for循环遍历,下载每张图片
        for img_link in img_link_list:
            self.save_image(img_link,directory,word)
            # 控制爬取速率: 每爬完1张图片,休眠
            time.sleep(random.randint(1,2))

    # 保存图片函数
    def save_image(self,img_link,directory,word):
        headers = { 'User-Agent':random.choice(ua_list) }
        # 1. 向图片链接发请求,得到bytes类型
        try:
            html = requests.get(url=img_link,headers=headers).content
            filename = directory + '{}_{}.jpg'.format(word,self.i)
            # 2. 命名文件名,wb方式保存图片
            with open(filename,'wb') as f:
                f.write(html)
            self.i += 1
            print(filename,'下载成功')
        except Exception as e:
            pass

    # 入口函数
    def run(self):
        word = input('你想要谁的图片:')
        word1 = parse.quote(word)
        url = self.url.format(word1)
        self.get_image(url,word)

if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()











