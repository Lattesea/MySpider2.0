#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-10-24 23:28
# @Author: Lattesea
# @File: 爬取微信公众号test2.py
from airtest.core.api import auto_setup
import time
import requests

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

requests.adapters.DEFAULT_RETRIES = 1

s = requests.session()

s.keep_alive = False

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="微信").click()
poco(text="订阅号消息").click()
poco(desc="订阅号").click()
poco(text="电脑爱好者 @").click()
poco(name="android.support.v7.widget.LinearLayoutCompat").click()
poco(name="com.tencent.mm:id/b6h").click()
print(poco(name="activity-name").get_text())
time.sleep(3)
# print(poco(name="js_content").get_text())
poco(name="js_content")
message_obj = poco("js_content").offspring("android.view.View")
for i in message_obj:
    print(i.get_text())
time.sleep(2)
poco(name="readNum3")
time.sleep(2)
print(poco(name="readNum3").get_text())
print(poco(name="js_like_btn").get_text())
