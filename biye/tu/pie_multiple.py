import logging
import pymysql
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode


def data(sql):
    conn = pymysql.connect(host='localhost', port=3306, user='root',
                           password='root', db='beike',
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


strsql = "SELECT `用水`,COUNT(*) AS COUNT FROM bk GROUP BY `用水` HAVING COUNT>1 "
rows = data(strsql)
rows = list(rows)
strsql1 = "SELECT `用电`,COUNT(*) AS COUNT FROM bk GROUP BY `用电` HAVING COUNT>1 "
rows1 = data(strsql1)
rows1 = list(rows1)

def pie_multiple(xdata5, ydata5,xdata6, ydata6):
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='800px'))
    pie.add("",
            [list(z) for z in zip(xdata5, ydata5)],
            radius=["20%", "50%"],
            center=["25%", "50%"])
    # 添加多个饼图
    pie.add("",
            [list(z) for z in zip(xdata6, ydata6)],
            radius=["20%", "50%"],
            center=["75%", "50%"])

    return pie

xdata5 = []
ydata5 = []
for i in rows:
    xdata5.append(i[0])
    ydata5.append(i[1])
xdata6 = []
ydata6 = []
for i in rows1:
    xdata6.append(i[0])
    ydata6.append(i[1])
pie_multiple(xdata5, ydata5, xdata6, ydata6).render("pie_multiple.html")
