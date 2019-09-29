import requests

url = 'http://s9.rr.itc.cn/r/wapChange/20167_19_19/a1i42m7685213345628.jpg'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url=url,headers=headers).content
with open('花千骨.jpg','wb') as f:
    f.write(html)
























