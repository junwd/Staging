# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinazItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()   #名字
    pai = scrapy.Field()    #周排名
    wang = scrapy.Field()   #网站
    fan = scrapy.Field()    #反链数
    tui = scrapy.Field()    #得分

