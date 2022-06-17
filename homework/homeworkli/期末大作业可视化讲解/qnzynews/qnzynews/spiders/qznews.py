# -*- coding: utf-8 -*-
import scrapy
from qnzynews.items import QnzynewsItem

class QznewsSpider(scrapy.Spider):
    name = 'qznews'
    allowed_domains = ['qnzy.net']
    url="http://www.qnzy.net/list.jsp?cItemId=44&itemId=2&page="
    set_page=1
    start_urls = [url+str(set_page)]

    def parse(self, response):
        item=QnzynewsItem()
        articles=response.xpath('//li[@style="line-height:41px;height:41px;background-image: url(icon/bit01.jpg);background-position: left center ;"]')
        for article in articles:
            item["title"]=article.xpath('./span[1]/a/text()').extract()[0]
            item["time"]=article.xpath('./span[2]/text()').extract()[0]

            yield item
        self.set_page+=1
        next_url=self.url+str(self.set_page)
        yield scrapy.Request(next_url,callback=self.parse)
