# -*- coding: utf-8 -*-
import scrapy
from qnzy.items import QnzyItem

class ZySpider(scrapy.Spider):
    name = 'zy'
    allowed_domains = ['www.qnzy.net/']
    start_urls = ['http://www.qnzy.net/list.jsp?cItemId=61']

    def parse(self, response):
        item = QnzyItem()
        articles = response.xpath('//div[@class="articleList"]/ul/li')
        for article in articles:
            wen = article.xpath('./span//text()').extract()
            item["name"] = wen[0]
            item["shi"] = wen[1]
            yield item
