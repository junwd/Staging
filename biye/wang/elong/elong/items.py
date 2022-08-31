# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ElongItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 名称
    pin = scrapy.Field()  # 评分
    di = scrapy.Field()  # 地点
    pnu = scrapy.Field()  # 评论
    zun = scrapy.Field()  # 装修风格
    jul = scrapy.Field()  # 距离
    lei = scrapy.Field()  # 类型

