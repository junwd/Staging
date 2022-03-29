import requests
from lxml import etree
import csv
class fzlSpider:
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.baseurl='http://www.qnzy.net/public/consultletter/letterlist?searchType=4&consultId=8'
        self.pageurl="http://www.qnzy.net/public/consultletter/letterinfo?id="
        self.page=1

    def readPage(self, url):
        response=requests.get(url, headers=self.headers)
        response.encoding="utf-8"
        html=response.text
        # print(html)
        self.paserPage(html)

    def paserPage(self, html):
        parsehtml=etree.HTML(html)
        r_list=parsehtml.xpath('//ul/li[@class="code_ box_list_rightline"]/text()')  #'220311-0000001'
        # print(r_list)
        for t_link in r_list:
            #http://www.qnzy.net/public/consultletter/letterinfo?id=220311-0000001
            t_link=self.pageurl+t_link
            # print(t_link)
            self.getwriter(t_link)

    def getwriter(self, t_link):
        res=requests.get(t_link, headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        parsehtml=etree.HTML(html)
        t_link1=parsehtml.xpath('//tr/td[@class="lettertable_text"]/pre/text()')
        # print(t_link1)
        for i in t_link1[0:1]:
            print(i)
            list=i.split()
            print(list)
            self.writerPage(list)

    def writerPage(self,list):

        with open("信箱内容.csv", "a", newline="", encoding="gb18030") as f:
            writer=csv.writer(f)
            writer.writerow(["来信内容"])

        with open("信箱内容.csv", "a", newline="", encoding="gb18030") as f:
            writer=csv.writer(f)
            writer.writerow(list)

    def workOn(self):
        begin=int(input("请输入开始页:"))
        end=int(input("请输入结束页:"))
        i=begin
        while i <= end:
            self.page=i
            url=self.baseurl+'&page='+str(self.page)
            self.readPage(url)
            i+=1

if __name__=="__main__":
    qnzy=fzlSpider()
    qnzy.workOn()

