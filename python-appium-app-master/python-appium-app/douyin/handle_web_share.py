import re
import requests
import time
from lxml import etree
from handle_mongo import save_data
from handle_mongo import get_task



def handle_decode(input_data,share_web_url,task):
    search_douyin_str = re.compile(r'抖音ID：')
    regex_list = [
        {'name':[' &#xe603; ',' &#xe60d; ',' &#xe616; '],'value':0},
        {'name':[' &#xe602; ',' &#xe60e; ',' &#xe618; '],'value':1},
        {'name':[' &#xe605; ',' &#xe610; ',' &#xe617; '],'value':2},
        {'name':[' &#xe604; ',' &#xe611; ',' &#xe61a; '],'value':3},
        {'name':[' &#xe606; ',' &#xe60c; ',' &#xe619; '],'value':4},
        {'name':[' &#xe607; ',' &#xe60f; ',' &#xe61b; '],'value':5},
        {'name':[' &#xe608; ',' &#xe612; ',' &#xe61f; '],'value':6},
        {'name':[' &#xe60a; ',' &#xe613; ',' &#xe61c; '],'value':7},
        {'name':[' &#xe60b; ',' &#xe614; ',' &#xe61d; '],'value':8},
        {'name':[' &#xe609; ',' &#xe615; ',' &#xe61e; '],'value':9},
    ]

    for i1 in regex_list:
        for i2 in i1['name']:
            input_data = re.sub(i2,str(i1['value']),input_data)
    share_web_html = etree.HTML(input_data)
    douyin_info = {}
    douyin_info['nick_name'] = share_web_html.xpath("//div[@class='personal-card']/div[@class='info1']//p[@class='nickname']/text()")[0]
    if 'douyin_id' in task:
        douyin_info['douyin_id'] = task['douyin_id']
    else:
        douyin_id = ''.join(share_web_html.xpath("//div[@class='personal-card']/div[@class='info1']/p[@class='shortid']/i/text()"))
        if douyin_id == '':
            try:
                douyin_info['douyin_id'] = re.sub(search_douyin_str,'',share_web_html.xpath("//div[@class='personal-card']/div[@class='info1']/p[@class='shortid']/text()")[0]).strip()
            except:
                douyin_info['douyin_id'] = '无数据'
        else:
            douyin_info['douyin_id'] = douyin_id

    try:
        douyin_info['job'] = share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/div[@class='verify-info']/span[@class='info']/text()")[0].strip()
    except:
        pass
    douyin_info['describe'] = share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='signature']/text()")[0].replace('\n',',')
    douyin_info['location'] = share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='extra-info']/span[1]/text()")[0]
    douyin_info['xingzuo'] = share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='extra-info']/span[2]/text()")[0]
    douyin_info['follow_count'] = share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='focus block']//i[@class='icon iconfont follow-num']/text()")[0].strip()
    fans_value = ''.join(share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']//i[@class='icon iconfont follow-num']/text()"))
    unit = share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='follower block']/span[@class='num']/text()")
    if unit[-1].strip() == 'w':
        douyin_info['fans'] = str((int(fans_value)/10))+'w'
    like = ''.join(share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']//i[@class='icon iconfont follow-num']/text()"))
    unit = share_web_html.xpath("//div[@class='personal-card']/div[@class='info2']/p[@class='follow-info']//span[@class='liked-num block']/span[@class='num']/text()")
    if unit[-1].strip() == 'w':
        douyin_info['like'] = str(int(like)/10)+'w'
    douyin_info['from_url'] = share_web_url
    save_data(douyin_info)

def handle_douyin_web_share(task):
    share_web_url = 'https://www.douyin.com/share/user/'+task['share_id']
    print(share_web_url)
    share_web_header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    share_web_response = requests.get(url=share_web_url,headers=share_web_header)
    handle_decode(share_web_response.text,share_web_url,task)

if __name__ == '__main__':
    while True:
        task = get_task('share_id')
        if task == None:
            print('当前处理task为:%s'%task)
            break
        else:
            print('当前处理task为:%s'%task)
            handle_douyin_web_share(task)
        time.sleep(2)
