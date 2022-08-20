import scrapy
from top500.items import Top500Item


class KgSpider(scrapy.Spider):
    name = 'kg'
    allowed_domains = ['www.kugou.com']
    # start_urls = ['https://www.kugou.com/yy/rank/home/4-8888.html?from=rank']
    url = 'https://www.kugou.com/yy/rank/home/'
    url1 = '-8888.html?from=rank'
    set_page = 1
    start_urls = [url + str(set_page) + url1]

    def parse(self, response):
        item = Top500Item()
        articles = response.xpath('//div[@class="pc_temp_songlist "]/ul/li')
        for article in articles:
            item["pai"] = article.css('.pc_temp_num::text').get()[28:-18]
            # item["name"] = article.css('.pc_temp_songname::attr(title)').get()
            a = article.css('.pc_temp_songname::attr(title)').get()
            item["name"] = a.split('-')[0]
            item["ge"] = a.split('-')[1]
            # item["ge"] = article.css('.pc_temp_songname span::text').get()[3:]
            item["shi"] = article.css('.pc_temp_time::text').get()[28:-10]
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page) + self.url1
        yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
