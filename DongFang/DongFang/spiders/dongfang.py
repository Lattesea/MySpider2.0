# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import DongfangItem


class DongfangSpider(scrapy.Spider):
    name = 'dongfang'
    allowed_domains = ['data.eastmoney.com']

    # start_urls = ['http://data.eastmoney.com/']

    def start_requests(self):
        url = 'http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=YJBB21_YJBB&token=70f12f2f4f091e459a279469fe49eca5&st=latestnoticedate&sr=-1&p=%s&ps=50&js=var%20ddBqHseR={pages:(tp),data:%20(x),font:(font)}&filter=(securitytypecode%20in%20(%27058001001%27,%27058001002%27))(reportdate=^2019-09-30^)&rt=52533718'
        for p in range(1, 78):
            url = url % p
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        dict_FontMapping = {}
        response_replace = re.findall('"FontMapping":(.*?)}}', response)[0]
        response_code = re.findall('"code":"(.*?)"', response_replace)
        response_values = re.findall('"value":(.*?)}', response_replace)
        response_zip = zip(response_code, response_values)
        for i in response_zip:
            dict_FontMapping[i[0]] = i[1]
        print(dict_FontMapping)
        for key in dict_FontMapping:
            response = response.replace(str(key), dict_FontMapping[key])
        print(response)
        sname = re.findall('sname":"(.*?)"', response)  # 股票简称
        scode = re.findall('scode":"(.*?)"', response)  # 股票代码
        basiceps = re.findall('basiceps":"(.*?)"', response)  # 每股收益
        totaloperatereve = re.findall('totaloperatereve":"(.*?)"', response)  # 营业收入
        ystz = re.findall('ystz":"(.*?)"', response)  # 营业收入同比增长
        yshz = re.findall('yshz":"(.*?)"', response)  # 营业收入季度环比增长
        parentnetprofit = re.findall('parentnetprofit":"(.*?)"', response)  # 净利润
        sjltz = re.findall('sjltz":"(.*?)"', response)  # 净利润同比增长
        sjlhz = re.findall('sjlhz":"(.*?)"', response)  # 净利润季度环比增长
        roeweighted = re.findall('roeweighted":"(.*?)"', response)  # 净值产收益率
        bps = re.findall('bps":"(.*?)"', response)  # 每股净资产
        mgjyxjje = re.findall('mgjyxjje":"(.*?)"', response)  # 每股经营现金流量
        xsmll = re.findall('xsmll":"(.*?)"', response)  # 销售毛利率
        publishname = re.findall('publishname":"(.*?)"', response)  # 所属行业
        reportdate = re.findall('reportdate":"(.*?)"', response)  # 更新日期
        # print(sname, scode, basiceps, totaloperatereve, ystz, yshz, parentnetprofit, sjltz, sjlhz, roeweighted, bps,
        #       mgjyxjje, xsmll, publishname, reportdate)
        results = zip(sname, scode, basiceps, totaloperatereve, ystz, yshz, parentnetprofit, sjltz, sjlhz, roeweighted,
                      bps, mgjyxjje, xsmll, publishname, reportdate)
        item = DongfangItem()
        for result in results:
            item['sname'] = result[0]
            item['scode'] = result[1]
            item['basiceps'] = result[2]
            item['totaloperatereve'] = result[3]
            item['ystz'] = result[4]
            item['yshz'] = result[5]
            item['parentnetprofit'] = result[6]
            item['sjltz'] = result[7]
            item['sjlhz'] = result[8]
            item['roeweighted'] = result[9]
            item['bps'] = result[10]
            item['mgjyxjje'] = result[11]
            item['xsmll'] = result[12]
            item['publishname'] = result[13]
            item['reportdate'] = result[14]
            yield item
