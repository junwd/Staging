import urllib.request
import csv
import re

class qnztSpider:
    def __init__(self):
        self.baseurl = "https://gy.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.page = 1

    def readPage(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<a.*?data-is_focus="" data-sl="">(.*?)</a>.*?<a.*?data-el="region">(.*?).*?<a.*?target="_blank">(.*?)</a>.*?<i> </i><span>(.*?)</span><i>(.*?)</i>.*?data-price=".*?"><span>(.*?)</span>', re.S)
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