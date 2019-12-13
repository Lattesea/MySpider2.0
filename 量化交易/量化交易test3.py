from selenium import webdriver
import time
import re
browser = webdriver.Chrome()
browser.get('https://cn.tradingview.com/')
search = browser.find_element_by_xpath("/body[@class='search-page index-page']/div[@class='tv-main']/div[@class='tv-header']/div[@class='tv-header__inner tv-layout-width']/div[@class='tv-header__area tv-header__area--middle']/form[@class='tv-header-search js-header-search']/label[@class='tv-header-search__inputwrap']/tv-autocomplete/input[@class='tv-header-search__input js-header-search__input']")
time.sleep(5)
search.send_keys('XAUUSD')
test='jdasjdia'
test.replace()