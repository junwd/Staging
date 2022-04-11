import requests
import csv
import json

url = "https://movie.douban.com/j/chart/top_list?"
headers = {"User-Agent": "Mozilla/5.0"}
num = input("请输入要获取的电影数量：")
params = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": num
}
res = requests.get(url, params=params, headers=headers)
res.encoding = "utf-8"
html = res.text
html2 = json.loads(html)
with open("豆瓣电影.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["电影名称", "国家", "评分"])
for mimi in html2:
    name = mimi["title"]
    country = mimi["regions"]
    score = mimi["rating"][0]
    M = [name, country, score]
    with open("豆瓣电影.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(M)
