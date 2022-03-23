import requests
from lxml import etree
import csv


class baiduSpider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.baseurl = "http://www.baidu.com"

    def readPage(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        html = response.text
        self.paserPage(html)

    def paserPage(self, html):
        parsehtml = etree.HTML(html)
        r_list = parsehtml.xpath('//div/a[@class="mnav c-font-normal c-color-t"]/text()')
        r_list1 = parsehtml.xpath('//div[@id="s-top-left"]/a/@href')
        list=[]
        for i in range(len(r_list1)):
            new_list=[r_list[i],r_list1[i]]
            list.append(new_list)
        self.weit(list)

    def weit(self, r_list):

        with open("ass.csv", 'a', newline="", encoding="gb18030") as f:
            writer = csv.writer(f)
            writer.writerow(["标题", "链接"])
        for r_tup in r_list:
            with open("ass.csv", 'a', newline="", encoding="gb18030") as f:
                writer = csv.writer(f)
                writer.writerow(r_tup)

    def workOn(self):
        url = self.baseurl
        self.readPage(url)


if __name__ == "__main__":
    baidu = baiduSpider()
    baidu.workOn()