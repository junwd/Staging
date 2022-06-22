# -*- coding: utf-8 -*-
import scrapy
from chinaz.items import ChinazItem


class GenSpider(scrapy.Spider):
    name = 'gen'
    allowed_domains = ['gen.com']
    # start_urls = ['http://gen.com/']
    url = "http://top.chinaz.com/hangye/index_jiaotonglvyou_"  # .html
    set_page = 2
    set_html = '.html'
    start_urls = [url + str(set_page) + set_html]

    def parse(self, response):
        item = ChinazItem()
        articles = response.xpath('//ul[@class="listCentent"]/li')
        for article in articles:
            item["name"] = article.xpath('.//h3[@class="rightTxtHead"]/a/text()').extract_first()              #名字
            item["pai"] = article.xpath('.//p[@class="RtCData"]/a/text()').extract_first()                     #周排名
            item["wang"] = article.xpath('.//h3[@class="rightTxtHead"]/span/text()').extract_first()           #网站
            item["fan"] = article.xpath('.//div[@class="RtCPart clearfix"]/p[4]/a/text()').extract_first()     #反链数
            item["tui"] = article.xpath('.//strong[@class="col-red02"]/text()').extract_first()                #得分
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page) + self.set_html
        yield scrapy.Request(next_url, callback=self.parse,dont_filter=True)
