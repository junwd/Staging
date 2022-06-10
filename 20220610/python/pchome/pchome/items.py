# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PchomeItem(scrapy.Item):
    # define the fields for your item here like:
    Phone = scrapy.Field()  # 手机
    Price = scrapy.Field()  # 价格
    battery = scrapy.Field()  # 电池
    memory = scrapy.Field()  # 内存
    shi = scrapy.Field()  # 上市时间
    pixel = scrapy.Field()  # 像素
    cpu = scrapy.Field()  # 处理器

