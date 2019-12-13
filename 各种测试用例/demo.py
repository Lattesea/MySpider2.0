# * Coding:UTF-8 *
# *__Author:LiuXin
# *__Date:2019/12/3 14:43


import time
import json
import requests
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from fake_useragent import UserAgent

class Login():

    ##获取信息
    def get_info(self):
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = Chrome(options=option)
        url = 'https://mobile.yangkeduo.com/login.html'
        driver.get(url)
        driver.find_element_by_class_name('phone-login').click()
        time.sleep(1)
        driver.find_element_by_id('user-mobile').send_keys('18998261232')
        time.sleep(1)
        send_msg_js = """document.getElementById('code-button').click()"""
        driver.execute_script(send_msg_js)
        driver.find_element_by_id('input-code').send_keys(input('请输入验证码：'))
        driver.find_element_by_id('submit-button').click()
        time.sleep(2)
        ## 获取登录的url
        self.login_url = driver.current_url
        ## 获取cookie
        jsonCookie = driver.get_cookies()
        driver.quit()
        with open('jsonCookie.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(jsonCookie))

    ## 模拟登录
    def get_login(self):
        user_agent = UserAgent().random
        with open('jsonCookie.json', 'r', encoding='utf-8') as f:
            cookies = json.loads(f.read())
        cookie = [item['name'] + '=' + item['value'] for item in cookies]
        cookiestr = ';'.join(item for item in cookie)
        headers = {'user_agent': user_agent,
                   'cookie': cookiestr}
        html = requests.get(url=self.login_url, headers=headers).text
        time.sleep(2)
        print(html)

if __name__ == '__main__':
    login = Login()
    login.get_info()
    login.get_login()


