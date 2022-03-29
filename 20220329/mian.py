import urllib.request
import csv
import re
import warnings
import pymysql

class qnztSpider:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="", charset="utf8")
        self.cursor = self.db.cursor()
        self.baseurl = "https://gy.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.page = 1

    def readPage(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<a.*?data-is_focus="" data-sl="">(.*?)</a>.*?<a.*?data-el="region">(.*?)</a>.*?<a.*?target="_blank">(.*?)</a>.*?<i> </i><span>(.*?)</span><i>(.*?)</i>.*?data-price=".*?"><span>(.*?)</span>', re.S)
        r_list = p.findall(html)
        self.writer(r_list)
        # print(r_list)
    def writer(self, r_list):
        c_db = 'create database if not exists 链家 charset utf8'
        u_db = 'use 链家'
        c_table = """create table if not exists lianjia(数据 int primary key auto_increment,
                            名称 varchar(100),
                            地区 varchar(200),
                            地点 varchar(100),
                            价钱 varchar(100),
                            单位 varchar(100),
                            平方 varchar(30));
                        """
        ins = 'insert into lianjia(名称,地区,地点,价钱,单位,平方)values(%s,%s,%s,%s,%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_table)
        except:
            pass

        for r_tuple in r_list:
            L = []
            for r_str in r_tuple:
                L.append(r_str.strip())
            print(L)
            # execute(ins,[列表])
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
    qnzy = qnztSpider()
    qnzy.workOn()