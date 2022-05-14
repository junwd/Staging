# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class QnzyPipeline:
#     def process_item(self, item, spider):
#         print(item["number"])
#         print(item["name"])
#         print(item['type'])
#         print(item["time"])
#         print(item["Company"])
#         print(item['reply'])
#

import csv


class QnzyPipeline:
    def __init__(self):
        self.f = open("ass.csv", 'a', newline="", encoding='gb18030')
        self.write = csv.writer(self.f)
        self.write.writerow(["编号", "主题", "类型", "时间", "单位", "回复", ])

    def process_item(self, item, spider):
        L = [item["number"], item["name"], item['type'],
             item["time"], item["Company"], item['reply']
             ]

        self.write.writerow(L)
        return item
