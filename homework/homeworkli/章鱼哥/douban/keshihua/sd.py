from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
from link_mysql import selectdata


def pie_radius(xdata, ydata):
    c = (
        EffectScatter()
            .add_xaxis(xdata)
            .add_yaxis("评分统计", ydata, symbol=SymbolType.ARROW)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return c


strsql = "SELECT rate,COUNT(*) AS COUNT FROM db GROUP BY rate HAVING COUNT > 1"
rows = selectdata(strsql)
rows = list(rows)
print(rows)
xdata = []
ydata = []
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata, ydata).render("sd.html")
