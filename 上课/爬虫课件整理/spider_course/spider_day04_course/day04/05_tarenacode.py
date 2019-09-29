import requests

url = 'http://code.tarena.com.cn/AIDCode/aid1905/13_redis/'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url=url,headers=headers).text

print(html)


















