# -*- coding: utf-8 -*-
import scrapy


class AdministrativeDivisionSpider(scrapy.Spider):
    name = 'administrative-division'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://stats.gov.cn/']

    def parse(self, response):
        pass
