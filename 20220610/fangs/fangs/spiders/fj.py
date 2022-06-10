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
            # item["cs"] = url1
            for link in href:
                html_data = requests.get(url=link, headers=self.headers).text
                selector_1 = parsel.Selector(html_data)
                item["district"] = selector_1.xpath('//span[@class="info"]/a[1]/text()').get()   # 区域
                item["title"] = selector_1.css('.main::attr(title)').get()   # 标题
                item["bedroom"] = selector_1.xpath('//div[@class="content"]/ul/li[1]/text()').get()   # 房厅
                item["area"] = selector_1.xpath('//div[@class="content"]/ul/li[3]/text()').get()  # 面积
                item["direction"] = selector_1.xpath('//div[@class="content"]/ul/li[7]/text()').get()   # 朝向
                item["decoration"] = selector_1.xpath('//div[@class="content"]/ul/li[9]/text()').get()   # 装修
                item["total_price"] = selector_1.xpath('/html/body/div[5]/div[2]/div[2]/div/span[1]/text()').get()   # 总价(万元)
                item["unit_price"] = selector_1.xpath('/html/body/div[5]/div[2]/div[2]/div/div[1]/div[1]/span/text()').get()   # 单价(元/平方米)
                item["add_date"] = selector_1.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()').get()   # 创建日期
                item["mod_date"] = selector_1.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/span[2]/text()').get()   # 修改日期

                yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse)
