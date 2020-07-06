# -*- coding: utf-8 -*-
import scrapy
from TsienSpider.items import AdministrativeDivisionItem


class AdministrativeDivisionSpider(scrapy.Spider):
    name = 'administrative-division'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html']

    def parse(self, response):
        """
        用于解析个人用户页的所有比赛
        :param response:
        :return:
        """
        area_item = AdministrativeDivisionItem()
        area_node_list = response.css(".provincetr td a")
        for area_node in area_node_list:
            area_item['areaCode'] = area_node.css('a::attr(href)').extract_first()
            area_item['areaName'] = area_node.css('a::text').extract_first()
            area_item['areaLevel'] = '省'
            area_item['parentCode'] = '0'
            area_item['urCode'] = '0'
            yield area_item
