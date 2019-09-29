import requests
from lxml import etree

class RenrenLogin(object):
    def __init__(self):
        # 抓取的url地址
        self.url = 'http://www.renren.com/970294164/profile'
        self.headers = {
            'Cookie':'td_cookie=18446744071183638191; anonymid=k0n5mw7b-yr20ef; depovince=GW; _r01_=1; JSESSIONID=abc-z0-dciI-7anVI080w; ick_login=e4d81bfe-4bd3-4d73-ad37-061473d9945f; first_login_flag=1; ln_uact=15110225726; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=4d826d37-e486-4bb4-b007-1d08a20dafc6%7C3317b1face1adcda7e34f17db4558a85%7C1568683539064%7C1%7C1568683541522; jebe_key=4d826d37-e486-4bb4-b007-1d08a20dafc6%7C3317b1face1adcda7e34f17db4558a85%7C1568683539064%7C1%7C1568683541526; wp_fold=0; jebecookies=20984bc9-51eb-474e-b879-184c6447b827|||||; _de=5411E55883CC3142BC1347536B8CB062; p=609fc60ff1377cbb862a79211c6d343d4; t=99e511d67091882efb64676bc7fe46f44; societyguester=99e511d67091882efb64676bc7fe46f44; id=970294164; xnsid=c3240af9; ver=7.0; loginfrom=null',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }

    def parse_html(self):
        html = requests.get(url=self.url,headers=self.headers).text
        parse_obj = etree.HTML(html)
        xpath_bds = '//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()'
        r_list = parse_obj.xpath(xpath_bds)
        # r_list: ['就读于国家检察官学院']
        print(r_list)

    def run(self):
        self.parse_html()

if __name__ == '__main__':
    spider = RenrenLogin()
    spider.run()














































