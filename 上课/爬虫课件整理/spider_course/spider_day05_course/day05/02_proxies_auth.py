'''私密代理+独享代理'''
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent':'xxxxxxx'}
proxies = {
    'http':'http://309435365:szayclhp@59.62.164.40:21963',
    'https':'https://309435365:szayclhp@59.62.164.40:21963'
}
html = requests.get(url=url,proxies=proxies,headers=headers).text
print(html)



















