class liaoxuede:
    def __init__(self):
        # 内容存储器
        self.baseurl = "https://gy.ke.com/ershoufang/pg"
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def loadPage(self, url):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePpage(html)
        self.Bs(html)

    def parsePage(self, html):
        pl=re.compile
        # p1 = re.compile( '<div\sclass="address">\s*.*\s*.*\s*.*\s*<a\s.*?>(.*?)<\/a>\s*<\/div>\s*<\/div>\s*<div\sclass="houseinfo">\s*.*\s*(.*)\s*(.*)\s*.\s(.*)\s*.*\s*.*\s*.*\s*\s*.*\s*.\s.*\s*.*\s*.*\s*<\/div>')
        r_list = pl.findall(html)
        self.writePage(r_list)

    def writePage(self, r_list):
        if self.page == 1:
            with open("File.txt", "a", encoding='gbk', newline='')as f:
                writer = csv.writer(f)
                writer.writerow(["社区", "楼高", "层数", "多少年建成", "房间规格", "占地面积"])
        for r_tuple in r_list:
            with open("File.txt", "a", encoding='gbk', newline="")as f:
                w = csv.writer(f)
                w.writerow(r_tuple)

    def worKOn(self):
        begin = int(input("请输入爬取的起始页："))
        end = int(input("请输入爬取的终止页"))
        i = begin
        while i <= end:
            self.page = i
            url = self.baseurl + str(self.page) + "/"
            self.loadPage(url)
            print("爬取成功")
            i += 1


if __name__ == "__main__":
    spider = liaoxuede()
    spider.worKOn()
