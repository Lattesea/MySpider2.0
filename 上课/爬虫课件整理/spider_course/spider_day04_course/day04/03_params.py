import requests

baseurl = 'http://tieba.baidu.com/f?'
params = {
    'kw':'金喜善吧',
    'pn':'50'
}
headers = {'User-Agent':'Mozilla/5.0'}

res = requests.get(url=baseurl,params=params,headers=headers)
res.encoding = 'utf-8'
print(res.text)
























