# 非结构化数据抓取
from urllib import request

url = 'https://p0.meituan.net/movie/128eb7fc53c82a383ee6d466b2beacdc113707.jpg@465w_258h_1e_1c'
res = request.urlopen(url)
html = res.read()

with open('无间道.jpg','wb') as f:
    f.write(html)

# 2. os模块使用
import os

directory = '/home/tarena/spider/day03'
if not os.path.exists(directory):
    os.makedirs(directory)







