# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 房名
    jia = scrapy.Field()  # 价格
    zul = scrapy.Field()  # 租赁方式
    lei = scrapy.Field()  # 房屋类型 去除面积
    chao = scrapy.Field()  # 房屋朝向 去除楼层
    mian = scrapy.Field()  # 面积
    lou = scrapy.Field()  # 楼层
    shui = scrapy.Field()  # 用水
    dian = scrapy.Field()  # 用电
    zuq = scrapy.Field()  # 租期
    ran = scrapy.Field()  # 燃气
    ti = scrapy.Field()  # 电梯
    che = scrapy.Field()  # 车位
