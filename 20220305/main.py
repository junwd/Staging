import urllib.request
import urllib.parse
import random
headers_list=[{"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"},
              {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"},
              {"User-Agent":"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0"}]
headers=random.choice(headers_list)
name=input("请输入要搜索的贴吧名：")
begin=int(input("请输入要获取的开始页面："))
end=int(input("请输入要获取的结束页面："))
p={"kw":name}
key=urllib.parse.urlencode(p)
for i in range(begin,end+1):
    pn=(i-1)*50
    baseurl="https://tieba.baidu.com/f?"
    url=baseurl+key+"&pn="+str(pn)
    # print(url)
    req=urllib.request.Request(url,headers=headers)
    res=urllib.request.urlopen(req)
    html=res.read().decode("UTF-8")
    # print(html)
    filename="第"+str(i)+"页.html"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)
        print("第%d页数据获取成功"%i)
        print("*"*30)