import sqlite3

from pyecharts.charts import Funnel
from pyecharts.faker import Faker
from pyecharts import options as opts

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT country,COUNT(*) AS COUNT FROM movie250 GROUP BY country HAVING COUNT>1'
# sql = 'select introduction from movie250'
data = cur.execute(sql)


def Funnelchart(a, d):
    c = (
        Funnel()
            .add("商品", [list(z) for z in zip(a, d)])
            # .set_global_opts(title_opts=opts.TitleOpts(title="Funnel"))
            .set_global_opts(title_opts=opts.TitleOpts(title="装修情况"))
    )
    return c


xdata = []
ydata = []
for i in data:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
    a = xdata
    d = ydata
Funnelchart(a, d).render("Funnelchart.html")

cur.close()
con.close()
