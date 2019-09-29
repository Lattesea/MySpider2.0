from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains

# 1.打开浏览器+输入百度url+找到设置节点
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
set_node=browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
# 2.鼠标移动到 设置 节点
ActionChains(browser).move_to_element(set_node).perform()
# 3.找 高级搜索 节点,并点击
browser.find_element_by_link_text('高级搜索').click()





















