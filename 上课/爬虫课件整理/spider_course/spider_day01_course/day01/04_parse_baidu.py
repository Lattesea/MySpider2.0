from urllib import request
from urllib import parse
import time

# 1. 拼接URL地址函数
def get_url(word):
    baseurl = 'http://www.baidu.com/s?'
    # 编码 + 拼接
    params = parse.urlencode({'wd':word})
    url = baseurl + params

    return url

# 2. 请求+保存
def write_html(url,word):
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    # 拿到响应内容
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    # 保存到本地文件
    filename = word + '.html'
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

# 主程序入口
if __name__ == '__main__':
    word = input('请输入要搜索的内容:')
    url = get_url(word)
    while True:
        try:
            write_html(url,word)
            break
        except Exception as e:
            time.sleep(0.5)


# ConnectionReset error [errno 104] : 远程主机......


















