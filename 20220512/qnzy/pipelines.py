# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class QnzyPipeline:
    def process_item(self, item, spider):
        print(item["bia"])
        print(item["bio"])
        print(item["lei"])
        print(item["shi"])
        print(item["hui"])
        print(item["zha"])
