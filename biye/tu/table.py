import logging
import pymysql
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


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


strsql = "SELECT bk.`房名`,bk.`价格`,bk.`面积`,bk.`楼层`,bk.`房屋类型`,bk.`租期` FROM bk LIMIT 3"
rows = data(strsql)
rows = list(rows)


def table(xdata9):
    table = Table()
    headers = ["房名", "价钱", "平方", "楼层", "房屋类型", "租期"]
    # qw = [
    #     ["Brisbane", 5905, 1857594, 1146.4, "df", "as"]
    # ]

    table.add(headers, xdata9)
    table.set_global_opts(
        title_opts=ComponentTitleOpts(title="房情况", subtitle="看看就好")
    )
    return table

xdata9 = []
for i in rows:
    xdata9.append(i)
table(xdata9).render("table_base.html")
