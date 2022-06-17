from link_mysql import  selectdata
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
def pie_radius(xdata,ydata):
    c = (
        Bar()
            .add_xaxis(xdata)
            .add_yaxis("城市",ydata, category_gap="60%")
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode(
                        """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: 'rgba(0, 244, 255, 1)'
                }, {
                    offset: 1,
                    color: 'rgba(0, 77, 167, 1)'
                }], false)"""
                    ),
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "rgb(0, 160, 221)",
                }
            }
        )
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    return c
strsql="select 城市,count(*)as 数量 from qy where 城市<>'--' GROUP BY 城市 ORDER BY 数量 DESC limit 10"
rows=selectdata(strsql)
rows=list(rows)
print(rows)
xdata=[]
ydata=[]
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata,ydata).render("bar_tu.html")