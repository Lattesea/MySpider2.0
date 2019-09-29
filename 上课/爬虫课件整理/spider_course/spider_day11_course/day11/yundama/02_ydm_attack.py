from selenium import webdriver
from PIL import Image
from ydmapi import get_result

class AttackYdm(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'http://www.yundama.com/'

    # 获取首页截图
    def get_index(self):
        self.browser.get(self.url)
        self.browser.save_screenshot('index.png')

    # 截取验证码图片
    def get_caphe(self):
        xpath_bds = '//*[@id="verifyImg"]'
        # 定位节点 - x y坐标
        location = self.browser.find_element_by_xpath(
                                      xpath_bds).location
        # 获取宽度和高度
        size = self.browser.find_element_by_xpath(
                                      xpath_bds).size
        # 左上角x y 坐标
        left = location['x']
        top = location['y']
        # 右下角x y 坐标
        right = left + size['width']
        bottom = top + size['height']
        # 截取验证码图片(crop()):对图片进行剪切
        img = Image.open('index.png').crop((left,top,right,bottom))
        img.save('yzm.png')

        # 在线打码
        result = get_result('yzm.png')
        print(result)

    def run(self):
        self.get_index()
        self.get_caphe()

if __name__ == '__main__':
    spider = AttackYdm()
    spider.run()

























