# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import sqlite3
import warnings
import pymysql
from itemadapter import ItemAdapter


class BeikePipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["jia"])
        print(item["zul"])
        print(item["lei"])
        print(item["chao"])
        print(item["mian"])
        print(item["lou"])
        print(item["shui"])
        print(item["dian"])
        print(item["zuq"])
        print(item["ran"])
        print(item["ti"])
        print(item["che"])


class BeikePipeline_csv:
    def process_item(self, item, spider):
        def __init__(self):
            self.f = open("bk.csv", 'a', newline="", encoding='gb18030')
            self.write = csv.writer(self.f)
            self.write.writerow(["房名", "价格", "租赁方式", "房屋类型", "房屋朝向", "面积", "楼层", "用水", "用电", "租期", "燃气", "电梯", "车位"])

        def process_item(self, item, spider):
            L = [item["name"], item["jia"], item["zul"], item["lei"], item["chao"], item["mian"], item["lou"],
                 item["shui"], item["dian"], item["zuq"], item["ran"], item["ti"], item["che"]]
            self.write.writerow(L)
            return item


class BeikePipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists beike charset utf8'
        u_db = 'use beike'
        c_table = """create table if not exists bk(编号 int primary key auto_increment,
                                                           房名 varchar(100),
                                                           价格 varchar(200),
                                                           租赁方式 varchar(200),
                                                           房屋类型 varchar(200),
                                                           房屋朝向 varchar(200),
                                                           面积 varchar(100),
                                                           楼层 varchar(200),
                                                           用水 varchar(200),
                                                           用电 varchar(200),
                                                           租期 varchar(200),
                                                           燃气 varchar(100),
                                                           电梯 varchar(200),
                                                           车位 varchar(200));
                                                       """
        ins = 'insert into bk(房名,价格,租赁方式,房屋类型,房屋朝向,面积,楼层,用水,用电,租期,燃气,电梯,车位)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,' \
              '%s,%s) '
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["jia"], item["zul"], item["lei"], item["chao"], item["mian"], item["lou"], item["shui"],
             item["dian"], item["zuq"], item["ran"], item["ti"], item["che"]]
        self.cursor.execute(ins, L)
        self.db.commit()


import codecs, json


class BeikePipeline_json(object):
    """
    将数据保存到json文件，由于文件编码问题太多，这里用codecs打开，可以避免很多编码异常问题
        在类加载时候自动打开文件，制定名称、打开类型(只读)，编码
        重载process_item，将item写入json文件，由于json.dumps处理的是dict，所以这里要把item转为dict
        为了避免编码问题，这里还要把ensure_ascii设置为false，最后将item返回回去，因为其他类可能要用到
        调用spider_closed信号量，当爬虫关闭时候，关闭文件
    """

    def __init__(self):
        self.file = codecs.open('beike.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class BeikePipeline_SQLite:
    def __init__(self):
        self.con = sqlite3.connect('beike.db')
        # 数据库存放位置，可自行移动到flask框架内，可设置路径到框架内
        # 框架内路径为: ./flask/movie.db ,可视化路径为./目录位置
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):  # REAL PRIMARY KEY
        self.cur.execute("""CREATE TABLE IF NOT EXISTS bk(
           房名 VARCHAR, 
           价格 VARCHAR,
           租赁方式 VARCHAR,
           房屋类型 TEXT,
           房屋朝向 VARCHAR,
           面积 TEXT,
           楼层 TEXT,
           用水 VARCHAR,
           用电 VARCHAR,
           租期 VARCHAR,
           燃气 VARCHAR,
           电梯 VARCHAR,
           车位 VARCHAR
           )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO bk VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) """,
                         (item["name"], item["jia"], item["zul"], item["lei"], item["chao"], item["mian"], item["lou"],
                          item["shui"], item["dian"], item["zuq"], item["ran"], item["ti"], item["che"]))
        self.con.commit()
        return item
