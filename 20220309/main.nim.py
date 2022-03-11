# 1,class 方法
import urllib.request
import urllib.parse
import re


class BaiduSpider:
    def __init__(self):
        self.baseurl = "http://www.qnzy.net/list.jsp?cItemId=44&itemId=2"
        self.headers = {"User-Agent": "Mozilla/5.0"}


    def readPage(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<li.*?href.".*itemId=44">(.*?)</a>.*class="time".*?">(.*?)</span>', re.S)
        r_list = p.findall(html)
        print(r_list)

    def workOn(self):
        url = self.baseurl
        self.readPage(url)


if __name__ == "__main__":
    spder = BaiduSpider()
    spder.workOn()
