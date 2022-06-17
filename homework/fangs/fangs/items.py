# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangsItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()  # 面积
    info_link = scrapy.Field()  # url1
    pic_link = scrapy.Field()  # url2
    cname = scrapy.Field()  # 地区
    score = scrapy.Field()  # 价格
    rated = scrapy.Field()  # 几舍
    introduction = scrapy.Field()  # 简介
    year_release = scrapy.Field()  # 时间
    country = scrapy.Field()  # 装修
    category = scrapy.Field()  # 朝向
