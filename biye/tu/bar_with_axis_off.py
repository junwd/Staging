import logging
import pymysql
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType


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


strsql = "SELECT bk.`房名`,bk.`价格` FROM bk ORDER BY bk.`房名` DESC LIMIT 5,5"
rows = data(strsql)
rows = list(rows)


def bar_with_axis_off(xdata1, ydata1):
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='800px',
                                      height='600px'))
    bar.add_xaxis(xdata1)
    bar.add_yaxis('价格', ydata1)
    # 碰上类目标签过长的时候，可以选择关闭坐标轴，直接显示在图形中
    bar.set_series_opts(label_opts=opts.LabelOpts(position='insideLeft', formatter='{b}:{c}'))
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(is_show=False),
                        yaxis_opts=opts.AxisOpts(is_show=False))
    bar.reversal_axis()
    return bar


xdata1 = []
ydata1 = []
for i in rows:
    xdata1.append(i[0])
    ydata1.append(i[1])

bar_with_axis_off(xdata1, ydata1).render("bar_with_axis_off.html")
