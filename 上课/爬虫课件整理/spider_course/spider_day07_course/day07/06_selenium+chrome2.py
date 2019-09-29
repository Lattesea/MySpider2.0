from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# 1.在搜索框输入赵丽颖   //*[@id="kw"]
kw_input = browser.find_element_by_id("kw")
kw_input.send_keys('赵丽颖')
# 2.点击按钮 百度一下   //*[@id="su"]
su_button = browser.find_element_by_xpath('//*[@id="su"]')
su_button.click()
browser.save_screenshot('girl.png')

























