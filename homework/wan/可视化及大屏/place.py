import sqlite3

from pyecharts import options as opts
from pyecharts.charts import Pie, Funnel

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT cname,COUNT(*) AS COUNT FROM movie250 GROUP BY cname HAVING COUNT>1'
# sql = 'select introduction from movie250'
data = cur.execute(sql)

def place(k, p):
    pie = Pie()
    pie.add('', [list(z) for z in zip(k, p)], rosetype='radius',center = ["50%", "50%"])
    center = ["0%", "100%"]

    pie.set_global_opts(title_opts=opts.TitleOpts(title="各地"),legend_opts = opts.LegendOpts(is_show=False))

    pie.render_notebook()
    return pie
xdata = []
ydata = []
for i in data:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
    k = xdata
    p = ydata
place(k,p).render("place.html")

cur.close()
con.close()
