import requests
from lxml import etree
import warnings
import pymysql
import csv


class baiduSpider:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="", charset="utf8")
        self.cursor = self.db.cursor()
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.baseurl = "https://www.liepin.com/zhaopin/?headId&currentPage="
        self.page = 1

    def readPage(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        html = response.text
        self.paserPage(html)

    def paserPage(self, html):
        parsehtml = etree.HTML(html)
        r_list = parsehtml.xpath('//div[@class="job-title-box"]/div[1]/text()')
        r_list1 = parsehtml.xpath('//div[@class="job-dq-box"]/span[2]/text()')
        r_list2 = parsehtml.xpath('//div[@class="job-detail-header-box"]/span[1]/text()')
        r_list3 = parsehtml.xpath('//div[@class="job-labels-box"]/span[2]/text()')
        list = []
        for i in range(len(r_list1)):
            new_list = [r_list[i], r_list1[i], r_list2[i], r_list3[i]]
            list.append(new_list)
        self.weit(list)
        self.csv(list)
    def csv(self,list):
        with open("ass.csv", 'a', newline="", encoding="gb18030") as f:
            writer = csv.writer(f)
            writer.writerow(["职位", "地区","薪资","学历"])
        for r_tup in list:
            with open("ass.csv", 'a', newline="", encoding="gb18030") as f:
                writer = csv.writer(f)
                writer.writerow(r_tup)

    def weit(self, list):
        c_db = 'create database if not exists liepin charset utf8'
        u_db = 'use liepin'
        c_table = """create table if not exists lie(数据 int primary key auto_increment,
                                   职位 varchar(200),
                                   地区 varchar(200),
                                   薪资 varchar(200),
                                   学历 varchar(200));
                               """
        ins = 'insert into lie(职位,地区,薪资,学历)values(%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        for r_tuple in list:
            L = []
            for r_str in r_tuple:
                L.append(r_str.strip())
            print(L)
            self.cursor.execute(ins, L)
            self.db.commit()
            print('存入数据库成功')

    def workOn(self):

        begin = int(input("请输入开始页："))
        end = int(input("请输入结束页："))
        for i in range(begin, end + 1):
            self.page = i
            url = self.baseurl + str(self.page)
            self.readPage(url)


if __name__ == "__main__":
    baidu = baiduSpider()
    baidu.workOn()
