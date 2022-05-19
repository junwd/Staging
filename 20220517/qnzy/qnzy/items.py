# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QnzyItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    time = scrapy.Field()
    Company = scrapy.Field()
    reply = scrapy.Field()
