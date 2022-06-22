# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 名称
    rate = scrapy.Field()  # 评分
    id = scrapy.Field()  # id
    cover_x = scrapy.Field()  # 人气
