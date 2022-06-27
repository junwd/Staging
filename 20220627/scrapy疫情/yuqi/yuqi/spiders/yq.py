import json
import re

import scrapy
from yuqi.items import YuqiItem


class YqSpider(scrapy.Spider):
    name = 'yq'
    allowed_domains = ['yq.com']
    start_urls = ['https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner']

    def parse(self, response):

        html_data = response.text
        json_str = re.findall('"component":\[(.*)\],', html_data)[0]  # 字符串
        # 字典类型取值, 转类型
        json_dict = json.loads(json_str)
        caseList = json_dict['caseList']
        # print(caseList)
        for case in caseList:
            area = case['area']  # 城市
            curConfirm = case['curConfirm']  # 当前确诊
            curConfirmRelative = case['curConfirmRelative']  # 新增人数
            confirmed = case['confirmed']  # 累计确诊
            crued = case['crued']  # 治愈人数
            died = case['died']  # 死亡人数
            # print(area, curConfirm, curConfirmRelative, confirmed, crued, died)
            item = YuqiItem()
            item["area"] = area
            item["curConfirm"] = curConfirm
            item["curConfirmRelative"] = curConfirmRelative
            item["confirmed"] = confirmed
            item["crued"] = crued
            item["died"] = died
            yield item
