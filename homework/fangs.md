

本程序使用scrapy爬取链家数据存储到 _SQLite_，使用 *flask* 框架可视化数据

## 目录结构说明

│  app.py                ----- flask框架 文件
│  movie.db                ----- 数据库
│  README.md
│  requirements.txt        ----- 依赖包环境版本
│  spider.py            ----- 爬取数据 文件
│  testCloud.py            ----- 词云生成 文件
├─static                ----- 静态页面
├─templates                ----- HTML页面
└─venv                    ----- 虚拟环境



项目改自[GitHub](https://github.com/lzz110/douban_movies_top250)    点击查看



基本沿用之前的思路，只是更改了数据库及前端页面的内容，重构了数据库及显示的内容，




