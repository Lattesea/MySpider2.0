import requests
import time
import random
from hashlib import md5

class YdSpider(object):
    def __init__(self):
        # F12抓到的Request URL中地址
        self.post_url = 'http://fanyi.youdao.com/' \
                        'translate_o?smartresult=dict&' \
                        'smartresult=rule'
        self.headers = {
            # 检查频率最高的3个字段: Cookie Referer User-Agent
            "Cookie": "OUTFOX_SEARCH_USER_ID=-1258737612@10.169.0.83; JSESSIONID=aaaRPbU9VTB3V-mO4HJ0w; OUTFOX_SEARCH_USER_ID_NCOO=1111840937.5782938; ___rl__test__cookies=1568264679590",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        }
        self.proxies = {
            'http':'http://309435365:szayclhp@116.62.128.50:16817',
            'https':'https://309435365:szayclhp@116.62.128.50:16817'
        }

    # ts salt sign
    def get_ts_salt_sign(self,word):
        # ts
        ts = str(int(time.time()*1000))
        # salt
        salt = ts + str(random.randint(0,9))
        # sign
        string = "fanyideskweb" + word + salt + \
                              "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts,salt,sign

    # 攻克有道
    def attack_yd(self,word):
        ts,salt,sign = self.get_ts_salt_sign(word)
        data = {
            "i": word,
            "from":  "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "a4f4c82afd8bdba188e568d101be3f53",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        res = requests.post(
            url=self.post_url,
            data=data,
            proxies=self.proxies,
            headers=self.headers
        )
        # {"translateResult":[[{"tgt":"老虎","src":"tiger"}]]
        # ,"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 老虎；凶暴的人\r\n","n. (Tiger)人名；(英)泰格；(法)蒂热；(瑞典)蒂格\r\n"],"type":1}}
        # res.json()直接得到python数据类型 - 字典
        html = res.json()
        result = html['translateResult'][0][0]['tgt']

        return result

    def run(self):
        word = input('请输入要翻译的单词:')
        result = self.attack_yd(word)
        print('翻译结果:',result)

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()






