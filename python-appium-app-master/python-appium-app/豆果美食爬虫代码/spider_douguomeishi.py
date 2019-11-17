import requests
import json
#引入了队列
from multiprocessing import Queue
from handel_mongo import mongo_info
#ThreadPoolExecutor包引入线程池
from concurrent.futures import ThreadPoolExecutor


#创建队列
queue_list = Queue()

#封装请求函数,相同的请求头
def handel_request(url,data):
    header = {
        "client":"4",
        "version":"6922.2",
        "device":"MI 6",
        "sdk":"19,4.4.2",
        "imei":"863254010448503",
        "channel":"qqkp",
        # "mac":"44:85:00:5E:5B:28",
        "resolution":"720*1280",
        "dpi":"1.5",
        # "android-id":"4485005e5b281516",
        # "pseudo-id":"05e5b28151644850",
        "brand":"Xiaomi",
        "scale":"1.5",
        "timezone":"28800",
        "language":"zh",
        "cns":"3",
        "carrier":"CMCC",
        # "imsi":"460074485009491",
        "user-agent":"Mozilla/5.0 (Linux; Android 4.4.2; MI 6  Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
        "reach":"1",
        "newbie":"1",
        # "lon":"116.568176",
        # "lat":"26.997867",
        # "cid":"361000",
        "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"Keep-Alive",
        # "Cookie":"duid=57158696",
        "Host":"api.douguo.net",
        # "Content-Length":"68",
    }

    #设置的代理Ip
    proxy = {'http': 'http://H211EATS9O5745KC:F8FFBC929EB7D5A7@http-cla.abuyun.com:9030'}
    #请求函数构造好了
    response = requests.post(url=url,headers=header,data=data,proxies=proxy)
    return response

#菜谱分类页面
def handle_index():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        "client": "4",
        # "_session": "1537295931652863254010448503",
        # "v": "1503650468",
        "_vs": "2305",
    }

    response = handel_request(url=url,data=data)
    index_response_dict = json.loads(response.text)
    for index_item in index_response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for item in index_item_1['cs']:
                data_2 = {
                    "client": "4",
                    # "_session": "1537295931652863254010448503",
                    "keyword": item['name'],
                    "order": "3",
                    "_vs": "400",
                }
                #放到队列内部,put方法，向队里内部放数据
                queue_list.put(data_2)

#线程的处理函数,把队列里面的data get出来
#请求的是菜谱的列表页和详情页
def handle_caipu_list(data):
    print('当前处理的食材: ',data['keyword'])
    caipu_list_url = 'http://api.douguo.net/recipe/v2/search/0/20'
    #第一次请求
    caipu_list_response = handel_request(url=caipu_list_url,data=data)
    caipu_list_response_dict = json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict['result']['list']:
        caipu_info = {}
        caipu_info['shicai'] = data['keyword']
        if item['type'] == 13:
            caipu_info['user_name'] = item['r']['an']
            caipu_info['shicai_id'] = item['r']['id']
            caipu_info['describe'] = item['r']['cookstory'].replace('\n','').replace(' ','')
            caipu_info['caipu_name'] = item['r']['n']
            caipu_info['zuoliao_list'] = item['r']['major']
            detail_url = 'http://api.douguo.net/recipe/detail/'+str(caipu_info['shicai_id'])
            detail_data = {
                "client": "4",
                # "_session": "1537295931652863254010448503",
                "author_id": "0",
                "_vs": "2803",
                "_ext": '{"query":{"id":'+str(caipu_info['shicai_id'])+',"kw":'+caipu_info['shicai'] +',"idx":"4","src":"2803","type":"13"}}',
            }
            #第二次请求
            detail_response = handel_request(url=detail_url,data=detail_data)
            detail_response_dict = json.loads(detail_response.text)
            caipu_info['tips'] = detail_response_dict['result']['recipe']['tips']
            caipu_info['cook_step'] = detail_response_dict['result']['recipe']['cookstep']
            print('当前入库的菜谱是: ',caipu_info['caipu_name'])
            #mongdb当中去
            mongo_info.insert_item(caipu_info)
        else:
            continue

handle_index()
#实现多线程抓取，引入了线程池
pool = ThreadPoolExecutor(max_workers=2)
while queue_list.qsize() > 0:
    pool.submit(handle_caipu_list,queue_list.get())
