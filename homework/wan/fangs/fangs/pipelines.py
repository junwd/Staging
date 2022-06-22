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


import csv


class FangsPipeline_csv:
    def __init__(self):
        self.f = open("ass.csv", 'a', newline="", encoding='gb18030')
        self.write = csv.writer(self.f)
        self.write.writerow(["面积", "url", "img", "地区", "价格", "几室", "简介", "时间", "装修", "朝向"])

    def process_item(self, item, spider):
        L = [item["id"], item["info_link"], item["pic_link"], item['cname'], item["score"], item["rated"],
             item["introduction"], item["year_release"], item["country"], item["category"]]
        self.write.writerow(L)
        return item


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
        # 数据库存放位置，可自行移动到flask框架内，可设置路径到框架内
        # 框架内路径为: ./flask/movie.db ,可视化路径为./目录位置
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


import codecs, json


class FangsPipeline_json(object):
    """
    将数据保存到json文件，由于文件编码问题太多，这里用codecs打开，可以避免很多编码异常问题
        在类加载时候自动打开文件，制定名称、打开类型(只读)，编码
        重载process_item，将item写入json文件，由于json.dumps处理的是dict，所以这里要把item转为dict
        为了避免编码问题，这里还要把ensure_ascii设置为false，最后将item返回回去，因为其他类可能要用到
        调用spider_closed信号量，当爬虫关闭时候，关闭文件
    """

    def __init__(self):
        self.file = codecs.open('spiderdata.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()
