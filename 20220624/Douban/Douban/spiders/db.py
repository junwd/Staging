import scrapy
from Douban.items import DoubanItem  # 导入items里面的DoubanItem类
import re


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['doubna.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']  # 默认的请求
    domain_url = 'https://movie.douban.com/top250'  # 翻页拼接url

    def parse(self, response):
        item = DoubanItem()  # 创建一个对象
        articles = response.xpath('//ol[@class="grid_view"]/li')  # 使用xpath定位到一页电影所在的列表
        # response.xpath为请求获取网站内容并定位列表，// 为xpath中全部的意思
        for article in articles:  # 使用for 循环读出列表
            item["name"] = article.xpath('.//span[@class="title"]/text()').extract_first()  # 使用xpath定位到数据所在位置
            # article.xpath从列表里面找到数据 .//为在当前位置
            yield item  # 传递
        url1 = response.xpath('//span[@class="next"]/a/@href').extract_first()  # # 找到按钮'下一页'的href
        # 如果下一页url存在， 回调parse方法处理
        if url1:
            yield scrapy.Request(self.domain_url + url1, callback=self.parse, dont_filter=True)
            # 找到下一页后循环
