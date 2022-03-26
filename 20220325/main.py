import requests
from lxml import etree
import csv


class baiduSpider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.baseurl = "http://www.qnzy.net/public/consultletter/letterlist?searchType=4&consultId=7&page="
        self.baseurl2 = "http://www.qnzy.net/public/consultletter/letterinfo?id="

    def readPage(self, baseurl):
        res = requests.get(baseurl, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        dier = etree.HTML(html)
        t_list = dier.xpath('//ul/li[@class="code_ box_list_rightline"]/text()')
        for t_link in t_list:
            t_link = self.baseurl2 + t_link
            self.getinit(t_link)

    def getinit(self, t_link):
        res = requests.get(t_link, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        parseHtml = etree.HTML(html)
        list3 = parseHtml.xpath('//td[@class="lettertable_text"]/pre/text()')
        # for list4 in list3:
            # print(list4)
        self.baocheng(list3)

    def baocheng(self,list4):
        with open("ass.csv", 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(list4)


    def workOn(self):

        begin = int(input("请输入开始页："))
        end = int(input("请输入结束页："))
        for i in range(begin, end + 1):
            self.page = i
            url = self.baseurl + str(self.page)
            self.readPage(url)


if __name__ == "__main__":
    baidu = baiduSpider()
    baidu.workOn()
