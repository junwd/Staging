# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    xz = scrapy.Field()
    dq = scrapy.Field()
    nz = scrapy.Field()
    xl = scrapy.Field()
    gs = scrapy.Field()

