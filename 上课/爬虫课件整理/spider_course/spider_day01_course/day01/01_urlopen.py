'''向百度发请求,得到响应内容'''
import urllib.request

# res为对象
res = urllib.request.urlopen('http://www.baidu.com/')
# 1. html为字符串(特别长)
# 2. read():bytes   read().decode():string
html = res.read().decode()
# 返回实际数据URL地址
url = res.geturl()
# 返回HTTP响应码
code = res.getcode()
print(url,code)



















