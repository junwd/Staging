# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class QnzynewsPipeline(object):
    def process_item(self, item, spider):
        print("---------------------------------")
        print(item["title"])
        print(item["time"])
        print("----------------------------------")


# import csv  #写入csv
# class QnzynewsPipelin_a(object):
#     def __init__(self):
#         self.f = open("qnzynews.csv", "w")
#         self.writer = csv.writer(self.f)
#         self.writer.writerow(["title", "time"])
#
#     def process_item(self, item, spider):
#         tencent_list = [item['title'], item['time']]
#         self.writer.writerow(tencent_list)
#         return item
#
#     def close_spider(self, spider):  # 关闭
#         self.writer.close()
#         self.f.close()


#保存mysql

import pymysql
import warnings

class QnzynewsmysqlPipeline_mysql(object):
    def __init__(self):
        #创建连接对象
        self.db=pymysql.connect(host="localhost",
                           user="root",
                           password="",
                           charset="utf8")
        #创建游标对象
        self.cursor=self.db.cursor()
        #这个函数名称不能修改
    def process_item(self, item, spider):
        c_db="create database if not exists qnzynewsdb character set utf8"
        u_db="use qnzynewsdb"
        c_tab="create table if not exists news(" \
              " title varchar(50),\
                time varchar(100))charset=utf8"

        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins='insert into news values(%s,%s)'
        L=[item["title"],item["time"]]
        self.cursor.execute(ins,L)
        self.db.commit()  #提交