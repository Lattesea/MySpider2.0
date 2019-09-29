import requests

url = 'http://httpbin.org/get'
proxies = {
    'http' : 'http://27.204.112.20:9999',
    'https': 'https://27.204.112.20:9999'
}
html = requests.get(url=url,proxies=proxies,timeout=8).text
print(html)













