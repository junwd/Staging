import scrapy
from daomu.items import DaomuItem


class DmSpider(scrapy.Spider):
    name = 'dm'
    allowed_domains = ['daomubiji.com']
    start_urls = ['https://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        item = DaomuItem()
        articles = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for article in articles:
            wen = article.xpath('./a/text()').extract()[0].split(' ')
            item["name"] = wen[0]
            item["zhan"] = wen[1]
            item["ti"] = wen[2]
            item["lian"] = article.xpath('./a/@href').extract()
            yield item
