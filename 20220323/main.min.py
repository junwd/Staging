import requests
from lxml import etree
import csv


class baiduSpider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}
        self.baseurl = "http://www.qnzy.net/public/consultletter/letterlist?searchType=4&consultId=7&page="
        self.page = 1

    def readPage(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = "utf-8"
        html = response.text
        self.paserPage(html)

    def paserPage(self, html):
        parsehtml = etree.HTML(html)
        r_list = parsehtml.xpath('//ul/li[@class="code_ box_list_rightline"]/text()')
        r_list1 = parsehtml.xpath('//li[@class="title_ box_list_rightline"]/a/text()')
        r_list2 = parsehtml.xpath('//ul/li[@class="sort_ box_list_rightline"]/text()')
        r_list3 = parsehtml.xpath('//ul/li[@class="replyTime_ box_list_rightline"]/text()')
        r_list4 = parsehtml.xpath('//ul/li[@class="replyUnit_ box_list_rightline"]/text()')
        r_list5 = parsehtml.xpath('//ul/li[@class ="state_ fontblue"]/text()')
        list = []
        for i in range(len(r_list1)):
            new_list = [r_list[i], r_list1[i], r_list2[i], r_list3[i], r_list4[i], r_list5[i]]
            list.append(new_list)
        self.weit(list)

    def weit(self, r_list):

        with open("ass.csv", 'a', newline="", encoding="gb18030") as f:
            writer = csv.writer(f)
            writer.writerow(["编号", "标题", "类型", "回复时间", "回复单位", "回复状态"])
        for r_tup in r_list:
            with open("ass.csv", 'a', newline="", encoding="gb18030") as f:
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
    baidu = baiduSpider()
    baidu.workOn()
