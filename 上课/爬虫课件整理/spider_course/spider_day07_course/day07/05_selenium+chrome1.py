# 导入selenium的webdriver接口
from selenium import webdriver
import time

# 1. 创建浏览器对象 - 打开浏览器
browser = webdriver.Chrome()
# 2. 地址栏输入 百度地址
browser.get('http://www.baidu.com/')

print(browser.page_source.find('ssssssssssssss'))




# 获取快照
browser.save_screenshot('baidu.png')
# 3. 停留5秒钟
time.sleep(5)
# 4. 关闭浏览器
browser.quit()




















