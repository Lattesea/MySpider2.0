import requests
from lxml import etree

word = input('请输入要翻译的单词:')
post_url = 'http://m.youdao.com/translate'
data = {
    'inputtext': word,
    'type': 'AUTO',
}
html = requests.post(url=post_url,data=data).text
parse_html = etree.HTML(html)
result = parse_html.xpath(
    '//ul[@id="translateResult"]/li/text()')[0]
print('翻译结果:',result)














