import pyecharts.options as opts
from pyecharts.charts import Radar
from link_mysql import  selectdata
def pie_radius(xdata,ydata):
    v1 = [ydata]
    c = (
        Radar()
            .add_schema(
            schema=[
                opts.RadarIndicatorItem(name=xdata[0], max_=130),
                opts.RadarIndicatorItem(name=xdata[1], max_=130),
                opts.RadarIndicatorItem(name=xdata[2], max_=130),
                opts.RadarIndicatorItem(name=xdata[3], max_=130),
                opts.RadarIndicatorItem(name=xdata[4], max_=130),
                opts.RadarIndicatorItem(name=xdata[5], max_=130),
                opts.RadarIndicatorItem(name=xdata[6], max_=130),
                opts.RadarIndicatorItem(name=xdata[7], max_=130),
                opts.RadarIndicatorItem(name=xdata[8], max_=130),
                opts.RadarIndicatorItem(name=xdata[9], max_=130),
            ]
        )
            .add("行业分类", v1)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title=""),
        )
    )
    return c
strsql="SELECT `行业分类`,count(`行业分类`) as 数量 from qy where 行业分类<>'--' GROUP BY `行业分类` ORDER BY 数量 DESC"
rows=selectdata(strsql)
rows=list(rows)
print(rows)
xdata=[]
ydata=[]
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata,ydata).render("radar.html")




