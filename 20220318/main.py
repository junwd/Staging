import requests
url="http://www.baidu.com"
headers={"User-Agent":"Mozilla/5.0 "}
requests=requests.get(url,headers=headers)
requests.encoding="utf-8"
html=requests.text
print(html)