# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Top500Pipeline:
    def process_item(self, item, spider):
        print(item["pai"])
        print(item["name"])
        print(item["ge"])
        print(item["shi"])


import warnings
import pymysql


class Top500Pipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists top500 charset utf8'
        u_db = 'use top500'
        c_table = """create table if not exists kg(排名 varchar(300),
                                                   歌手 varchar(300),
                                                   歌名 varchar(300),
                                                   时长 varchar(300));
                                                   """
        ins = 'insert into kg(排名,歌手,歌名,时长)''values(%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["pai"], item["name"], item["ge"], item["shi"]]
        self.cursor.execute(ins, L)
        self.db.commit()

import csv


class Top500Pipeline_csv:
    def __init__(self):
        self.f = open("ass.csv", 'a', newline="", encoding='gb18030')
        self.write = csv.writer(self.f)
        self.write.writerow(["排名", "歌手", "歌名", "时间"])

    def process_item(self, item, spider):
        L = [item["pai"], item["name"], item["ge"], item["shi"]]
        self.write.writerow(L)
        return item