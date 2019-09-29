from urllib import request

url = 'http://httpbin.org/get'
res = request.urlopen(url)
print(res.read().decode())