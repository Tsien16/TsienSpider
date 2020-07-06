# -*- coding: utf-8 -*-

# Scrapy settings for TsienSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 项目名称,使用 startproject 命令创建项目时会被自动赋值
BOT_NAME = 'TsienSpider'

# 爬虫存储的文件路径
SPIDER_MODULES = ['TsienSpider.spiders']

# 创建爬虫文件的模板，创建好爬虫文件会存放在这个目录下
NEWSPIDER_MODULE = 'TsienSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 模拟浏览器请求,用户代理，一般设置这个参数用来伪装浏览器请求
# USER_AGENT = 'TsienSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 是否遵行robots协议，为False时，表示不遵守,默认为True，表示遵守
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Scrapy downloader(下载器) 处理的最大地并发请求数量。 默认: 16
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 下载延迟的秒数，用来限制访问的频率,默认为0，没有延时
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# 每个域名下能够被执行的最大的并发请求数据量,默认8个
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 设置某个IP最大并发请求数量，默认0个
# 1. 如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。 也就是说，并发限制 将针对IP，而不是网站。
# 2. 该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0， 下载延迟应用在IP而不是网站上。
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否要携带cookies，一般情况下， 不是必须要携带cookies的请求，我们 将这个参数设置为False,默认为: True
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 设置默认的请求头，cookie不要放在这里，会不生效

DEFAULT_REQUEST_HEADERS = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'Host': 'www.stats.gov.cn',
}

# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'TsienSpider.middlewares.TsienspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'TsienSpider.middlewares.TsienspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'TsienSpider.pipelines.MysqlTwistedPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# mysql基本信息
MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "administrative_division"
MYSQL_USER = "root"
MYSQL_PASSWORD = "18896727773"
