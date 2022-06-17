# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanPipeline_list:
    def process_item(self, item, spider):
        print(item["info_link"])
        print(item["pic_link"])
        print(item["cname"])
        print(item["score"])
        print(item["rated"])
        print(item["introduction"])
        print(item["year_release"])
        print(item["country"])
        print(item["category"])


import sqlite3


class DoubanPipeline:
    def __init__(self):
        self.con = sqlite3.connect('movie.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):  # REAL PRIMARY KEY
        self.cur.execute("""CREATE TABLE IF NOT EXISTS movie250(
           id TEXT, 
           info_link TEXT,
           pic_link VARCHAR,
           cname TEXT,
           score VARCHAR,
           rated VARCHAR,
           introduction TEXT,
           year_release NUMERIC,
           country VARCHAR,
           category VARCHAR
           )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO movie250 VALUES(?,?,?,?,?,?,?,?,?,?) """,  #
                         (item["id"], item["info_link"], item["pic_link"], item['cname'], item["score"], item["rated"],
                          item["introduction"], item["year_release"], item["country"], item["category"]))
        self.con.commit()
        return item
