# -*- coding: utf-8 -*-
import scrapy
from deins.items import DeinsItem


class BdSpider(scrapy.Spider):
    name = 'bd'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item = DeinsItem()
        # item["name"] = response.xpath('//div[@id="s-top-left"]/a/text()').extract()[:-5]
        item["hao"] = response.xpath('//div[@id="s-top-left"]/a/text()').extract()[0]
        item["name"] = response.xpath('//div[@id="s-top-left"]/a/text()').extract()[1]

        yield item
