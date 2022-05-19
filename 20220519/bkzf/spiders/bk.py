import scrapy
from bkzf.items import BkzfItem

class BkSpider(scrapy.Spider):
    name = 'bk'
    allowed_domains = ['gy.fang.ke.com']
    url = 'https://gy.fang.ke.com/loupan/1/pg'
    set_page = 1
    start_urls = [url + str(set_page)]

    def parse(self, response):
        item = BkzfItem()
        articles = response.xpath('//ul[@class="resblock-list-wrapper"]/li')
        for article in articles:
            item["name"] = article.xpath('.//a[@class="name "]/text()').extract_first()
            item["zo"] = article.xpath('.//div[@class="second"]/text()').extract_first()
            item["jia"] = article.xpath('.//span[@class="number"]/text()').extract_first()
            item["mia"] = article.xpath('.//span[@class="area"]/text()').extract_first()
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse)
