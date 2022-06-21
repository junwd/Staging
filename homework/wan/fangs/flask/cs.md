面积-
链接-链接-地区-价格-几舍-介绍-时间-装修-朝向

item["id"], item["info_link"], item["pic_link"], item['cname'], item["score"], item["rated"],
item["introduction"], item["year_release"], item["country"], item["category"]
    id = scrapy.Field()  # 面积
    info_link = scrapy.Field()  # url
    pic_link = scrapy.Field()  # url
    cname = scrapy.Field()  # 地区
    score = scrapy.Field()  # 价格
    rated = scrapy.Field()  # 几舍
    introduction = scrapy.Field()  # 介绍
    year_release = scrapy.Field()  # 时间
    country = scrapy.Field()  # 装修 //*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()
    category = scrapy.Field()  # 朝向