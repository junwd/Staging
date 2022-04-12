import requests
import warnings
import pymysql
import json

class deins:
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", charset="utf8")
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
            list1 = ([mimi["title"]])
            list2 = (mimi["regions"])
            list3 = ([mimi["rating"][0]])
            list = []
            for i in range(len(list1)):
                new_list = [list1[i], list2[i], list3[i]]
                list.append(new_list)
            self.sjk(list)

    def sjk(self, list):
        print(list)
        c_db = 'create database if not exists duo charset utf8'
        u_db = 'use duo'
        c_table = """create table if not exists db(编号 int primary key auto_increment,
                                            名称 varchar(100),
                                            地区 varchar(200),
                                            评分 varchar(100));
                                        """
        ins = 'insert into db(名称,地区,评分)values(%s,%s,%s)'
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

    L = ["剧情", "喜剧", "动作", "爱情", "科幻", "动画", "悬疑", "惊悚", "恐怖", "纪录片", "短片", "情色", "音乐", "歌舞", "家庭", "儿童", "传记",
         "历史", "战争", "犯罪", "西部", "奇幻", "冒险", "灾难", "武侠", "古装", "运动", "黑色电影"]
    tp_list = [{"剧情": "11"}, {"喜剧": "24"}, {"动作": "5"}, {"爱情": "13"}, {"科幻": "17"}, {"动画": "25"}, {"悬疑": "10"},
               {"惊悚": "19"}, {"恐怖": "20"}, {"纪录片": "1"}, {"短片": "23"}, {"情色": "6"}, {"音乐": "14"}, {"歌舞": "7"},
               {"家庭": "7"}, {"儿童": "8"}, {"传记": "2"}, {"历史": "4"}, {"犯罪": "3"}, {"西部": "27"}, {"奇幻": "16"},
               {"武侠": "29"}, {"古装": "30"}, {"运动": "18"}, {"黑色电影": "31"}]
    tp = input("请你输入要爬取的电影类型：")
    for fiml_dict in tp_list:
        for key, value in fiml_dict.items():
            if tp == key:
                num = input("请输入要爬取的数量：")
                params = {
                    "type": value,
                    "interval_id": "100:90",
                    "action": "",
                    "start": "0",
                    "limit": num
                }


if __name__ == "__main__":
    junwd = deins()
    junwd.workOn()
