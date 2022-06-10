# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PchomePipeline:
    def process_item(self, item, spider):
        print(item["phone"])
        print(item["Price"])
        print(item["battery"])
        print(item["memory"])
        print(item["shi"])
        print(item["pixel"])
        print(item["cpu"])


import warnings
import pymysql


class PchomePipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists sj charset utf8'
        u_db = 'use sj'
        c_table = """create table if not exists rentanalysis_rent(编号 int primary key auto_increment,
                                                                  Phone varchar(200),
                                                                  Price varchar(200),
                                                                  battery varchar(200),
                                                                  memory varchar(200),
                                                                  shi varchar(200),
                                                                  pixel varchar(200),
                                                                  cpu varchar(200));
                                                              """
        ins = 'insert into rentanalysis_rent(Phone,Price,battery,memory,shi,pixel,cpu)values(%s,%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["Phone"], item["Price"], item["battery"], item['memory'], item["shi"],
             item["pixel"], item["cpu"]]
        self.cursor.execute(ins, L)
        self.db.commit()
