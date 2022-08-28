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


strsql = "SELECT `租期`,COUNT(*) AS COUNT FROM bk GROUP BY `租期` HAVING COUNT>1 "
rows = data(strsql)
rows = list(rows)
color_js = """
            new echarts.graphic.LinearGradient(
                                0, 
                                1, 
                                0, 
                                0,
                                [{offset: 0, color: '#008B8B'}, 
                                 {offset: 1, color: '#FF6347'}], 
                                false)
           """
def bar_with_linear_gradient_color(xdata3, ydata3):
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(xdata3)
    bar.add_yaxis('租赁期限', ydata3,
                  # 使用JsCode执行渐变色代码
                  itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_js)))

    return bar

xdata3 = []
ydata3 = []
for i in rows:
    xdata3.append(i[0])
    ydata3.append(i[1])

bar_with_linear_gradient_color(xdata3, ydata3).render("bar_with_linear_gradient_color.html")
