# 检查作业：作业讲解——《黔南民族职业技术学院》

# 链接数据库---------------------------------------------------------
# 示例1
'''创建一个库spiderdb ,创建表t1,插入1条记录'''
import pymysql
# 1、创建数据库连接对象
# db=pymysql.connect(host="localhost",user="root",password="",charset="utf8")
# #2、创建游标对象
# cursor=db.cursor()
# #3、执行语句
# cursor.execute("create database if not exists spiderdb4 character set utf8")
# cursor.execute("use spiderdb4")
# cursor.execute("create table if not exists t2(id int,name varchar(20))")
# ins="insert into t2 values(%s,%s)"
# cursor.execute(ins,[1,"zhangs"])
# # cursor.execute(ins,[2])
# #4、提交
# db.commit()
# #5、关闭
# cursor.close()  #关闭游标
# db.close()   #关闭数据库
#

# 示例2
# import pymysql
# import warnings
# #创建数据库连接对象
# db=pymysql.connect("localhost","root","password",charset="utf8")
# #创建游标对象
# cursor=db.cursor()
# #执行语句
# warnings.filterwarnings("ignore")
# try:
#     cursor.execute("create database if not exists spiderdb")
#     cursor.execute("use spiderdb")
#     cursor.execute("create table if not exists t1(id int)")
# except Warning:
#     pass
# ins="insert into t1 values(%s)"
# cursor.execute(ins,[1])
# cursor.execute(ins,[2])
# #提交
# db.commit()
# #关闭
# cursor.close()
# db.close()

# 案例项目：爬取链家二手房信息-->存到Mysql数据库中
import requests
import re
import csv
import pymysql
from lxml import etree
import warnings


class Lianjiaspider:
    def __init__(self):
        self.baseurl = "https://bj.lianjia.com/ershoufang/pg"
        self.page = 1
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.db = pymysql.connect(host="localhost", user="root", password="", charset="utf8")
        self.cursor = self.db.cursor()

    def getPage(self, url):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # print(html)
        self.parsePage(html)

    def parsePage(self, html):
        s = []
        parsehtml = etree.HTML(html)
        r_list1 = parsehtml.xpath('//*[@class="sellListContent"]/li/div/div[2]/div/a/text()')
        r_list2 = parsehtml.xpath('//*[@class="sellListContent"]/li/div/div[2]/div/a[2]/text()')
        r_list3 = parsehtml.xpath('//*[@class="sellListContent"]/li/div/div[6]/div[1]/span/text()')
        r_list4 = parsehtml.xpath('//*[@class="sellListContent"]/li/div/div[6]/div[2]/span/text()')
        for x in range(0, len(r_list4)):
            newlist = [r_list1[x], r_list2[x], r_list3[x], r_list4[x]]
            s.append(newlist)
        print(s)
        print("页面解析成功，正在存入数据库")
        # self.writeTomysql(s)

    def writeTomysql(self, r_list):
        c_db = "create database if not exists lianjiaspider character set utf8"
        u_db = "use lianjiaspider"
        c_tab = "create table if not exists housePrice(id int primary key auto_increment,\
                housename varchar(50),\
                totalprice int," \
                "price varchar(50))charset=utf8"

        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins = "insert into houseprice(housename,totalprice,price) values(%s,%s,%s)"
        for r_tuple in r_list:
            name = r_tuple[0].strip()
            totalprice = float(r_tuple[2].strip()) * 10000
            price = r_tuple[3]
            L = [name, totalprice, price]
            self.cursor.execute(ins, L)
            self.db.commit()
            # self.cursor.close()
            # self.db.close()

    def workOn(self):
        begin = int(input("开始页："))
        end = int(input("结束页："))
        for i in range(begin, end + 1):
            self.page = i
            url = self.baseurl + str(self.page) + "/"
            print(url)
            self.getPage(url)


if __name__ == "__main__":
    spider = Lianjiaspider()
    spider.workOn()
