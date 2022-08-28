import logging
import pymysql
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker


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


strsql = "SELECT `房屋类型`,COUNT(*) AS COUNT FROM bk GROUP BY `房屋类型` HAVING COUNT>1"
rows = data(strsql)
rows = list(rows)
def bar_with_default_selected_series(xdata2, ydata2):
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(xdata2)
    # 默认选中A C
    bar.add_yaxis('A', ydata2, is_selected=True)
    # bar.add_yaxis('B', ydata2, is_selected=False)
    # bar.add_yaxis('C', ydata2, is_selected=True)
    return bar

xdata2 = []
ydata2 = []
for i in rows:
    xdata2.append(i[0])
    ydata2.append(i[1])

bar_with_default_selected_series(xdata2, ydata2).render("bar_with_default_selected_series.html")
