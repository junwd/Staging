# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
import json


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['careers.tencent.com/']
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?&pageSize=10&language=zh-cn&area=cn&pageIndex='
    set_page = 1
    start_urls = [url + str(set_page)]

    def parse(self, response):
        content = json.loads(response.body.decode())
        # print(content)
        jobs = content['Data']['Posts']
        # print(jobs)
        for job in jobs:
            item = TencentItem()
            item["name"] = job['RecruitPostName']
            item["di"] = job['LocationName']
            item["pin"] = job['CategoryName']
            item["shi"] = job['LastUpdateTime']
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
