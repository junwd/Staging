import json
import scrapy
from elong.items import ElongItem


class YlSpider(scrapy.Spider):
    name = 'yl'
    allowed_domains = ['elong.com']
    start_urls = [
        f'https://hotel.elong.com/tapi/v2/list?pageSize=20&t=1661868330108&city=0201&inDate=2022-08-30&outDate=2022-08-31&filterList=8888_{i}&pageIndex=0&sugActInfo=' for i in range(1, 20)]

    def parse(self, response):
        content = json.loads(response.body.decode())
        # print(content)
        jobs = content['data']['hotelList']
        for job in jobs:
            item = ElongItem()
            item["name"] = job['hotelName']  # 名称
            item["pin"] = job['commentScore']  # 评分
            item["di"] = job['hotelAddress']  # 地点
            item["pnu"] = job['commentCount']  # 评论
            item["zun"] = job['commentMainTag']  # 装修风格
            item["jul"] = job['trafficInfo']  # 距离
            item["lei"] = job['starLevelDes']  # 类型
            yield item
