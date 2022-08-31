import logging
import pymysql
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType


def data(sql):
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           password='root', db='ylong',
                           charset="utf8")
    cursor = conn.cursor()  # 建立一个游标对象
    try:
        cursor.execute(sql)  # 使用游标执行SQL语句
        conn.commit()  # 提交数据
        #  print(cursor.rowcount) 输出查询记录数
        return cursor.fetchall()  # 获取全部记录
        #  return SqlDomainName
        cursor.close()  # 关闭游标对象
        conn.close()  # 关闭连接
    except Exception as e:
        # 有异常，回滚事务
        logging.exception(e)
        conn.rollback()  # 撤销数据


strsql = "SELECT lo.`酒店名`,lo.`评论` FROM lo LIMIT 15"
rows = data(strsql)
rows = list(rows)


def bar(x1data, y1data):
    bar = (Bar()
           .add_xaxis(x1data)
           .add_yaxis('', y1data)
           )
    bar.set_global_opts(title_opts=opts.TitleOpts(title="酒店名与评论"))
    # bar.render_notebook()
    return bar
x1data = []
y1data = []
for i in rows:
    x1data.append(i[0])
    y1data.append(i[1])
bar(x1data, y1data).render("bar.html")
