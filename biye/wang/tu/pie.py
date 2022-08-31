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


strsql = "SELECT `评分`,COUNT(*) AS COUNT FROM lo GROUP BY `评分` HAVING COUNT>1"
rows = data(strsql)
rows = list(rows)


def pie(x2data, y2data):
    pie = (Pie()
           .add('', [list(z) for z in zip(x2data, y2data)])
           )
    pie.set_global_opts(title_opts=(opts.TitleOpts(title="酒店评分统计")))
    return pie

x2data = []
y2data = []
for i in rows:
    x2data.append(i[0])
    y2data.append(i[1])
pie(x2data, y2data).render("pie.html")
