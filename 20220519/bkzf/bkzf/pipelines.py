# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import warnings
import pymysql


class BkzfPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["zo"])
        print(item["jia"])
        print(item["mia"])


class BkzfPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists bkzf charset utf8'
        u_db = 'use bkzf'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                                   name varchar(200),
                                                   zo varchar(200),
                                                   jia varchar(200),
                                                   mia varchar(100));
                                               """
        ins = 'insert into db(name,zo,jia,mia)values(%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["zo"], item['jia'], item["mia"]]
        self.cursor.execute(ins, L)
        self.db.commit()
