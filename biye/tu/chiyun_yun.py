import logging
import pymysql
import pyecharts.options as opts
from pyecharts.charts import WordCloud


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


strsql = "SELECT `房名`,COUNT(*) AS COUNT FROM bk GROUP BY `房名` HAVING COUNT>1 "
rows = data(strsql)
rows = list(rows)


def yun(xdata11):
    c = (
        WordCloud()
            .add(
            "",
            xdata11,
            word_size_range=[20, 100],
            textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud词云"))
        # .render("ciyun.html")
    )
    return c


xdata11 = []
for i in rows:
    xdata11.append(i)
yun(xdata11).render("ciyun.html")
