# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import warnings

import pymysql
from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["rate"])
        print(item["id"])
        print(item["cover_x"])


import csv
class DoubanPipeline_csv:
    def __init__(self):
        self.f = open("doubna.csv", 'a', newline="", encoding='gb18030')
        self.write = csv.writer(self.f)
        self.write.writerow(["名称", "评分", "id", "人气"])

    def process_item(self, item, spider):
        L = [item["name"], item["rate"], item['id'],
             item["cover_x"]]
        self.write.writerow(L)
        return item


class DoubanPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists Doub charset utf8'
        u_db = 'use Doub'
        c_table = """create table if not exists DB(编号 int primary key auto_increment,
                                                    name varchar(100),
                                                    rate varchar(200),
                                                    id varchar(200),
                                                    cover_x varchar(200));
                                                """
        ins = 'insert into DB(name,rate,id,cover_x)values(%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["rate"], item['id'],
             item["cover_x"]]
        self.cursor.execute(ins, L)
        self.db.commit()
