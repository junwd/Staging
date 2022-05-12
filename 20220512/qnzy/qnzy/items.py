# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QnzyItem(scrapy.Item):
    # define the fields for your item here like:
    bia = scrapy.Field()
    bio = scrapy.Field()
    lei = scrapy.Field()
    shi = scrapy.Field()
    hui = scrapy.Field()
    zha = scrapy.Field()

