# -*- coding: utf-8 -*-
import scrapy
import requests
from tup.items import TupItem
from lxml import etree


class TpSpider(scrapy.Spider):
    name = 'tp'
    allowed_domains = ['https://pic.netbian.com/4kfengjing/']
    url = "https://pic.netbian.com/4kfengjing/"
    set_page = 1
    start_urls = ['https://pic.netbian.com/4kfengjing/']
    headers = {"User-Agent": "Mozilla/5.0"}

    def parse(self, response):
        item = TupItem()
        imgs = response.xpath('//ul[@class="clearfix"]/li')
        for img in imgs:
            url1 = img.xpath('./a/@href').extract()[0]
            urlLink = "https://pic.netbian.com/" + url1
            res = requests.get(urlLink, headers=self.headers)
            res.encoding = 'utf-8'
            html = res.text
            parsehtml = etree.HTML(html)
            item["imgurl"] = parsehtml.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
            item["imgname"] = img.xpath('//div[@class="photo-pic"]/a/img/@alt').extract_first()
            yield item
        self.set_page += 1
        next_url = self.url + "index_" + str(self.set_page)+".html"
        yield scrapy.Request(next_url, callback=self.parse)
