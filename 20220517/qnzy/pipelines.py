# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class QnzyPipeline:
#     def process_item(self, item, spider):
#         print(item["number"])
#         print(item["name"])
#         print(item['type'])
#         print(item["time"])
#         print(item["Company"])
#         print(item['reply'])
#

import csv


class QnzyPipeline:
    def __init__(self):
        self.f = open("ass.csv", 'a', newline="", encoding='gb18030')
        self.write = csv.writer(self.f)
        self.write.writerow(["编号", "主题", "类型", "时间", "单位", "回复", ])

    def process_item(self, item, spider):
        L = [item["number"], item["name"], item['type'],
             item["time"], item["Company"], item['reply']
             ]

        self.write.writerow(L)
        return item


import warnings
import pymysql


class QnzyPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists qnzy charset utf8'
        u_db = 'use qnzy'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                            number varchar(100),
                                            name varchar(200),
                                            type varchar(200),
                                            time varchar(200),
                                            Company varchar(200),
                                            reply varchar(100));
                                        """
        ins = 'insert into db(number,name,type,time,Company,reply)values(%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["number"], item["name"], item['type'],
             item["time"], item["Company"], item['reply']
             ]
        self.cursor.execute(ins, L)
        self.db.commit()
