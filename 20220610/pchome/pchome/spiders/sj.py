import parsel
import scrapy
import requests
from pchome.items import PchomeItem
from lxml import etree


class SjSpider(scrapy.Spider):
    name = 'sj'
    allowed_domains = ['product.pchome.net']
    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://product.pchome.net/cell_phone/list/105.html?page='
    set_page = 1
    start_urls = [url + str(set_page)]

    def parse(self, response):
        item = PchomeItem()
        articles = response.xpath('//div[@class="pl-mainList"]/ul/li')
        for article in articles:
            href = article.xpath('./a/@href').getall()  # 找到url
            # item["Phone1"] = article.xpath('./a/h4/text()').get()
            # item["Price1"] = article.xpath('.//div[@class="pl-mainList-price"]/i/text()').get()
            for link in href:
                html_data = requests.get(url=link, headers=self.headers).text
                selector_1 = parsel.Selector(html_data)
                item["Phone"] = selector_1.xpath('//div[@class="hd-left"]/h1//text()').get()
                item["Price"] = selector_1.xpath('//div[@class="hd-left"]/div//text()').get()
                item["battery"] = selector_1.xpath('//*[@id="tab"]/div[1]/div[2]/div[2]/div[1]/div[3]/p/text()').get()
                item["memory"] = selector_1.xpath('//*[@id="tab"]/div[1]/div[2]/div[2]/div[1]/div[4]/p/text()').get()
                item["shi"] = selector_1.xpath('//*[@id="tab-detail"]/tbody/tr[1]/td/div[1]/p/text()').get()
                item["pixel"] = selector_1.xpath('//*[@id="tab"]/div[1]/div[2]/div[2]/div[2]/div[1]/p/text()').get()
                item["cpu"] = selector_1.xpath('//*[@id="tab-detail"]/tbody/tr[4]/td/div[2]/p/text()').get()
                yield item

        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse)
