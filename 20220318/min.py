
#练习1：
# 1.改写代码，用requests模块实现
# 2.链家二手房
#  网址：https://bj.lianjia.com/ershoufang/pg1/
#3.百度搜索--链家二手房--->二手房
#4.爬取：小区名称、总价

import requests
import csv
import re

class qnztSpider:
    def __init__(self):
        self.baseurl = "https://gy.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.page = 1

    def readPage(self, url):
        # req = urllib.request.Request(url, headers=self.headers)
        # res = urllib.request.urlopen(req)
        # html = res.read().decode("utf-8")
        req = requests.get(url, headers=self.headers)
        req.encoding = "utf-8"
        html = req.text
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<a.*?data-is_focus="" data-sl="">(.*?)</a>.*?<i>.*?</i><span>(.*?)</span><i>(.*?)</i>', re.S)
        r_list = p.findall(html)
        self.writer(r_list)

    def writer(self, r_list):

        if self.page == 1:
            with open("qnzy.csv", 'a', newline="", encoding="gb18030") as f:
                writer = csv.writer(f)
                writer.writerow(["地点", "地区","地点", "地区"])
        for r_tup in r_list:

            with open("qnzy.csv", 'a', newline="", encoding="gb18030") as f:
                writer = csv.writer(f)
                writer.writerow(r_tup)

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