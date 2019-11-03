#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 19-10-21 上午9:58 
# @Author : Lattesea 
# @File : 爬取猫眼电影实时数据test1.py 
import requests
from fontTools.ttLib import TTFont
from fake_useragent import UserAgent
import re
import os
from lxml import etree


class MaoyanSpider(object):
    def __init__(self):
        self.url = ''

    def get_headers(self):
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        return headers

    def modify_html(self, newFont, html):
        basefont = TTFont('./base_font.woff')

        unilist = newFont['cmap'].tables[0].ttFont.getGlyphOrder()

        numlist = []

        base_num = ['6', '3', '7', '1', '5', '9', '0', '4', '2', '8']

        base_unicode = ['uniF0DA', 'uniE907', 'uniED01', 'uniEAE1', 'uniF206',

                        'uniE455', 'uniF401', 'uniE19C', 'uniEB76', 'uniF855']

        for i in range(1, len(unilist)):

            newGlyph = newFont['glyf'][unilist[i]].coordinates

            for j in range(len(base_unicode)):

                baseGlyph = basefont['glyf'][base_unicode[j]].coordinates

                if compare(newGlyph, baseGlyph):

                    numlist.append(base_num[j])

                    break

        rowList = []

        for i in unilist[2:]:

            i = i.replace('uni', '&#x').lower() + ";"

            rowList.append(i)

        dictory = dict(zip(rowList, numlist))

        for key in dictory:

            if key in html:

                html = html.replace(key, str(dictory[key]))

                return html

    def parse(self,html):
        pattern = re.compile('<dd>.*?board-index-.*?>(.*?)</i>.*?src="(.*?)".*?'

                             + 'title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?'

                             + 'realtime".*?stonefont">(.*?)</span>.*?'

                             + 'total-boxoffice".*?stonefont">(.*?)</span>.*?</dd>', re.S)

        items = re.findall(pattern, html)

        data = pd.DataFrame(items,
                            columns=['index', 'image', 'title', 'star', 'releasetime', 'realtime', 'total-boxoffice'])

        data['star'] = data['star'].str[3:]

        data['releasetime'] = data['releasetime'].str[5:]

        print(data)

        return data

    def run(self):
        html=self.modify_html()
        self.parse(html)


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
