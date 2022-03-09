# 1,class 方法
import urllib.request
import urllib.parse
import re


class BaiduSpider:
    def __init__(self):
        self.baseurl = "https://image.baidu.com/"
        self.headers = {"User-Agent": "Mozilla/5.0"}


    def readPage(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<a.*?class="query-link">(.*?)</a>', re.S)
        r_list = p.findall(html)
        print(r_list)

    def workOn(self):
        url = self.baseurl
        self.readPage(url)


if __name__ == "__main__":
    spder = BaiduSpider()
    spder.workOn()
