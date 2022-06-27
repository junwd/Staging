# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YuqiItem(scrapy.Item):
    # define the fields for your item here like:
    area = scrapy.Field()
    curConfirm = scrapy.Field()
    curConfirmRelative = scrapy.Field()
    confirmed = scrapy.Field()
    crued = scrapy.Field()
    died = scrapy.Field()
