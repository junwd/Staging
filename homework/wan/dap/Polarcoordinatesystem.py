import sqlite3

from pyecharts.charts import Polar
from pyecharts import options as opts
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT category,COUNT(*) AS COUNT FROM movie250 GROUP BY category HAVING COUNT>1'
# sql = 'select introduction from movie250'
data = cur.execute(sql)


def Polarcoordinatesystem(m, v):
    polar = (
        Polar()
            .add_schema(
            radiusaxis_opts=opts.RadiusAxisOpts(data=m, type_="category"),
        )
            .add("", v, type_='bar')
    )
    return polar


xdata = []
ydata = []
for i in data:
    xdata.append(i[0])
    ydata.append(i[1])
    m=xdata
    v=ydata
Polarcoordinatesystem(m,v).render("Polarcoordinatesystem.html")
cur.close()
con.close()
