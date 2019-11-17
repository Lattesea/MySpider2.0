#需要安装客户端的包
#pip3 install Appium-Python-Client
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


cap = {
  "platformName": "Android",
  "platformVersion": "4.4.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",cap)

def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return(x,y)

try:
    #是否跳过
    if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
except:
    pass
try:
    if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys("dazhuang123")
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys("qwe123asd")
        driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except:
    pass


try:
    #隐私协议
    if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_title']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_agree']").click()
        driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]").click()
except:
    pass

#点击研讯
if WebDriverWait(driver,3).until(lambda x:x.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")):
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()

    l = get_size()

    x1 = int(l[0]*0.5)
    y1 = int(l[1]*0.75)
    y2 = int(l[1]*0.25)

    #滑动操作
    while True:
        driver.swipe(x1,y1,x1,y2)
        time.sleep(0.5)


