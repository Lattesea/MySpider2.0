from selenium import webdriver
import time

class JdSpider(object):
    def __init__(self):
        self.url = 'https://www.jd.com/'
        # 创建浏览器对象
        self.browser = webdriver.Chrome()

    # 跳转到商品详情页 - 爬虫书
    def get_html(self):
        # 找节点,send_keys() click()
        so = '//*[@id="key"]'
        button = '//*[@id="search"]/div/div[2]/button'
        self.browser.get(self.url)
        self.browser.find_element_by_xpath(so).send_keys('爬虫书')
        self.browser.find_element_by_xpath(button).click()
        # 必须的: 给页面留出加载时间
        time.sleep(3)

    # 匹配每个商品信息的li节点对象列表, li.text
    def parse_html(self):
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            L = li.text.split('\n')
            if L[0].startswith('￥'):
                price = L[0]
                market = L[3]
            elif L[0] == '单件':
                price = L[3]
                market = L[6]
            elif '减' in L[0]:
                price = L[1]
                market = L[4]


            print(price,market)

if __name__ == '__main__':
    spider = JdSpider()
    spider.get_html()
    spider.parse_html()


















