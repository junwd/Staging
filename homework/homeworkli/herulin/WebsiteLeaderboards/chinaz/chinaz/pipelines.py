# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ChinazPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["pai"])
        print(item["wang"])
        print(item["fan"])
        print(item["tui"])


import csv


class ChinazPipeline_csv:
    def __init__(self):
        self.f = open("ass.csv", 'a', newline="", encoding='gb18030')
        self.write = csv.writer(self.f)
        self.write.writerow(["名称", "排名", "网站", "反链", "推荐"])

    def process_item(self, item, spider):
        L = [item["name"], item["pai"], item['wang'], item["fan"], item["tui"]]
        self.write.writerow(L)
        return item


import warnings
import pymysql


class ChinazPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists gen charset utf8'
        u_db = 'use gen'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                                   name varchar(200),
                                                   pai varchar(200),
                                                   wang varchar(200),
                                                   fan varchar(100),
                                                   tui varchar(100));
                                               """
        ins = 'insert into db(name,pai,wang,fan,tui)values(%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["pai"], item['wang'], item["fan"], item["tui"]]
        self.cursor.execute(ins, L)
        self.db.commit()
