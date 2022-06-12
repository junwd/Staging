import scrapy
from stockstar.items import StockstarItem


class BkSpider(scrapy.Spider):
    name = 'bk'
    allowed_domains = ['stockstar.com']
    url = 'http://stock.stockstar.com/list/1577_'
    set_page = 1
    set_pa = ".shtml"
    start_urls = [url + str(set_page)+set_pa]


    def parse(self, response):
        item = StockstarItem()
        articles = response.xpath('//div[@class="listnews"]/ul/li')
        for article in articles:
            item["name"] = article.xpath('.//a/text()').extract_first()
            item["shi"] = article.xpath('.//span/text()').extract_first()
            yield item

        self.set_page += 1
        next_url = self.url + str(self.set_page) + self.set_pa
        yield scrapy.Request(next_url, callback=self.parse)
