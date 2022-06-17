from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from link_mysql import  selectdata
def map(xdata,ydata):
    c = (
        Map()
            .add("省份", [list(z) for z in zip(xdata,ydata)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="上市公司地域分布"),
            visualmap_opts=opts.VisualMapOpts(max_=600, is_piecewise=True),
        )
            # .render("map_visualmap_piecewise.html")
    )
    return c
strsql="select `省份`,count(*)as 数量 from qy where 省份<>'--' GROUP BY 省份 ORDER BY 数量 desc "
rows=selectdata(strsql)
rows=list(rows)
print(rows)
xdata=[]
ydata=[]
for i in rows:
    xdata.append(i[0])
    ydata.append(i[1])
map(xdata,ydata).render("map.html")




