# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangsItem(scrapy.Item):
    # define the fields for your item here like:
    district = scrapy.Field()
    title = scrapy.Field()
    bedroom = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    decoration = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    add_date = scrapy.Field()
    mod_date = scrapy.Field()


