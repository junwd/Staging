import requests
import csv
import re


class qnztSpider:
    def __init__(self):
        self.baseurl = "https://movie.douban.com/top250?start=25&filter="
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def readPage(self, url):
        # req = urllib.request.Request(url, headers=self.headers)
        # res = urllib.request.urlopen(req)
        # html = res.read().decode("utf-8")
        req = requests.get(url, headers=self.headers)
        req.encoding = "utf-8"
        html = req.text
        # print(html)
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<div class="bd">.*?<br>(.*?)</p>', re.S)
        r_list = p.findall(html)
        self.writer(r_list)

    def writer(self, r_list):
        print(r_list[1])

    def workOn(self):
        url = self.baseurl
        self.readPage(url)


if __name__ == "__main__":
    qnzy = qnztSpider()
    qnzy.workOn()
