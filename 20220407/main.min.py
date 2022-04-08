import requests
import warnings
import pymysql
import json


class deins:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="", charset="utf8")
        self.cursor = self.db.cursor()
        self.baseurl = "https://movie.douban.com/j/chart/top_list?"
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def qingqiu(self, url):
        res = requests.get(url, params=self.params, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        html2 = json.loads(html)
        self.day(html2)

    def day(self, html2):
        for mimi in html2:
            name = mimi["title"]
            country = mimi["regions"]
            score = mimi["rating"][0]
            # M = [name, country, score]
            list1 =([mimi["title"]])
            list2=(mimi["regions"])
            list3=([mimi["rating"][0]])
            list = []
            for i in range(len(list1)):
                new_list = [list1[i], list2[i],list3[i]]
                list.append(new_list)
            self.sjk(list)

    def sjk(self, list):
        c_db = 'create database if not exists duo charset utf8'
        u_db = 'use duo'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                    名称 varchar(100),
                                    地区 varchar(200),
                                    评分 varchar(100));
                                """
        ins = 'insert into db(名称,地区,地点)values(%s,%s,%s)'
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
            # execute(ins,[列表])
            self.cursor.execute(ins, L)
            self.db.commit()
            print('存入数据库成功')

    def workOn(self):
        url = self.baseurl
        self.qingqiu(url)

    num = input("请输入要获取的电影数量：")
    params = {
        "type": "11",
        "interval_id": "100:90",
        "action": "",
        "start": "0",
        "limit": num
    }


if __name__ == "__main__":
    junwd = deins()
    junwd.workOn()
