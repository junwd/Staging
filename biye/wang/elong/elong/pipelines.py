# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs
import json
import warnings

import pymysql
from itemadapter import ItemAdapter


class ElongPipeline:
    def process_item(self, item, spider):
        print(item["name"])
        print(item["pin"])
        print(item["di"])
        print(item["pnu"])
        print(item["zun"])
        print(item["jul"])
        print(item["lei"])


class ElongPipeline_json(object):
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


class ElongPipeline_mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = 'create database if not exists ylong charset utf8'
        u_db = 'use ylong'
        c_table = """create table if not exists lo(编号 int primary key auto_increment,
                                                                   酒店名 varchar(100),
                                                                   评分 varchar(200),
                                                                   地点 varchar(200),
                                                                   评论 varchar(200),
                                                                   装修风格 varchar(200),
                                                                   距离 varchar(100),
                                                                   类型 varchar(200));
                                                               """
        ins = 'insert into lo(酒店名,评分,地点,评论,装修风格,距离,类型)values(%s,%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        L = [item["name"], item["pin"], item["di"], item["pnu"], item["zun"], item["jul"], item["lei"]]
        self.cursor.execute(ins, L)
        self.db.commit()
