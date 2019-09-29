from selenium import webdriver
import time

class JdSpider(object):
    def __init__(self):
        self.url = 'https://www.jd.com/'
        # 创建浏览器对象
        self.browser = webdriver.Chrome()
        self.i = 0
        self.page = 1

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
        # 拉到最下面,所有商品加载,再提取数据
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(3)

        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        item = {}
        for li in li_list:
            # 用 find_element_xxx
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
            item['comment'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
            item['market'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()
            print(item)
            self.i += 1
        print('第%d页抓取完成' % self.page)
        self.page += 1

    # 入口函数
    def run(self):
        self.get_html()
        for i in range(4):
            self.parse_html()
            # 判断是否为最后一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                # -1说明没找到,不是最后一页,点击 下一页 按钮
                self.browser.find_element_by_class_name('pn-next').click()
                # 给新的一页元素加载预留时间
                time.sleep(3)
            # else:
            #     break
        print('数量:',self.i)

if __name__ == '__main__':
    spider = JdSpider()
    spider.run()


















