# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TupItem(scrapy.Item):
    # define the fields for your item here like:
    imgurl = scrapy.Field()
    imgname = scrapy.Field()
