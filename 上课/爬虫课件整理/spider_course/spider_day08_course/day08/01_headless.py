from selenium import webdriver

# 设置无界面
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 创建浏览器对象
browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.png')






























