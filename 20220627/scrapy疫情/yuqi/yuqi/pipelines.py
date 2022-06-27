# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import warnings

import pymysql
from itemadapter import ItemAdapter


# class YuqiPipeline:
#     def process_item(self, item, spider):
#         print(item["area"])
#         print(item["curConfirm"])
#         print(item["curConfirmRelative"])
#         print(item["confirmed"])
#         print(item["crued"])
#         print(item["died"])


class YuqiPipeline_csv:
    def __init__(self):
        self.f = open("yuqi.csv", 'a', newline="", encoding='gb18030')
        self.write = csv.writer(self.f)
        self.write.writerow(["城市", "当前确诊", "新增人数", "累计确诊", "治愈人数", "死亡人数"])

    def process_item(self, item, spider):
        L = [item["area"], item["curConfirm"], item["curConfirmRelative"], item["confirmed"], item["crued"],
             item["died"]]

        self.write.writerow(L)
        return item


class YuqiPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists yuqi charset utf8'
        u_db = 'use yuqi'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                                   城市 varchar(100),
                                                   当前确诊 varchar(200),
                                                   新增人数 varchar(200),
                                                   累计确诊 varchar(200),
                                                   治愈人数 varchar(200),
                                                   死亡人数 varchar(100));
                                               """
        ins = 'insert into db(城市,当前确诊,新增人数,累计确诊,治愈人数,死亡人数)values(%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["area"], item["curConfirm"], item["curConfirmRelative"], item["confirmed"], item["crued"],
             item["died"]]
        self.cursor.execute(ins, L)
        self.db.commit()
