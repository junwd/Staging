# -*- coding: utf-8 -*-
import scrapy
from qnzy.items import QnzyItem


class QnSpider(scrapy.Spider):
    name = 'qn'
    allowed_domains = ['www.qnzy.net']
    url = "http://www.qnzy.net/public/consultletter/letterlist?searchType=4&consultId=8&page="
    set_page = 1
    start_urls = [url+str(set_page)]

    def parse(self, response):
        item = QnzyItem()
        articles = response.xpath('//div[@class="win_b"]/div[2]/div')
        for article in articles:
            item["bia"] = article.xpath('./ul/li[1]/text()').extract_first()
            item["bio"] = article.xpath('./ul/li/a//text()').extract_first()
            item["lei"] = article.xpath('./ul/li[3]/text()').extract_first()
            item["shi"] = article.xpath('./ul/li[4]/text()').extract_first()
            item["hui"] = article.xpath('./ul/li[5]/text()').extract_first()
            item["zha"] = article.xpath('./ul/li[6]/text()').extract_first()
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse)
