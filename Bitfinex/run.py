from scrapy import cmdline
import time
import os
import threading
import time


# cmdline.execute('scrapy crawl bitfinex -o bitfinex.csv'.split())

cmdline.execute('scrapy crawl bitfinex'.split())
# # while True:
# #     os.system('scrapy crawl bitfinex')
# def go(num):
#     cmdline.execute('scrapy crawl bitfinex'.split())
#     time.sleep(1)
#
#
# t1 = threading.Thread(target=go, args=("t1",))
# t2 = threading.Thread(target=go, args=("t2",))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
