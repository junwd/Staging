# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GupiaoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    dai = scrapy.Field()
    jia = scrapy.Field()
    zi = scrapy.Field()
    lei = scrapy.Field()