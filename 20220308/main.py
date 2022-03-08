# 1,class 方法
import urllib.request
import urllib.parse
import random
class Tiebasp:
 # 初始化函数
    def __init__(self):
        self.baseurl="https://tieba.baidu.com/f?"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

 # 读取函数
    def readPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

# 写入函数
    def writePage(self,filename,html):
        with open(filename,"w",encoding="utf-8") as f:
            f.write(html)
            print("写入成功")

# 主函数
    def workOn(self):
        name=input("请输入要搜索的贴吧名：")
        begin=int(input("请输入要获取的开始页面："))
        end=int(input("请输入要获取的结束页面："))
        p={"kw":name}
        key=urllib.parse.urlencode(p)
        for i in range(begin,end+1):
            pn=(i-1)*50
            baseurl="https://tieba.baidu.com/f?"
            url=baseurl+key+"&pn="+str(pn)
            html=self.readPage(url)
            filename = "第" + str(i) + "页数.html"
            self.writePage(filename,html)

if __name__=="__main__":
    spider=Tiebasp()
    spider.workOn()