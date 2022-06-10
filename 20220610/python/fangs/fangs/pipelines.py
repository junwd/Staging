# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FangsPipeline:
    def process_item(self, item, spider):
        print(item["district"])
        print(item["title"])
        print(item["bedroom"])
        print(item["area"])
        print(item["direction"])
        print(item["decoration"])
        print(item["total_price"])
        print(item["unit_price"])
        print(item["add_date"])
        print(item["mod_date"])


import warnings
import pymysql


class FangsPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists edu charset utf8'
        u_db = 'use edu'
        c_table = """create table if not exists rentanalysis_rent(编号 int primary key auto_increment,
                                                          district varchar(200),
                                                          title varchar(200),
                                                          bedroom varchar(200),
                                                          area varchar(200),
                                                          direction varchar(200),
                                                          decoration varchar(200),
                                                          total_price varchar(200),
                                                          unit_price varchar(200),
                                                          add_date varchar(200),
                                                          mod_date varchar(100));
                                                      """
        ins = 'insert into rentanalysis_rent(district,title,bedroom,area,direction,decoration,' \
              'total_price,unit_price,add_date,mod_date)' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["district"], item["title"], item["bedroom"], item["area"], item['direction'], item["decoration"],
             item["total_price"], item["unit_price"],
             item['add_date'], item["mod_date"]]
        self.cursor.execute(ins, L)
        self.db.commit()
