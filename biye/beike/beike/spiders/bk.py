import scrapy
from beike.items import BeikeItem


class BkSpider(scrapy.Spider):
    name = 'bk'
    allowed_domains = ['bk.com']
    start_urls = [f'https://gy.zu.ke.com/zufang/pg{i}/#contentList' for i in range(1, 20)]
    start_url = 'https://gy.zu.ke.com'

    def parse(self, response):
        href = response.css('.twoline::attr(href)').extract()
        # print(href)
        for href_list in href:
            # print(href_list)
            # href1 = self.start_url+href_list
            # print(href1)
            yield scrapy.FormRequest(url=self.start_url + href_list, callback=self.list_data, dont_filter=True)
            # url_s = response.css('p.last a::attr(href)').extract_first()
            # if url_s:
            #     # 找下一页
            #     yield scrapy.Request(self.url + url_s, callback=self.parse, dont_filter=True)

    def list_data(self, response):
        for item in response.xpath('//body'):
            names = response.css('.content .content__title::text').get()  # 房名
            jia = item.css('.content__aside--title span::text').get()  # 价格
            zul = item.css('.content__aside__list li:nth-child(1)::text').get()  # 租赁方式
            lei = item.css('.content__aside__list li:nth-child(2)::text').get()  # 房屋类型 去除面积
            chaos = item.css('.content__article__info ul li:nth-child(3)::text').get()  # 房屋朝向 去除楼层
            mians = item.css('.content__article__info ul li:nth-child(2)::text').get()  # 面积
            lous = item.css('.content__article__info ul li:nth-child(8)::text').get()  # 楼层
            shuis = item.css('.content__article__info ul li:nth-child(12)::text').get()  # 用水
            dians = item.css('.content__article__info ul li:nth-child(14)::text').get()  # 用电
            zuqs = item.css('.content__article__info ul:nth-child(3) li:nth-child(2)::text').get()  # 租期
            rans = item.css('.content__article__info ul li:nth-child(15)::text').get()  # 燃气
            tis = item.css('.content__article__info ul li:nth-child(9)::text').get()  # 电梯
            ches = item.css('.content__article__info ul li:nth-child(11)::text').get()  # 车位
            yield {
                "name": names.split('·')[1],
                "jia": jia,
                "zul": zul,
                "lei": lei.split(' ')[0],
                "chao": chaos.split('：')[1],
                "mian": mians.split('：')[1],
                "lou": lous.split('：')[1],
                "shui": shuis.split('：')[1],
                "dian": dians.split('：')[1],
                "zuq": zuqs.split('：')[1],
                "ran": rans.split('：')[1],
                "ti": tis.split('：')[1],
                "che": ches.split('：')[1],
            }
