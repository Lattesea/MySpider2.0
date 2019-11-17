# -*- coding: utf-8 -*-

# Scrapy settings for sgcnSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sgcnSpider'

SPIDER_MODULES = ['sgcnSpider.spiders']
NEWSPIDER_MODULE = 'sgcnSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sgcnSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'iZOJfd_c4f3_saltkey=G2LnKCLJ; iZOJfd_c4f3_lastvisit=1573390687; _ga=GA1.2.425666919.1573394290; _gid=GA1.2.846694321.1573394290; iZOJfd_c4f3_connect_qq_nick=%E9%97%B2%E9%B1%BC%E7%BF%BB%E8%BA%AB; iZOJfd_c4f3_stats_qc_login=4; iZOJfd_c4f3_client_created=1573400048; iZOJfd_c4f3_client_token=1; iZOJfd_c4f3_connect_login=1; iZOJfd_c4f3_connect_is_bind=1; iZOJfd_c4f3_connect_uin=A4F255F3702304EE44ABBB1E81C3500D; iZOJfd_c4f3_stats_qc_reg=1; iZOJfd_c4f3_nofavfid=1; PHPSESSID=3ba6aksnd434cm53gcta2j1jr7; iZOJfd_c4f3_home_diymode=1; iZOJfd_c4f3_st_p=0%7C1573461402%7Cfccf2fdef287ce665a4e95c84bb6a776; iZOJfd_c4f3_viewid=tid_16378260; iZOJfd_c4f3_sendmail=1; _gat=1; iZOJfd_c4f3_ulastactivity=1573462989%7C0; iZOJfd_c4f3_auth=6b6eyqZJXDO6MEhCOI7VHNaz%2BN0lg00%2FCpyj%2BrIWFltDGpGyPWchMpuLYlBlyEVKbPDw4i2%2B3VDzDJBkHDFPpaLVt8kF; iZOJfd_c4f3_lastcheckfeed=1099896%7C1573462989; iZOJfd_c4f3_checkfollow=1; iZOJfd_c4f3_lip=58.249.80.50%2C1573462989; iZOJfd_c4f3_checkpm=1; iZOJfd_c4f3_st_t=1099896%7C1573463009%7C6e5d9aa69a61b101e0cfecf89ed9ce09; iZOJfd_c4f3_forum_lastvisit=D_215_1573461446D_235_1573463009; iZOJfd_c4f3_visitedfid=235D215; iZOJfd_c4f3_lastact=1573463010%09connect.php%09check',
    'Host': 'bbs.sgcn.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sgcnSpider.middlewares.SgcnspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'sgcnSpider.middlewares.SgcnspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'sgcnSpider.pipelines.SgcnspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#JOBDIR='sgcn_request_seen_1'