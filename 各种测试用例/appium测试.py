# 导入appium模块
from appium import webdriver
# 等待元素控件
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['udid'] = '127.0.0.1:62001'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'
desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True  #

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

