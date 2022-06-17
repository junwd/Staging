# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZsqbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()     #"公司名称
    sf=scrapy.Field()       #"省份"
    cs=scrapy.Field()       #"城市"
    sr=scrapy.Field()       #"营业收入"
    lr=scrapy.Field()       #"利润
    rs=scrapy.Field()       #员工人数
    time=scrapy.Field()     #上市日期
    fl=scrapy.Field()       #行业分类
    lx=scrapy.Field()       #产品类型

