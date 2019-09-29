from urllib import request,parse
import random
import time
from fake_useragent import UserAgent

class TiebaSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'

    # 生成随机的User-Agent
    def get_headers(self):
        ua = UserAgent()
        headers = {'User-Agent':ua.random}
        return headers

    # 获取响应内容
    def get_page(self,url):
        headers = self.get_headers()
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()

        return html

    # 解析,提取数据
    def parse_page(self):
        pass

    # 保存数据
    def write_page(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)

    # 入口函数
    def run(self):
        name = input('请输入贴吧名:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        kw = parse.quote(name)
        # 拼接 + 获取内容 + 保存
        for i in range(start,end+1):
            pn = (i-1)*50
            url = self.url.format(kw,pn)
            html = self.get_page(url)
            filename = '{}-第{}页.html'.format(name,i)
            self.write_page(filename,html)
            print('第%d页抓取成功' % i)

            # 每爬取1个页面随机休眠1-3秒
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    begin = time.time()
    spider = TiebaSpider()
    spider.run()
    stop = time.time()
    print('执行时间: %.2f' % (stop-begin))


























