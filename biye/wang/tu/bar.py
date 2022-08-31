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


strsql = "SELECT `类型`,COUNT(*) AS COUNT FROM lo GROUP BY `类型` HAVING COUNT>1"
rows = data(strsql)
rows = list(rows)


def bars(x3data, y3data):
    bar = (Bar()
           .add_xaxis(x3data)
           .add_yaxis('', y3data)
           )

    line = (Line()
            .add_xaxis(x3data)
            .add_yaxis('', y3data)
            )

    grid = (Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="65%", pos_left="50%"))
            .add(line, grid_opts=opts.GridOpts(pos_left="15%"))
            )

    return grid
x3data = []
y3data = []
for i in rows:
    x3data.append(i[0])
    y3data.append(i[1])
bars(x3data, y3data).render("bars.html")
