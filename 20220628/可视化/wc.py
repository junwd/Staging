from MySQL import selectdata
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Line
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


def pie_radius(xdata, ydata):
    bar = (Bar()
           .add_xaxis(xdata)
           .add_yaxis('', ydata)
           )
    bar.set_global_opts(title_opts=opts.TitleOpts(title="每个地方有多少套房"), legend_opts=opts.LegendOpts(is_show=False))
    return bar


strsql = "SELECT `地点`,COUNT(*) AS COUNT FROM db GROUP BY `地点` HAVING COUNT>1"
rows = selectdata(strsql)
rows = list(rows)
print(rows)
xdata = []
ydata = []
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata, ydata).render("wc.html")
