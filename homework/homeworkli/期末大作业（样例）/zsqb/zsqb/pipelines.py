# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

#
# class ZsqbPipeline:
#     def process_item(self, item, spider):
        # return item
        # print('='*100)
        # print(item['name'])
        # print(item['sf'])
        # print(item['cs'])
        # print(item['sr'])
        # print(item['lr'])
        # print(item['rs'])
        # print(item['time'])
        # print(item['fl'])
        # print(item['lx'])
        # print('=' * 100)




import csv
class zs(object):
    def __init__(self):
        self.f=open("zsqb.csv","w",newline='')
        self.writer=csv.writer(self.f)
        self.writer.writerow(["公司名称","省份","城市","营业收入","利润","员工人数","上市日期","行业分类","产品类型"])

    def process_item(self, item, spider):
        r_list = [item['name'],item['sf'],item['cs'], item['sr'],item['lr'],item['rs'],item['time'],item['fl'],item['lx']]
        self.writer.writerow(r_list)
        return item



import pymysql
import warnings
class zsqb(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        c_db="create database if not exists zsqb character set utf8"
        u_db="use zsqb"
        c_tab="create table if not exists qy1("\
              "序号 int primary key auto_increment," \
              "公司名称 varchar(56)," \
              "省份 varchar(50)," \
              "城市 varchar(30)," \
              "营业收入 varchar(52)," \
              "利润 varchar(23)," \
              "员工人数 varchar(20)," \
              "上市日期 varchar(26)," \
              "行业分类 varchar(32)," \
              "产品类型 varchar(60))"
        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins='insert into qy1(公司名称,省份,城市,营业收入,利润,员工人数,上市日期,行业分类,产品类型) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        L=[item['name'],item['sf'],item['cs'], item['sr'],item['lr'],item['rs'],item['time'],item['fl'],item['lx']]
        self.cursor.execute(ins,L)
        self.db.commit()