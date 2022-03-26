#示例2：爬取百度贴吧帖子里面所有的图片
#      1.目标：爬取指定贴吧所有的图片
#      2.思路：
#             1.获取贴吧主页URL,下一页，找URL规律
#             2.获取1页中每个帖子的URL
#             3.对每个帖子URL发请求，获取帖子图片里的URL
#             4.对图片的URL发请求，以web方式写入本地文件
#       3.步骤：
#             1.获取贴吧主页的URL
#                  http://tieba.baidu.com/f?+查询参数
#             2.找到页面中使用帖子的URL，
#                 src:完整链接
#                 href:和主URL进行拼接
#                 href="/p/6333559032"
#                 http://tieba.baidu.com/p/6333559032
#                 xpath匹配链接：
#                    方法1： //div[@class="col2_right j_threadlist_li_right"]
#                     /div/div/a@href

#                    方法2(推荐)：//div[@class="t_con cleafix"]/div/div/div
#                    /a@href
#             3.找每个帖子里面图片的链接
#               xpath匹配：
#               //img[@class="BDE_Image"]/@src
#            4.代码实现

#示例2：百度贴吧图片抓取案例
import requests
from lxml import etree
class baiduImagespider:
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.baseurl="http://tieba.baidu.com"
        self.pageurl="http://tieba.baidu.com/f?"

    #获取页面使用的帖子URL列表
    def getPageurl(self,params):
        res=requests.get(self.pageurl,headers=self.headers,params=params)
        res.encoding="utf-8"
        html=res.text
        #构建解析对象
        parseHtml=etree.HTML(html)
        #帖子链接列表
        # t_list=parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a@href')
        t_list=parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        #t_list:['/p/123234234','/p/214325346',...]
        for t_link in t_list:
            t_link=self.baseurl+t_link  #拼接帖子完整url
            self.getImageurl(t_link)


        # 获取帖子中图片URL列表
    def getImageurl(self,t_link):
        res=requests.get(t_link,headers=self.headers)
        res.encoding="utf-8"
        html=res.text
        #构建解析对象
        parseHtml=etree.HTML(html)
        # Img_list=parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        Img_list = parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        # print(Img_list)
        for img_link in  Img_list:
            self.writeImage(img_link)

    #保存到本地
    def writeImage(self,img_link):
        res=requests.get(img_link,headers=self.headers)#获取图片的bytes
        res.encoding="utf-8"
        html=res.content

        filename=img_link[-12:]
        with open(filename+".jpg","wb") as f:
            f.write(html)
            print("%s下载成功"%filename)

    #主函数
    def workOn(self):
        name=input("请你输入贴吧名：")
        begin=int(input("请输入起始页："))
        end=int(input("请输入终止页："))

        for n in range(begin,end+1):
            pn=(n-1)*50
            params={"kw":name,
                    "pn":str(pn)
                    }
            self.getPageurl(params)


if __name__=="__main__":
    spider=baiduImagespider()
    spider.workOn()

