# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()  # 电影链接
    info_link = scrapy.Field()  # 电影链接
    pic_link = scrapy.Field()  # 电影图片链接
    cname = scrapy.Field()  # 中文名
    score = scrapy.Field()  # 评分
    rated = scrapy.Field()  # 评论数
    introduction = scrapy.Field()  # 概述
    year_release = scrapy.Field()  # 上映年份改为是否可播放
    country = scrapy.Field()  # 制片国家改为其他
    category = scrapy.Field()  # 类型改为导演
