## scrapy 框架基本命令行
---

创建项目
```
 scrapy startproject deins
```
```
 cd deins
```
创建爬虫对象
```
scrapy genspider junwd junwd.xyz
```
运行爬虫
```
scrapy crawl junwd
```
---
### 配置爬虫请求头
```
User-Agent: Mozilla/5.0
```
其它实例看[github](https://github.com/junwd/Staging)项目，