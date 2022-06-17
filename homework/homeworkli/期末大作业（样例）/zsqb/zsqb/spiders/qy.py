import scrapy
from zsqb.items import ZsqbItem

class QySpider(scrapy.Spider):
    name = 'qy'
    allowed_domains = ['s.askci.com']
    # start_urls = ['https://s.askci.com/stock/a/0-0?reportTime=2021-03-31&pageNum=1#QueryCondition']
    url = 'https://s.askci.com/stock/a/0-0?reportTime=2021-03-31&pageNum='
    set_page = 1
    start_urls = [url + str(set_page) + '#QueryCondition']
    def parse(self, response):
        item=ZsqbItem()
        conts=response.xpath('//tbody/tr')
        for cont in conts:
            item['name']=cont.xpath('./td[4]/text()').extract()[0]      #"公司名称
            item['sf']=cont.xpath('./td[5]/text()').extract()[0]        #"省份"
            item['cs']=cont.xpath('./td[6]/text()').extract()[0]        #"城市"
            item['sr'] = cont.xpath('./td[7]/text()').extract()[0]      #"营业收入"
            item['lr'] = cont.xpath('./td[8]/text()').extract()[0]      #"利润
            item['rs'] = cont.xpath('./td[9]/text()').extract()[0]      #员工人数
            item['time'] = cont.xpath('./td[10]/text()').extract()[0]   #上市日期
            item['fl'] = cont.xpath('./td[13]/text()').extract()[0]     #行业分类
            item['lx'] = cont.xpath('./td[14]/text()').extract()[0]     #产品类型
            yield item
        if self.set_page<220:
            print("第" + str(self.set_page) + "页爬取成功")
            self.set_page += 1
            next_url = self.url + str(self.set_page) + '#QueryCondition'
        else:
            print("爬取完成")
        yield scrapy.Request(next_url, callback=self.parse)
