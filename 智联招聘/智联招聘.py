import requests
from lxml import etree
import csv, re, random, time
import json
from selenium import webdriver
from time import sleep
# 引入了队列
from multiprocessing import Queue
# ThreadPoolExecutor包引入线程池
from concurrent.futures import ThreadPoolExecutor


# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#解决编译出现的问题


def get_headers(url):
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    ]

    cookies = [
        'sts_deviceid=1684b54d5ea3e3-0e7ad211909fc7-58422116-1327104-1684b54d5eb52a; zg_did=%7B%22did%22%3A%20%22168595e05b724b-0a26618d2b558d-58422116-144000-168595e05b8704%22%7D; NTKF_T2D_CLIENTID=guest8C2EB479-D44D-8FA1-6B8E-5970838A036E; bdshare_firstime=1547705692606; __xsptplus30=30.5.1548219589.1548219589.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23HVC5LOPl04lSJcNWYqqVzmyrvm0u1fV_%23; _jzqa=1.2768125421918309000.1548060025.1548212714.1548219590.5; dywem=95841923.y; Hm_lvt_80e552e101e24fe607597e5f45c8d2a2=1553652323,1553652367,1553652541,1553652557; x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2; adfbid2=0; sou_experiment=unexperiment; ZP_OLD_FLAG=false; acw_tc=2760828415681742889036941e22998841053263fb415433ea89802292b999; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; dywec=95841923; dywez=95841923.1568443824.4.3.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utmc=269921210; __utmz=269921210.1568443825.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568174169,1568423072,1568443825; sts_sg=1; sts_sid=16d2e897dcf3c1-0152d8b5b50ae8-5373e62-1327104-16d2e897dd034c; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoEMIiwvKQthah21mu5AXBsi40vy4WQHM8sM53NxIi9PXXgIgzmGYD8W5TCDHqL-Q%26ck%3D4553.2.111.387.146.415.242.240%26shh%3Dwww.baidu.com%26sht%3D06074089_18_pg%26wd%3D%26eqid%3Dd113a7dd003de52f000000035d7c8df2; jobRiskWarning=true; POSSPORTLOGIN=5; CANCELALL=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22%24device_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dywea=95841923.37350777197861720.1568174169.1568443824.1568446729.5; __utma=269921210.1664687181.1568174169.1568443825.1568446729.4; dyweb=95841923.2.10.1568446729; __utmb=269921210.2.10.1568446729; acw_sc__v2=5d7c9a16e57b280b8aa347e4e4015d54c5b4e81b; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%222ec760b1-91e0-45a8-977d-e59bcc5863c9-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22company%22:{%22actionid%22:%22eefb64ff-22ff-47db-aa6e-e43350f78847-company%22%2C%22funczone%22:%22hiring_jd%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22fc270696-aebe-4029-ac78-401bb3ec0ee7-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}%2C%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%2202882013-cafb-4d17-b9c1-f6f94486a481-cityPage%22}}; LastCity=%E5%8D%97%E4%BA%AC; LastCity%5Fid=635; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568446965; sts_evtseq=47',
        'sts_deviceid=1684b54d5ea3e3-0e7ad211909fc7-58422116-1327104-1684b54d5eb52a; zg_did=%7B%22did%22%3A%20%22168595e05b724b-0a26618d2b558d-58422116-144000-168595e05b8704%22%7D; NTKF_T2D_CLIENTID=guest8C2EB479-D44D-8FA1-6B8E-5970838A036E; bdshare_firstime=1547705692606; __xsptplus30=30.5.1548219589.1548219589.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23HVC5LOPl04lSJcNWYqqVzmyrvm0u1fV_%23; _jzqa=1.2768125421918309000.1548060025.1548212714.1548219590.5; dywem=95841923.y; Hm_lvt_80e552e101e24fe607597e5f45c8d2a2=1553652323,1553652367,1553652541,1553652557; x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2; adfbid2=0; sou_experiment=unexperiment; ZP_OLD_FLAG=false; acw_tc=2760828415681742889036941e22998841053263fb415433ea89802292b999; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; dywec=95841923; dywez=95841923.1568443824.4.3.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utmc=269921210; __utmz=269921210.1568443825.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568174169,1568423072,1568443825; sts_sg=1; sts_sid=16d2e897dcf3c1-0152d8b5b50ae8-5373e62-1327104-16d2e897dd034c; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoEMIiwvKQthah21mu5AXBsi40vy4WQHM8sM53NxIi9PXXgIgzmGYD8W5TCDHqL-Q%26ck%3D4553.2.111.387.146.415.242.240%26shh%3Dwww.baidu.com%26sht%3D06074089_18_pg%26wd%3D%26eqid%3Dd113a7dd003de52f000000035d7c8df2; jobRiskWarning=true; POSSPORTLOGIN=5; CANCELALL=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22%24device_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dywea=95841923.37350777197861720.1568174169.1568443824.1568446729.5; __utma=269921210.1664687181.1568174169.1568443825.1568446729.4; dyweb=95841923.2.10.1568446729; __utmb=269921210.2.10.1568446729; acw_sc__v2=5d7c9a16e57b280b8aa347e4e4015d54c5b4e81b; LastCity=%E5%8D%97%E4%BA%AC; LastCity%5Fid=635; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568446965; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%222ec760b1-91e0-45a8-977d-e59bcc5863c9-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22company%22:{%22actionid%22:%22eefb64ff-22ff-47db-aa6e-e43350f78847-company%22%2C%22funczone%22:%22hiring_jd%22}%2C%22jobs%22:{%22recommandActionidShare%22:%226d62c4ef-2b03-4f5f-910a-47a2eca6eb15-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}%2C%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%2202882013-cafb-4d17-b9c1-f6f94486a481-cityPage%22}}; sts_evtseq=54',
        'sts_deviceid=1684b54d5ea3e3-0e7ad211909fc7-58422116-1327104-1684b54d5eb52a; zg_did=%7B%22did%22%3A%20%22168595e05b724b-0a26618d2b558d-58422116-144000-168595e05b8704%22%7D; NTKF_T2D_CLIENTID=guest8C2EB479-D44D-8FA1-6B8E-5970838A036E; __xsptplus30=30.5.1548219589.1548219589.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23HVC5LOPl04lSJcNWYqqVzmyrvm0u1fV_%23; _jzqa=1.2768125421918309000.1548060025.1548212714.1548219590.5; dywem=95841923.y; x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2; adfbid2=0; sou_experiment=unexperiment; acw_tc=2760822715681742461203848e0e34ceca1f40d99cdd28e9fd7e5da9f7b89d; ZP_OLD_FLAG=false; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; dywec=95841923; dywez=95841923.1568443824.4.3.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utmc=269921210; __utmz=269921210.1568443825.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568174169,1568423072,1568443825; sts_sg=1; sts_sid=16d2e897dcf3c1-0152d8b5b50ae8-5373e62-1327104-16d2e897dd034c; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoEMIiwvKQthah21mu5AXBsi40vy4WQHM8sM53NxIi9PXXgIgzmGYD8W5TCDHqL-Q%26ck%3D4553.2.111.387.146.415.242.240%26shh%3Dwww.baidu.com%26sht%3D06074089_18_pg%26wd%3D%26eqid%3Dd113a7dd003de52f000000035d7c8df2; jobRiskWarning=true; POSSPORTLOGIN=5; CANCELALL=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22%24device_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dywea=95841923.37350777197861720.1568174169.1568443824.1568446729.5; __utma=269921210.1664687181.1568174169.1568443825.1568446729.4; dyweb=95841923.3.10.1568446729; __utmt=1; __utmb=269921210.3.10.1568446729; LastCity=%E8%8B%8F%E5%B7%9E; LastCity%5Fid=639; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22b2ac879a-fda6-4223-92a8-05040f544ffb-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22company%22:{%22actionid%22:%22eefb64ff-22ff-47db-aa6e-e43350f78847-company%22%2C%22funczone%22:%22hiring_jd%22}%2C%22jobs%22:{%22recommandActionidShare%22:%220873bde8-03b5-4bed-9458-d679e1414068-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}%2C%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%221b085184-022b-46e1-a387-b44b57f294ab-cityPage%22}}; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568448460; sts_evtseq=66'
    ]
    headers = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        "Cache-Control": 'max-age=0',
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": 'zh-CN,zh;q=0.9',
        "Connection": 'keep-alive',
        "Upgrade-Insecure-Requests": '1',
        "Referer": 'https://sou.zhaopin.com/?jl=635&kw=%E8%B4%A8%E9%87%8F&kt=3&sf=0&st=0',
        "User-Agent": random.choice(agents),
        "Cookie": random.choice(cookies)
    }

    # time.sleep(random.random())
    try:
        res = requests.get(url, headers=headers)
        res.encoding = res.apparent_encoding
        # res.encoding = 'gb2312'
        # print(res.text)
        # time.sleep(3)
        print(res.status_code)
        # html = etree.HTML(res.text)
        return res.text
    except:
        print('打开不了网址...')


def get_headers2(url):
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    ]

    cookies = [
        "sts_deviceid=1684b54d5ea3e3-0e7ad211909fc7-58422116-1327104-1684b54d5eb52a; zg_did=%7B%22did%22%3A%20%22168595e05b724b-0a26618d2b558d-58422116-144000-168595e05b8704%22%7D; NTKF_T2D_CLIENTID=guest8C2EB479-D44D-8FA1-6B8E-5970838A036E; bdshare_firstime=1547705692606; __xsptplus30=30.5.1548219589.1548219589.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23HVC5LOPl04lSJcNWYqqVzmyrvm0u1fV_%23; _jzqa=1.2768125421918309000.1548060025.1548212714.1548219590.5; dywem=95841923.y; Hm_lvt_80e552e101e24fe607597e5f45c8d2a2=1553652323,1553652367,1553652541,1553652557; x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2; adfbid2=0; sou_experiment=unexperiment; ZP_OLD_FLAG=false; acw_tc=2760828415681742889036941e22998841053263fb415433ea89802292b999; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; dywec=95841923; dywez=95841923.1568443824.4.3.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utmc=269921210; __utmz=269921210.1568443825.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568174169,1568423072,1568443825; sts_sg=1; sts_sid=16d2e897dcf3c1-0152d8b5b50ae8-5373e62-1327104-16d2e897dd034c; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoEMIiwvKQthah21mu5AXBsi40vy4WQHM8sM53NxIi9PXXgIgzmGYD8W5TCDHqL-Q%26ck%3D4553.2.111.387.146.415.242.240%26shh%3Dwww.baidu.com%26sht%3D06074089_18_pg%26wd%3D%26eqid%3Dd113a7dd003de52f000000035d7c8df2; jobRiskWarning=true; POSSPORTLOGIN=5; CANCELALL=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22%24device_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; __utma=269921210.1664687181.1568174169.1568446729.1568452266.5; dywea=95841923.37350777197861720.1568174169.1568446729.1568452266.6; LastCity=%E8%8B%8F%E5%B7%9E; LastCity%5Fid=639; acw_sc__v2=5d7cd37a58320c461aff1dd0d9e79533010672c3; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%225772fdb7-116e-445f-ba34-78ccf51c5c76-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22company%22:{%22actionid%22:%22eefb64ff-22ff-47db-aa6e-e43350f78847-company%22%2C%22funczone%22:%22hiring_jd%22}%2C%22jobs%22:{%22recommandActionidShare%22:%2287f70323-2bec-47ee-ac90-18fcf6e24dd9-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}%2C%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%221ec9f19b-9cce-417b-b121-3cffc815b7d5-cityPage%22}}; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568462633; sts_evtseq=685",
        "sts_deviceid=1684b54d5ea3e3-0e7ad211909fc7-58422116-1327104-1684b54d5eb52a; zg_did=%7B%22did%22%3A%20%22168595e05b724b-0a26618d2b558d-58422116-144000-168595e05b8704%22%7D; NTKF_T2D_CLIENTID=guest8C2EB479-D44D-8FA1-6B8E-5970838A036E; bdshare_firstime=1547705692606; __xsptplus30=30.5.1548219589.1548219589.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23HVC5LOPl04lSJcNWYqqVzmyrvm0u1fV_%23; _jzqa=1.2768125421918309000.1548060025.1548212714.1548219590.5; dywem=95841923.y; Hm_lvt_80e552e101e24fe607597e5f45c8d2a2=1553652323,1553652367,1553652541,1553652557; x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2; adfbid2=0; sou_experiment=unexperiment; ZP_OLD_FLAG=false; acw_tc=2760828415681742889036941e22998841053263fb415433ea89802292b999; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; dywec=95841923; dywez=95841923.1568443824.4.3.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utmc=269921210; __utmz=269921210.1568443825.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568174169,1568423072,1568443825; sts_sg=1; sts_sid=16d2e897dcf3c1-0152d8b5b50ae8-5373e62-1327104-16d2e897dd034c; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoEMIiwvKQthah21mu5AXBsi40vy4WQHM8sM53NxIi9PXXgIgzmGYD8W5TCDHqL-Q%26ck%3D4553.2.111.387.146.415.242.240%26shh%3Dwww.baidu.com%26sht%3D06074089_18_pg%26wd%3D%26eqid%3Dd113a7dd003de52f000000035d7c8df2; jobRiskWarning=true; POSSPORTLOGIN=5; CANCELALL=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22%24device_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; __utma=269921210.1664687181.1568174169.1568446729.1568452266.5; dywea=95841923.37350777197861720.1568174169.1568446729.1568452266.6; LastCity=%E8%8B%8F%E5%B7%9E; LastCity%5Fid=639; acw_sc__v2=5d7cd37a58320c461aff1dd0d9e79533010672c3; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568462633; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%225772fdb7-116e-445f-ba34-78ccf51c5c76-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22company%22:{%22actionid%22:%22eefb64ff-22ff-47db-aa6e-e43350f78847-company%22%2C%22funczone%22:%22hiring_jd%22}%2C%22jobs%22:{%22recommandActionidShare%22:%22490e5d8a-6df5-4ebe-b7f5-ac3fb232bdb5-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}%2C%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%221ec9f19b-9cce-417b-b121-3cffc815b7d5-cityPage%22}}; sts_evtseq=687",
        "sts_deviceid=1684b54d5ea3e3-0e7ad211909fc7-58422116-1327104-1684b54d5eb52a; zg_did=%7B%22did%22%3A%20%22168595e05b724b-0a26618d2b558d-58422116-144000-168595e05b8704%22%7D; NTKF_T2D_CLIENTID=guest8C2EB479-D44D-8FA1-6B8E-5970838A036E; bdshare_firstime=1547705692606; __xsptplus30=30.5.1548219589.1548219589.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23HVC5LOPl04lSJcNWYqqVzmyrvm0u1fV_%23; _jzqa=1.2768125421918309000.1548060025.1548212714.1548219590.5; dywem=95841923.y; Hm_lvt_80e552e101e24fe607597e5f45c8d2a2=1553652323,1553652367,1553652541,1553652557; x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2; adfbid2=0; sou_experiment=unexperiment; ZP_OLD_FLAG=false; acw_tc=2760828415681742889036941e22998841053263fb415433ea89802292b999; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; dywec=95841923; dywez=95841923.1568443824.4.3.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utmc=269921210; __utmz=269921210.1568443825.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1568174169,1568423072,1568443825; sts_sg=1; sts_sid=16d2e897dcf3c1-0152d8b5b50ae8-5373e62-1327104-16d2e897dd034c; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DoEMIiwvKQthah21mu5AXBsi40vy4WQHM8sM53NxIi9PXXgIgzmGYD8W5TCDHqL-Q%26ck%3D4553.2.111.387.146.415.242.240%26shh%3Dwww.baidu.com%26sht%3D06074089_18_pg%26wd%3D%26eqid%3Dd113a7dd003de52f000000035d7c8df2; jobRiskWarning=true; POSSPORTLOGIN=5; CANCELALL=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22%24device_id%22%3A%2216d1e76d8e01d3-0ae941b19d979f-5373e62-1327104-16d1e76d8e168e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; __utma=269921210.1664687181.1568174169.1568446729.1568452266.5; dywea=95841923.37350777197861720.1568174169.1568446729.1568452266.6; LastCity=%E8%8B%8F%E5%B7%9E; LastCity%5Fid=639; acw_sc__v2=5d7cd37a58320c461aff1dd0d9e79533010672c3; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1568462633; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%225772fdb7-116e-445f-ba34-78ccf51c5c76-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22company%22:{%22actionid%22:%22eefb64ff-22ff-47db-aa6e-e43350f78847-company%22%2C%22funczone%22:%22hiring_jd%22}%2C%22jobs%22:{%22recommandActionidShare%22:%222e4541e5-e4ae-4896-bf62-f845185d4496-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}%2C%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%221ec9f19b-9cce-417b-b121-3cffc815b7d5-cityPage%22}}; sts_evtseq=689"
    ]
    headers = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        "Cache-Control": 'max-age=0',
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": 'zh-CN,zh;q=0.9',
        "Connection": 'keep-alive',
        "Upgrade-Insecure-Requests": '1',
        "sec-fetch-mode": 'navigate',
        "sec-fetch-site": 'none',
        "sec-fetch-user": '?1',
        "Referer": 'https://sou.zhaopin.com/?jl=639&kw=%E8%B4%A8%E9%87%8F&kt=3',
        "User-Agent": random.choice(agents),
        "Cookie": random.choice(cookies)

    }

    # time.sleep(random.random())
    try:
        res = requests.get(url, headers=headers)
        res.encoding = res.apparent_encoding
        # res.encoding = 'gb2312'
        # print(res.text)
        # time.sleep(3)
        print(res.status_code)
        # html = etree.HTML(res.text)
        return res.text
    except:
        print('打开不了网址...')


# 存储产品的地址
def save_url(data2):
    print('正在将产品地址数据存进文件...')
    with open("各个公司产品的url.csv", "a", newline='', encoding="utf-8") as f:
        fieldnames = ['company', 'product_name', 'product_url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data2)
        print("OK")


# 获得所有得Url
def all_url(url, href):
    # page = all_page(url)
    for i2 in range(1, 13):
        i = (i2 - 1) * 90
        url2 = href.format(i)
        data2 = {
            "url": url2,
            "num": str(i2),
        }
        get_data2(data2)
        # queue_list.put(data2)


def get_data2(data2):
    url2 = data2["url"]
    i = data2['num']
    print('正在爬取第%s页的数据' % i, url2)
    try:
        res_dict = json.loads(get_headers(url2))
        # print(res_dict)
        results2 = res_dict['data']['results']
        print(len(results2))

        for results in results2:
            company = results['company']  # 公司信息全部
            # print(company)
            company_name = company['name']
            company_type = company['type']['name']
            # print(company_type)
            company_size = company['size']['name']
            # print(company_size)

            city = results['city']['display']
            # print(city)
            updateDate = results['updateDate']
            # print(updateDate)
            salary = results['salary']
            # print(salary)
            eduLevel = results['eduLevel']['name']  # 学历
            # print(eduLevel)
            workingExp = results['workingExp']['name']  # 经验要求
            # print(workingExp)
            positionURL = results['positionURL']  # 地址
            # print(positionURL)
            welfare = results['welfare']  # 亮点
            # print(type(welfare))
            keys = ['jobName', 'company_name', 'company_type', 'company_size', "city", "updateDate", "salary",
                    "eduLevel", 'workingExp', "welfare", "url", "people", "dult"]
            data2 = {
                'jobName': results['jobName'],
                'company_name': company_name,
                'company_type': company_type,
                'company_size': company_size,
                "city": city,
                "updateDate": updateDate,
                "salary": salary,
                "eduLevel": eduLevel,
                'workingExp': workingExp,
                "welfare": welfare,
                "url": positionURL
            }
            print(data2)
            d = {
                "keys": keys,
                "values": data2
            }
            # get_data(d)
            # save_field(d)
            queue_list.put(d)
    except:
        pass


# 获取企业基本信息
def get_data(data):
    url = data["values"]["url"]
    data3 = data["values"]
    keys = data["keys"]
    i = 1

    html = etree.HTML(get_headers2(url))
    # print(html)
    try:
        people2 = ''.join(html.xpath('//ul[@class="summary-plane__info"]/li[4]/text()')).strip()
        people = re.findall(r'^招(.*?)人', people2)[0]
        print(people)
        if people:
            pass
        else:
            people = '-'
        dults = html.xpath('//div[@class="describtion"]//text()')
        data3["people"] = people
        data3["dult"] = dults
        print(dults)
    except:
        pass
    finally:
        d = {
            "keys": keys,
            "values": data3
        }
        save_field(d)


# 存储信息
def save_field(data3):
    # 存储数据
    print('正在将数据存进文件...')
    with open("苏州.csv", "a", newline='', encoding="utf-8") as f:
        fieldnames = data3['keys']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data3["values"])
        print("OK...")
    # broswer.quit()


if __name__ == '__main__':
    # 创建队列
    queue_list = Queue()
    # get_area()
    # get_headers(url)
    url = 'https://fe-api.zhaopin.com/c/i/sou?start=0&pageSize=90&cityId=635&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%B4%A8%E9%87%8F&kt=3&_v=0.55074657&x-zp-page-request-id=c571ce9dcc9b48bca2ffeee1886e10cb-1568443952098-942185&x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2'
    href = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=639&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%B4%A8%E9%87%8F&kt=3&_v=0.35595343&x-zp-page-request-id=7a3c0dc47a5a4f9bac961767392c0ff9-1568462629449-273340&x-zp-client-id=3f8b21d5-c3ff-42ae-82f7-6c1c4a1b19d2'
    # all_page(url)
    all_url(url, href)
    ##实现多线程抓取，引入了线程池
    pool = ThreadPoolExecutor(max_workers=4)
    while queue_list.qsize() > 0:
        pool.submit(get_data, queue_list.get())
