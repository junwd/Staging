# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GupiaoPipeline:
    def process_item(self, item, spider):
        print(item["name"])  # 名称
        print(item["dai"])  # 股票代码
        print(item["jia"])  # 成交额
        print(item["zi"])  # 总值
        print(item["lei"])  # 类型


import csv


class GupiaoPipeline_csv:
    def __init__(self):
        self.f = open("zsqb.csv", "w", newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(["名称", "股票代码", "成交额", "总值", "类型"])

    def process_item(self, item, spider):
        r_list = [item['name'], item["dai"], item["jia"], item["zi"], item["lei"]]
        self.writer.writerow(r_list)
        return item


import pymysql
import warnings


class GupiaoPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = "create database if not exists gp character set utf8"
        u_db = "use gp"
        c_tab = "create table if not exists qy1(" \
                "序号 int primary key auto_increment," \
                "名称 varchar(56)," \
                "代码 varchar(50)," \
                "成交额 varchar(30)," \
                "总值 varchar(52)," \
                "类型 varchar(23))"
        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins = 'insert into qy1(名称,代码,成交额,总值,类型) values(%s,%s,%s,%s,%s)'
        L = [item['name'], item["dai"], item["jia"], item["zi"], item["lei"]]
        self.cursor.execute(ins, L)
        self.db.commit()
