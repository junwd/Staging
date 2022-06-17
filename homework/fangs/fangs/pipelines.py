# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FangsPipeline:
    def process_item(self, item, spider):
        print(item["id"])
        print(item["info_link"])
        print(item["pic_link"])
        print(item["cname"])
        print(item["score"])
        print(item["rated"])
        print(item["introduction"])
        print(item["year_release"])
        print(item["country"])
        print(item["category"])


import warnings
import pymysql


class FangsPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists edu charset utf8'
        u_db = 'use edu'
        c_table = """create table if not exists rentanalysis(编号 int primary key auto_increment,
                                                          id varchar(300),
                                                          info_link varchar(300),
                                                          pic_link varchar(300),
                                                          cname varchar(300),
                                                          score varchar(300),
                                                          rated varchar(300),
                                                          introduction varchar(300),
                                                          year_release varchar(300),
                                                          country varchar(300),
                                                          category varchar(300));
                                                      """
        ins = 'insert into rentanalysis(id,info_link,pic_link,cname,score,rated,' \
              'introduction,year_release,country,category)' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["id"], item["info_link"], item["pic_link"], item['cname'], item["score"], item["rated"],
             item["introduction"], item["year_release"], item["country"], item["category"]]
        self.cursor.execute(ins, L)
        self.db.commit()


import sqlite3


class FangsPipeline_SQLite:
    def __init__(self):
        self.con = sqlite3.connect('movie.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):  # REAL PRIMARY KEY
        self.cur.execute("""CREATE TABLE IF NOT EXISTS movie250(
           id VARCHAR, 
           info_link VARCHAR,
           pic_link VARCHAR,
           cname TEXT,
           score VARCHAR,
           rated TEXT,
           introduction TEXT,
           year_release VARCHAR,
           country VARCHAR,
           category VARCHAR
           )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO movie250 VALUES(?,?,?,?,?,?,?,?,?,?) """,
                         (item["id"], item["info_link"], item["pic_link"], item['cname'], item["score"], item["rated"],
                          item["introduction"], item["year_release"], item["country"], item["category"]))
        self.con.commit()
        return item
