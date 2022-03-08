import json
import urllib.parse
import urllib.request

key = input("请你输入要翻译的内容：")
deta = {
    "i": key, "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16467214882038",
    "sign": "b42ab6e98b8b15863e1668ef0ddabfa8",
    "lts": "1646721488203",
    "bv": "c2777327e4e29b7c4728f13e47bde9a5",
    "doctype": "json",
    "version": "2.1",
    "keyfrom:": "fanyi.web",
    "action": "FY_BY_REALTlME"
}

data1 = urllib.parse.urlencode(deta)
deta2 = bytes(data1, "utf-8")

# 发请求，获取响应
url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
req = urllib.request.Request(url, data=deta2, headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

r_dict = json.loads(html)
print(r_dict["translateResult"][0][0]["tgt"])
