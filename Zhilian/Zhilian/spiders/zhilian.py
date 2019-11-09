# -*- coding: utf-8 -*-
import scrapy
import json
from urllib import parse
import requests
from ..items import ZhilianItem
from lxml import etree
import re


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['www.zhaopin.com', 'fe-api.zhaopin.com', 'jobs.zhaopin.com']
    # start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize={}&cityId=763&kw=python&kt=3']
    one_url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=763&kw={}&kt=3'
    keyword = input("请输入工作类型:")

    def start_requests(self):
        headers = {
            "cookie": "sou_experiment=psapi; x-zp-client-id=6dde1cc6-a24b-49bf-c203-1f7cc437e18c; urlfrom2=121114583; adfcid2=www.baidu.com; adfbid2=0; sts_deviceid=16e4c760dab6a8-05a89cb8be675c-7711a3e-1327104-16e4c760dac8a0; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22%24device_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%7D; acw_tc=9dff8bcb15732408363682015e590e043186a9dd5ac8af4cd543618cbe; LastCity%5Fid=763; LastCity=%E5%B9%BF%E5%B7%9E; ZP_OLD_FLAG=false; CANCELALL=1; POSSPORTLOGIN=1; urlfrom=121114583; adfcid=www.baidu.com; adfbid=0; __utma=269921210.1266153240.1573240836.1573240836.1573279420.2; __utmc=269921210; __utmz=269921210.1573279420.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=269921210.1.10.1573279420; dywec=95841923; dywea=95841923.793204343791415700.1573240836.1573240836.1573279420.2; dywez=95841923.1573279420.2.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; dyweb=95841923.1.10.1573279420; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1570976764,1573240836,1573279420; sts_sg=1; sts_sid=16e4ec2ce81148-07d6d07fa47642-7711a3e-1327104-16e4ec2ce827c6; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2e2W0Wg_yswsuNNAgNN6TrjkxZv2vETEHMcan3liZ8PjUt0u48IIGOp4AdWiqwiQ%26wd%3D%26eqid%3De47e0d9f0017cc57000000065dc656ba; jobRiskWarning=true; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1573279427; sts_evtseq=4; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22d85620ba-c303-4f5a-8ca7-ac110e2f2d5a-sou%22%2C%22funczone%22:%22smart_matching%22}}",
            "origin": "https://sou.zhaopin.com",
            "referer": "https://sou.zhaopin.com/?jl=763&kw=python&kt=3",
        }
        keyword = parse.quote(self.keyword)
        for index in range(0, 991, 90):
            url = self.one_url.format(index, keyword)
            yield scrapy.Request(
                # headers=headers,
                url=url,
                callback=self.parse_one_page
            )

    def parse_one_page(self, response):
        html = response.text
        html = json.loads(html)
        headers = {
            "cookie": "sou_experiment=psapi; x-zp-client-id=6dde1cc6-a24b-49bf-c203-1f7cc437e18c; adfbid2=0; sts_deviceid=16e4c760dab6a8-05a89cb8be675c-7711a3e-1327104-16e4c760dac8a0; LastCity%5Fid=763; LastCity=%E5%B9%BF%E5%B7%9E; ZP_OLD_FLAG=false; POSSPORTLOGIN=1; CANCELALL=1; adfbid=0; __utma=269921210.1266153240.1573240836.1573240836.1573279420.2; __utmc=269921210; __utmz=269921210.1573279420.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dywec=95841923; dywez=95841923.1573279420.2.2.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1570976764,1573240836,1573279420; sts_sg=1; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D2e2W0Wg_yswsuNNAgNN6TrjkxZv2vETEHMcan3liZ8PjUt0u48IIGOp4AdWiqwiQ%26wd%3D%26eqid%3De47e0d9f0017cc57000000065dc656ba; jobRiskWarning=true; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1573279495; acw_tc=3ccdc15815732896232864984e5fee442f55588d97f330d97b25f35962073b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22%24device_id%22%3A%2216e4c760dd38f9-053b922627b36d-7711a3e-1327104-16e4c760dd441e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%7D; dywea=95841923.793204343791415700.1573240836.1573279420.1573292721.3; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; JsNewlogin=3019216109; JSloginnamecookie=18998261232; JSShowname=""; at=631087c66bcf46c7bb9882443d48cce6; Token=631087c66bcf46c7bb9882443d48cce6; rt=be6c4c4f8cad4265a330544181a12109; JSpUserInfo=2f79277359665464547155685f6a4e7953735166566452715c68526a36792d73596654645c715c68506a4279517352665464567156685b6a41792673296658645c715568506a4c795a735166546457715068296a0b7912734a6606640b710868526a29793773596654645f7124683d6a477952735466486452714568586a4279597355665e6425712968546a4b7958733166246459712f68206a4a79557350665564517156685f6a43795b735f66306430715868586a417930732d66586451715568596a4b795373566655645f717; uiioit=3d753d6849684564553809644568417958745d7457650e395d7353753b6830684964553802644; privacyUpdateVersion=2; acw_sc__v3=5dc6f0cd01a89ae63576d3d9cab16f92c04960d8; acw_sc__v2=5dc6f0cde69088d94aab655a78e2e269301cdbff; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22d85620ba-c303-4f5a-8ca7-ac110e2f2d5a-sou%22%2C%22funczone%22:%22smart_matching%22}%2C%22jobs%22:{%22recommandActionidShare%22:%226a56a53b-3ea8-4262-9976-3e6f5de0238a-job%22%2C%22funczoneShare%22:%22dtl_best_for_you%22}}; sts_sid=16e511cae9a312-0545c107eee06-7711a3e-1327104-16e511cae9b8c9; sts_evtseq=2",
        }
        for job in html['data']['results']:
            item = ZhilianItem()
            item['jobname'] = job['jobName']  # 岗位名称
            item['company_name'] = job['company']['name']  # 公司名称
            item['company_type'] = job['company']['type']['name']  # 公司类型
            item['company_size'] = job['company']['size']['name']  # 公司大小
            item['city'] = job['city']['display']  # 城市
            item['updateDate'] = job['updateDate']  # 更新日期
            item['salary'] = job['salary']  # 薪资
            item['eduLevel'] = job['eduLevel']['name']  # 学历
            item['workingExp'] = job['workingExp']['name']  # 工作经验
            item['welfare'] = job['welfare']  # 福利
            item['url'] = job['positionURL']
            url = job['positionURL']
            # headers["referer"] = url
            # print(item)

            yield scrapy.Request(
                headers=headers,
                url=url,
                meta={'item': item},
                callback=self.parse_two_page
            )

    def parse_two_page(self, response):
        item = response.meta['item']
        # text=requests.get()
        # html = etree.HTML(response.text)
        item['people'] = response.xpath("//ul[@class='summary-plane__info']/li[4]/text()")
        print(response.text)
        # item['people'] = re.findall('招(.*?)人', response.text)
        item['dult'] = response.xpath("//div[@class='describtion__detail-content']/p/span//text()")
        yield item
