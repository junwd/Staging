import re
import urllib.request
import urllib.parse
import csv

class hudongjiaoliuSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
        self.baseurl="http://www.qnzy.net/list.jsp?cItemId=44&itemId"

    def readpage(self,url):
        req=urllib.request.Request(url,headers=self.headers)
        res=urllib.request.urlopen(req)
        html=res.read().decode("utf-8")
        self.paserPage(html)

    def paserPage(self, html):
        p = re.compile('<li.*?href.".*itemId=44">(.*?)</a>.*class="time".*?">(.*?)</span>', re.S)
        r_list = p.findall(html)
        print(r_list)
        self.warepage(r_list)

    def warepage(self, r_list):

        for r_tuple in r_list:
            with open("黔南职院.csv", "a", newline="") as f:
                writer = csv.writer(f)
                L = list(r_tuple)
                L = [r_tuple[0].strip(), r_tuple[1].strip()]
                writer.writerow(L)

    def workon(self):
        for n in range(1, 300):
            pn = (n * 1)
            url = self.baseurl + "&page=" + str(pn)
            self.readpage(url)

if __name__=="__main__":
    spider=hudongjiaoliuSpider()
    spider.workon()
