# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TsienspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AdministrativeDivisionItem(scrapy.Item):
    areaCode = scrapy.Field()  # 行政区域代码
    areaName = scrapy.Field()  # 行政区域名称
    areaLevel = scrapy.Field()  # 行政区域级别
    parentCode = scrapy.Field()  # 上级行政区域代码
    urCode = scrapy.Field()  # 城乡分类代码

    def get_insert_sql(self):
        insert_sql = "insert into administrative_division(area_code, area_name, area_level, parent_code, ur_code) \
        	VALUES (%s,%s,%s,%s,%s) "
        params = (
            self["areaCode"],
            self["areaName"],
            self["areaLevel"],
            self["parentCode"],
            self["urCode"],
        )
        return insert_sql, params
