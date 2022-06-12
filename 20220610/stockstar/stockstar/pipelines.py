# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StockstarPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["shi"])

import warnings
import pymysql

class StockstarPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()


    def process_item(self, item, spider):
        c_db = 'create database if not exists stockstar charset utf8'
        u_db = 'use stockstar'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                                              name varchar(200),
                                                              shi varchar(200));
                                                          """
        ins = 'insert into db(name,shi)values(%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["shi"]]
        self.cursor.execute(ins, L)
        self.db.commit()