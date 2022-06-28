# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import warnings

import pymysql
from itemadapter import ItemAdapter


class FangtianxiaPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["jia"])
        print(item["di"])
        print(item["bao"])
        print(item["jij"])
        print(item["mian"])


class FangtianxiaPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists fang charset utf8'
        u_db = 'use fang'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                                   名称 varchar(100),
                                                   价格 varchar(200),
                                                   地点 varchar(200),
                                                   保证金 varchar(200),
                                                   加价 varchar(200),
                                                   面积 varchar(100));
                                               """
        ins = 'insert into db(名称,价格,地点,保证金,加价,面积)values(%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["jia"], item["di"], item["bao"], item["jij"], item["mian"]]
        self.cursor.execute(ins, L)
        self.db.commit()
