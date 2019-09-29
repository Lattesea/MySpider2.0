'''API接口: 获取100个IP,只留下可用的'''
import requests

# 对每个IP做测试,保存可用的IP
def test_ip(ip_list):
    for ip in ip_list:
        proxies = {
            'http':'http://{}'.format(ip),
            'https':'https://{}'.format(ip)
        }
        test_url = 'http://www.baidu.com/'
        try:
            res = requests.get(
                url=test_url,proxies=proxies,timeout=5
            )
            print(ip,'Success')
            with open('proxies.txt','a') as f:
                f.write(ip + '\n')
        except Exception as e:
            print(ip,'Failed')

def get_proxy_ip():
    url = 'http://dev.kdlapi.com/api/getproxy/?' \
          'orderid=996823237536048&num=100&protocol=2' \
          '&method=2&an_an=1&an_ha=1&sep=1'
    # html: '1.1.1.1:8888\r\n2.2.2.2:8888\r\n
    html = requests.get(
        url=url,
        headers={'User-Agent':'Mozilla/5.0'}
    ).text
    # ip_list: ['1.1.1.1:8888','2.2.2.2:8888','']
    ip_list = html.split('\r\n')
    test_ip(ip_list)



if __name__ == '__main__':
    get_proxy_ip()




































