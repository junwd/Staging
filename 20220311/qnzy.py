import re
import urllib.request
import urllib.parse
import csv


class cscsd:
    def __init__(self):
        self.baseurl = "http://www.qnzy.net/list.jsp?cItemId=44&itemId=2&"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}

    def readPage(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<li.*?href.".*itemId=44">(.*?)</a>.*class="time".*?">(.*?)</span>', re.S)
        r_list = p.findall(html)
        self.WriterPage(r_list)
        print(r_list)

    def WriterPage(self, r_list):
        with open("python作业.csv", 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(r_list)

    def workon(self):
        for n in range(1, 300):
            pn = (n * 1)
            url = self.baseurl + "&page=" + str(pn)
            self.readPage(url)


if __name__ == "__main__":
    spider = spider = cscsd()
    spider.workon()
