from cgitb import html
import requests
import scrapy
import json
from Douban.items import DoubanItem


class DbSpider(scrapy.Spider):
    name = 'DB'
    allowed_domains = ['douban.com']

    url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags='  # &start=0
    # https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=1&start=0
    # https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=2&start=0
    # https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=3&start=0

    set_page = 1
    set_url = '&start=0'
    start_urls = [url + str(set_page) + set_url]

    def parse(self, response):
        content = json.loads(response.body.decode())
        # print(content)
        jobs = content['data']
        # print(jobs)
        for job in jobs:
            item = DoubanItem()
            item["name"] = job['title']
            item["rate"] = job['rate']
            item["id"] = job['id']
            item["cover_x"] = job['cover_x']
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page) + self.set_url
        yield scrapy.Request(next_url, callback=self.parse)
