# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TupPipeline:
    def process_item(self, item, spider):
        pass


import scrapy
from scrapy.pipelines.images import ImagesPipeline


class TupPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imageLink = "http://pic.netbian.com" + item['imgurl']
        yield scrapy.Request(imageLink)
