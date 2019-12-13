# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import BitfinexItem


class BitfinexSpider(scrapy.Spider):
    name = 'bitfinex'
    allowed_domains = ['www.bitfinex.com']

    # start_urls = ['https://api.bitfinex.com/v1/book/BTCUSD?_bfx_full=1']

    def start_requests(self):
        url = 'https://api.bitfinex.com/v1/book/BTCUSD?_bfx_full=1'
        yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)

    def parse(self, response):
        html = json.loads(response.text)
        buy_price_list = []
        buy_amount_list = []
        sell_price_list = []
        sell_amount_list = []
        time_list = []

        for i in html['bids']:
            buy_price = i['price']
            buy_price_list.append(buy_price)
        for j in html['bids']:
            buy_amount = j['amount']
            buy_amount_list.append(buy_amount)
        for k in html['asks']:
            sell_price = k['price']
            sell_price_list.append(sell_price)
        for z in html['asks']:
            sell_amount = z['amount']
            sell_amount_list.append(sell_amount)
        for t in html['asks']:
            time = t['timestamp']
            time_list.append(time)
        results = zip(buy_price_list, buy_amount_list, sell_price_list, sell_amount_list, time_list)
        for result in results:
            item = BitfinexItem()
            item['buy_price'] = result[0]
            item['buy_amount'] = result[1]
            item['sell_price'] = result[2]
            item['sell_amount'] = result[3]
            item['time'] = result[4]
            # next_url = 'https://api.bitfinex.com/v1/book/BTCUSD?_bfx_full=1'
            yield item
        next_url = 'https://api.bitfinex.com/v1/book/BTCUSD?_bfx_full=1'
        yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
