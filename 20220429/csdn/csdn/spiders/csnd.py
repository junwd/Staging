# -*- coding: utf-8 -*-
import scrapy
from csdn.items import CsdnItem


class CsndSpider(scrapy.Spider):
    name = 'csnd'
    allowed_domains = ['blog.csdn.net/weixin_45962741/article/details/120005833']
    start_urls = ['http://blog.csdn.net/weixin_45962741/article/details/120005833/']

    def parse(self, response):
        item = CsdnItem()
        item["name"] = response.xpath('//div[@class="article-title-box"]/h1/text()').extract()
        item["shi"] = response.xpath('//div[@class="bar-content"]/span/text()').extract()[0]
        item["re"] = response.xpath('//span[@class="read-count"]/text()').extract()
        yield item
