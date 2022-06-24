import scrapy
from gupiao.items import GupiaoItem


class GpSpider(scrapy.Spider):
    name = 'gp'
    allowed_domains = ['gp.com']
    url = 'https://push2ex.eastmoney.com/getTopicQSPool?cb=callbackdata5073295&ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex='
    set_url = '&pagesize=20&sort=zdp%3Adesc&date=20220624&_=1656070426198'
    set_page = 1
    start_urls = [url + str(set_page) + set_url]

    def parse(self, response):
        item = GupiaoItem()
        name = response.xpath('.').re('"n":"(.*?)","')
        dai = response.xpath('.').re('{"c":"(.*?)","m"')
        jia = response.xpath('.').re('"amount":(.*?),"ltsz"')
        zi = response.xpath('.').re('"tshare":(.*?),"hs"')
        lei = response.xpath('.').re('"hybk":"(.*?)"}')
        # {"c":"(.*?)","m".*?"n":"(.*?)","p":.*?"amount":(.*?),"ltsz".*?"tshare":(.*?),"hs":.*?"hybk":"(.*?)"}
        list1 = list(zip(name, dai, jia, zi, lei))
        for i in list1:
            item["name"] = i[0]
            item["dai"] = i[1]
            item["jia"] = i[2]
            item["zi"] = i[3]
            item["lei"] = i[4]
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page) + self.set_url
        yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
