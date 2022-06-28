from MySQL import selectdata
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


def pie_radius(xdata, ydata):
    pie = (Pie()
           .add('', [list(z) for z in zip(xdata, ydata)])
           )
    pie.set_global_opts(title_opts=opts.TitleOpts(title="单位百万元"), legend_opts=opts.LegendOpts(is_show=False))
    return pie


strsql = "SELECT db.`名称`,db.`价格` FROM db LIMIT 10"
rows = selectdata(strsql)
rows = list(rows)
print(rows)
xdata = []
ydata = []
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1][:-8])
pie_radius(xdata, ydata).render("Pie.html")
