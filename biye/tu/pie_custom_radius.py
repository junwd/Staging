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

def pie_custom_radius(xdata4, ydata4):
    pie = Pie(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    pie.add("",
            [list(z) for z in zip(xdata4, ydata4)],
            # 设置半径范围，0%-100%
            radius=["40%", "75%"])

    return pie

xdata4 = []
ydata4 = []
for i in rows:
    xdata4.append(i[0])
    ydata4.append(i[1])

pie_custom_radius(xdata4, ydata4).render("pie_custom_radius.html")
