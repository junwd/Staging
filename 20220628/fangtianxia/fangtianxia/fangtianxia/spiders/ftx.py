import scrapy
from fangtianxia.items import FangtianxiaItem


class FtxSpider(scrapy.Spider):
    name = 'ftx'
    allowed_domains = ['ftx.com']
    start_urls = ['https://esf.fang.com/fapai/i31/']
    url = 'https://esf.fang.com'

    def parse(self, response):
        href = response.css('h4.clearfix a::attr(href)').extract()  # 每个详情页的url
        for href_list in href:
            # 循环取出链接
            yield scrapy.FormRequest(url=self.url + href_list, callback=self.href_data, dont_filter=True)
            # 回调请求
        url_s = response.css('p.last a::attr(href)').extract_first()
        if url_s:
            # 找下一页
            yield scrapy.Request(self.url + url_s, callback=self.parse, dont_filter=True)

    def href_data(self, response):
        for item in response.xpath('//body'):
            yield {
                "name": item.css('div.tit_fpf.clearfix h1::text').get(),
                "jia": item.css('div.righ_text p::text').get(),
                "di": item.xpath('//div[@class="info_fpf"]/ul/li[5]/div/text()').get(),
                'bao': item.css('ul.clearfix li p::text').get(),
                "jij": item.xpath('//ul[@class="clearfix"]/li[3]/p/text()').get(),
                "mian": item.xpath('//ul[@class="clearfix"]/li[6]/p/text()').get()[:-1],
            }
