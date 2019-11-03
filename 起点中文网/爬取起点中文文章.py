#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-11-02 15:15
# @Author: Lattesea
# @File: 爬取起点中文文章.py
import requests
import re
from fake_useragent import UserAgent
from fontTools.ttLib import TTFont

ua = UserAgent()
response = requests.get('https://book.qidian.com/info/1015609210', headers={
    'User-Agent': ua.random
})

with open('替换前的网页.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)
html_page = response.text

font_url = re.findall("; src: url\('(.*?)'\) format", response.text)[1]
font_response = requests.get(font_url)
with open('字体文件.woff', mode='wb') as f:
    f.write(font_response.content)

fi = TTFont('字体文件.woff')
fi.saveXML('font.xml')

font_map = fi['cmap'].getBestCmap()
print(font_map)

d = {'zero': 0, 'six': 6, 'seven': 7, 'nine': 9, 'eight': 8, 'period': '.', 'one': 1, 'three': 3, 'four': 4, 'two': 2,
     'five': 5}
for key in font_map:
    font_map[key] = d[font_map[key]]

print(font_map)

for key in font_map:
    html_page = html_page.replace('&#' + str(key) + ';', str(font_map[key]))

with open('替换后的网页.html', mode='w', encoding='utf-8')as f:
    f.write(html_page)
