# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 打印
# class TencentPipeline:
#     def process_item(self, item, spider):
#         print(item["name"])
#         print(item["di"])
#         print(item["pin"])
#         print(item["shi"])
# csv
# import csv
#
#
# class TencentPipeline_csv:
#     def __init__(self):
#         self.f = open("ass.csv", 'a', newline="", encoding='gb18030')
#         self.write = csv.writer(self.f)
#         self.write.writerow(["名称", "地点", "类型", "时间"])
#
#     def process_item(self, item, spider):
#         L = [item["name"], item["di"], item['pin'], item["shi"]]
#         self.write.writerow(L)
#         return item
# mysql
import warnings
import pymysql


class TencentPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists tencent charset utf8'
        u_db = 'use tencent'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                                           name varchar(200),
                                                           di varchar(200),
                                                           pin varchar(200),
                                                           shi varchar(100));
                                                       """
        ins = 'insert into db(name,di,pin,shi)values(%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["di"], item['pin'], item["shi"]]
        self.cursor.execute(ins, L)
        self.db.commit()
