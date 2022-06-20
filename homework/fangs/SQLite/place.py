import sqlite3

from pyecharts import options as opts
from pyecharts.charts import Pie, Funnel

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT cname,COUNT(*) AS COUNT FROM movie250 GROUP BY cname HAVING COUNT>1'
# sql = 'select introduction from movie250'
data = cur.execute(sql)
def place(xdata, ydata):
    pie = Pie()
    pie.add('', [list(z) for z in zip(xdata, ydata)], rosetype='radius')
    pie.set_global_opts(title_opts=opts.TitleOpts(title="Pie的基本图表"))
    pie.render_notebook()
    return pie

    # c = (
    #     Funnel()
    #         .add(
    #         "类别",
    #         [list(z) for z in zip(xdata, ydata)],
    #         sort_="ascending",
    #         label_opts=opts.LabelOpts(position="inside"),
    #     )
    #         .set_global_opts(title_opts=opts.TitleOpts(title="标题"))
    # )
    # return c
xdata = []
ydata = []
for i in data:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
place(xdata, ydata).render("place.html")

cur.close()
con.close()
