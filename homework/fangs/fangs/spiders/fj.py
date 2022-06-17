import parsel
import scrapy
import requests
from fangs.items import FangsItem
from lxml import etree


class FjSpider(scrapy.Spider):
    name = 'fj'
    allowed_domains = ['gy.lianjia.com']
    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://gy.lianjia.com/ershoufang/pg'
    set_page = 1
    start_urls = [url + str(set_page)]

    def parse(self, response):
        item = FangsItem()
        articles = response.xpath('//ul[@class="sellListContent"]/li')
        for article in articles:
            href = article.xpath('.//div[@class="title"]/a/@href').getall()
            # item["info_link"] = href  # url1
            for link in href:
                html_data = requests.get(url=link, headers=self.headers).text
                selector_1 = parsel.Selector(html_data)
                item["info_link"] = selector_1.xpath('//*[@id="topImg"]/div[3]/a/@href').get()
                item["id"] = selector_1.xpath('//div[@class="content"]/ul/li[3]/text()').get()  # 面积
                item["pic_link"] = selector_1.xpath('/html/body/div[7]/div[1]/div[4]/div/div[1]/div/div[3]/img/@src').get()  # url2
                item["cname"] = selector_1.xpath('//a[@class="info "]/text()').get()  # 地区
                item["score"] = selector_1.xpath('/html/body/div[5]/div[2]/div[2]/div/span[1]/text()').get()  # 总价(万元)
                item["rated"] = selector_1.xpath('//div[@class="content"]/ul/li[1]/text()').get()  # 房厅
                item["introduction"] = selector_1.css('.main::attr(title)').get()  # 简介
                item["year_release"] = selector_1.xpath('//div[@class="content"]/ul/li[1]/span[2]/text()').get()  # 时间
                item["country"] = selector_1.xpath('//div[@class="content"]/ul/li[9]/text()').get()  # 装修
                item["category"] = selector_1.xpath('//div[@class="content"]/ul/li[7]/text()').get()  # 朝向

                yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse)
