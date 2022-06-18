import scrapy
from liepin.items import LiepinItem


class LpSpider(scrapy.Spider):
    name = 'lp'
    allowed_domains = ['liepin.com']
    # start_urls = ['http://liepin.com/']
    url = 'https://www.liepin.com/zhaopin/?headId=&sfrom=search_job_pc&key=web%E5%89%8D%E7%AB%AF&industry=1$030&currentPage='
    set_page = 0
    start_urls = [url + str(set_page)]

    def parse(self, response):
        item = LiepinItem()
        articles = response.xpath('//div[@class="left-list-box"]/ul/li')
        for article in articles:
            item["name"] = article.xpath('.//div[@class="ellipsis-1"]/text()').extract_first()
            item["xz"] = article.xpath('.//span[@class="job-salary"]/text()').extract_first()
            item["dq"] = article.xpath('.//span[@class="ellipsis-1"]/text()').extract_first()
            item["nz"] = article.xpath('.//div[@class="job-labels-box"]/span[1]/text()').extract_first()
            item["xl"] = article.xpath('.//div[@class="job-labels-box"]/span[2]/text()').extract_first()
            item["gs"] = article.xpath('.//span[@class="company-name ellipsis-1"]/text()').extract_first()
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse)
