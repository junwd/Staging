# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DeinsPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print("*"*30)
        print(item["hao"])
