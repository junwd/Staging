from pyecharts import options as opts
from pyecharts.charts import Bar, EffectScatter
import sqlite3  # 数据库
from pyecharts.charts import Bar
from pyecharts.globals import SymbolType

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'SELECT movie250.cname AS "名称",movie250.score AS "价钱" FROM movie250 ORDER BY 价钱 ASC LIMIT 10'
# sql = 'select introduction from movie250'
data = cur.execute(sql)


def pie_radius(w, r):
    c = (
        EffectScatter()
            .add_xaxis(w)
            .add_yaxis("价格", r, symbol=SymbolType.ARROW)
            .set_global_opts(title_opts=opts.TitleOpts(title="前十的价格"))
    )
    return c


# rows=list()
# print(rows)
xdata = []
ydata = []
for i in data:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
    w = xdata
    r = ydata
pie_radius(w, r).render("pie_radius.html")

cur.close()
con.close()
