import re

import scrapy
from Douban.items import DoubanItem
import parsel
import requests
from lxml import etree
class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']
    url = 'https://movie.douban.com/top250?start='
    set_page = 0
    set_pag = '&filter='
    start_urls = [url + str(set_page) + set_pag]

    def parse(self, response):
        item = DoubanItem()
        articles = response.xpath('//ol[@class="grid_view"]/li')
        for article in articles:
            item["info_link"] = article.xpath('.//div[@class="hd"]/a/@href').extract_first()  # 电影链接
            item["pic_link"] = article.xpath('.//div[@class="pic"]/a/img/@src').extract_first()  # 电影图片链接
            item["cname"] = article.xpath('.//span[@class="title"]/text()').extract_first()  # 中文名
            item["score"] = article.xpath('.//div[@class="star"]/span[2]/text()').extract_first()  # 评分 -价格
            item["rated"] = article.xpath('.//div[@class="star"]/span[4]/text()').extract_first()  # 评论数-几舍
            item["introduction"] = article.xpath('.//span[@class="inq"]/text()').extract_first()  # 概述-介绍
            item["year_release"] = article.xpath('.//span[@class="playable"]//text()').extract_first()  # 上映年份改为是否可播放
            item["country"] = article.xpath('.//span[@class="other"]//text()').extract_first()[3:]  # 制片国家改为其他
            item["category"] = article.xpath('.//div[@class="bd"]/p/text()').get()[33:40]  # 导演
            item["id"] = "1"  # 类型
            yield item
        self.set_page += 1 * 25
        next_url = self.url + str(self.set_page) + self.set_pag
        yield scrapy.Request(next_url, callback=self.parse)
