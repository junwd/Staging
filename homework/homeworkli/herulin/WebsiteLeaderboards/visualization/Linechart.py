from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
from MySQL import  selectdata
def pie_radius(xdata,ydata):
    c = (
        EffectScatter()
            .add_xaxis(xdata)
            .add_yaxis("网站推荐指数", ydata, symbol=SymbolType.ARROW)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return c
strsql="SELECT db.`name` AS `网站`, db.pai AS `推荐`FROM db ORDER BY 推荐 DESC LIMIT 10"
rows=selectdata(strsql)
rows=list(rows)
print(rows)
xdata=[]
ydata=[]
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata,ydata).render("Linechart.html")




