import pyecharts.options as opts
from pyecharts.charts import Funnel

from MySQL import selectdata


def pie_radius(xdata, ydata):
    c = (
        Funnel()
            .add("商品", [list(z) for z in zip(xdata, ydata)])
            # .set_global_opts(title_opts=opts.TitleOpts(title="Funnel"))
            .set_global_opts(title_opts=opts.TitleOpts(title="装修情况"))
    )
    return c


strsql = "SELECT db.`name`,db.tui FROM db ORDER BY db.tui DESC LIMIT 10"
rows = selectdata(strsql)
rows = list(rows)
print(rows)
xdata = []
ydata = []
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata, ydata).render("svs.html")
