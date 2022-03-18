import requests
url = "https://t7.baidu.com/it/u=1092574912,855301095&fm=193&f=GIF"
headers = {"User-Agent":"Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.encoding = "utf-8"
html = res.content
with open("1.jpg", "wb") as f:
    f.write(html)
print ("成功")
