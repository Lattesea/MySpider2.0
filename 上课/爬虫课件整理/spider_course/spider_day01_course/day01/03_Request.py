from urllib import request

# 定义常用变量
url = 'http://httpbin.org/get'
headers = {'User-Agent':'xxxxxxxxxxxxxx'}
# 1. 创建请求对象 - 并未真正发请求
req = request.Request(url=url,headers=headers)
# 2. 获取响应对象
res = request.urlopen(req)
# 3. 读取内容
html = res.read().decode()

print(html)



















