'''iframe'''
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://mail.qq.com/')
# 1. 切换到iframe子框架
login_iframe = browser.find_element_by_id('login_frame')
browser.switch_to.frame(login_iframe)
# 2. 找节点: 用户名+密码+登录按钮
user = browser.find_element_by_id('u').send_keys('2621470058')
pwd = browser.find_element_by_id('p').send_keys('zhanshen001')
login = browser.find_element_by_id('login_button').click()































