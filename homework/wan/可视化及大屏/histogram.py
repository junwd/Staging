import sqlite3

from pyecharts.charts import Bar
from pyecharts import options as opts

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT movie250.cname,movie250.id FROM movie250 ORDER BY movie250.id ASC LIMIT 10'
# sql = 'select introduction from movie250'
data = cur.execute(sql)


def histogram(f, s):
    c = (Bar().add_xaxis(xdata).add_yaxis('面积', ydata))

    return c


xdata = []
ydata = []
for i in data:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1][:3])
    f = xdata
    s = ydata
histogram(f, s).render("histogram.html")

cur.close()
con.close()
