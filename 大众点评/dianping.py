import re
import requests
from lxml import html


# 获取css的全部数据，并且一会通过正则表达式匹配出你想要的class
# css_name 你需要获取的css名称，例如zrvm6
# css_url 'https://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/3b0a424aef56ae40afe7711036173836.css'
# 这个地方是动态的，每次都要重新抓取一下
# .tiimh{background:-456.0px -849.0px;}  编写正则表达式
def get_css_position(css_name, css_url):
    css_positon_html = requests.get(css_url).text

    str_css = (r'%s{background:-(\d+).0px -(\d+).0px' % css_name)
    css_re = re.compile(str_css)
    info_css = css_re.findall(css_positon_html)

    return info_css


result = requests.get(
    'https://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/3e7551c3d26f090c29498db5024b1090.svg')
tree = html.fromstring(result.content)

a = tree.xpath('//text[@y="49"]/text()')[0]
b = tree.xpath('//text[@y="90"]/text()')[0]
c = tree.xpath('//text[@y="140"]/text()')[0]

print(a, b, c)

x, y = get_css_position('zrvm6',
                        'https://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/3b0a424aef56ae40afe7711036173836.css')[
    0]
x, y = int(x), int(y)
print('zrvm6的坐标是', x, y)
if y <= 49:
    print('svg图片对应的数字：', a[x // 12])
elif y <= 90:
    print('svg图片对应的数字：', b[x // 12])
else:
    print('svg图片对应的数字：', c[x // 12])

if __name__ == '__main__':
    a = get_css_position('tiimh','https://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/3b0a424aef56ae40afe7711036173836.css')
    print(a)
