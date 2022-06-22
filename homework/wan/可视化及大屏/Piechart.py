import sqlite3

from pyecharts.charts import Pie
from pyecharts import options as opts

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT rated,COUNT(*) AS COUNT FROM movie250 GROUP BY rated HAVING COUNT>1'
# sql = 'select introduction from movie250'
data = cur.execute(sql)


def piechart(h, t):
    pie = Pie()
    pie.add("", list(zip(h, t)),
            center=["50%", "60%"])  # 圆心位置
    # pie.set_global_opts(title_opts=opts.TitleOpts(title="几室几厅"))
    return pie


xdata = []
ydata = []
for i in data:
    xdata.append(i[0])
    ydata.append(i[1])
    h = xdata
    t = ydata
piechart(h, t).render("Piechart.html")
cur.close()
con.close()
