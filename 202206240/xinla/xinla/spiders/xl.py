import re

import parsel
import scrapy
import requests
from xinla.items import XinlaItem


class XlSpider(scrapy.Spider):
    name = 'xl'
    allowed_domains = ['xl.com']
    start_urls = ['https://news.sina.com.cn/']

    def parse(self, response):
        url1 = response.xpath('//li/a/@href').re('https.*\d{4}-\d{2}-\d{2}.*shtml$')
        # url2 = response.xpath('//li/a').re('shtml.*>(.*?)<\/a>$')
        for url3 in url1:
            yield scrapy.Request(url=url3, callback=self.okok, dont_filter=True)

    def okok(self, response):
        list = response.xpath('//div')
        for i in list:
            list1 = i.xpath('.//span[@class="date"]/text()').get()
            print(list1)
