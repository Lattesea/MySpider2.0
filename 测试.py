#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-9-12 下午2:17 
# @Author : Lattesea 
# @File : 测试.py

import requests
from lxml import etree
import re

url = "https://jobs.zhaopin.com/CC143220695J00189726615.htm"
headers = {
    "cookie": "sou_experiment=psapi; x-zp-client-id=6dde1cc6-a24b-49bf-c203-1f7cc437e18c; adfbid2=0; sts_deviceid=16e4c760dab6a8-05a89cb8be675c-7711a3e-1327104-16e4c760dac8a0; LastCity%5Fid=763; LastCity=%E5%B9%BF%E5%B7%9E; ZP_OLD_FLAG=false; POSSPORTLOGIN=1; CANCELALL=1; adfbid=0; __utma=269921210.1266153240.1573240836.1573240836.1573279420.2; __utmc=269921210; __utmz=269921210.1573279420.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dywec=95841923; dywez=95841923.1573279420.2.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1570976764,1573240836,1573279420; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2e2W0Wg_yswsuNNAgNN6TrjkxZv2vETEHMcan3liZ8PjUt0u48IIGOp4AdWiqwiQ%26wd%3D%26eqid%3De47e0d9f0017cc57000000065dc656ba; jobRiskWarning=true; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1573279495; acw_tc=3ccdc15815732896232864984e5fee442f55588d97f330d97b25f35962073b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22%24device_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; dywea=95841923.793204343791415700.1573240836.1573279420.1573292721.3; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; JsNewlogin=3019216109; JSloginnamecookie=18998261232; JSShowname=""; at=631087c66bcf46c7bb9882443d48cce6; Token=631087c66bcf46c7bb9882443d48cce6; rt=be6c4c4f8cad4265a330544181a12109; JSpUserInfo=2f79277359665464547155685f6a4e7953735166566452715c68526a36792d73596654645c715c68506a4279517352665464567156685b6a41792673296658645c715568506a4c795a735166546457715068296a0b7912734a6606640b710868526a29793773596654645f7124683d6a477952735466486452714568586a4279597355665e6425712968546a4b7958733166246459712f68206a4a79557350665564517156685f6a43795b735f66306430715868586a417930732d66586451715568596a4b795373566655645f717; uiioit=3d753d6849684564553809644568417958745d7457650e395d7353753b6830684964553802644; privacyUpdateVersion=2; acw_sc__v3=5dc6e9a6c2b4ed35cd435694dbe787a4cc98217d; acw_sc__v2=5dc6e9a34bf31695b4f6743b4575e8fbf0d83252; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22d85620ba-c303-4f5a-8ca7-ac110e2f2d5a-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%2234ec71c1-28ce-44fe-bcdd-140733396054-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_sid=16e5100bc9e25f-0f53c8d196a4aa-7711a3e-1327104-16e5100bc9f9df; sts_evtseq=2",
    # "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"
}

# headers["referer"]=url
response = requests.get(url=url, headers=headers).text
html=etree.HTML(response)
people1=html.xpath("//ul[@class='summary-plane__info']/li[4]/text()")
print(response)
print(people1)
people = re.findall('<li>招(.*?)人</li>', response)
print(people)
