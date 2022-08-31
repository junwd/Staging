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


strsql = "SELECT `装修风格`,COUNT(*) AS COUNT FROM lo GROUP BY `装修风格` HAVING COUNT>1"
rows = data(strsql)
rows = list(rows)


def bar_rev(x6data, y6data):
    c = (
        Bar()
            .add_xaxis(x6data)
            .add_yaxis("装修风格", y6data)
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="大多数装修风格"))
            # .render("bar_reversal_axis.html")
    )
    return c


x6data = []
y6data = []
for i in rows:
    x6data.append(i[0])
    y6data.append(i[1])
bar_rev(x6data, y6data).render("bar_rev.html")
