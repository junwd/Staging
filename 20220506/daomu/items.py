# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    zhan = scrapy.Field()
    ti = scrapy.Field()
    lian = scrapy.Field()
