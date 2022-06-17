from pyecharts.charts import Pie,Bar
from pyecharts import options as opts
from linkdatabase import  selectdata
from pyecharts.charts import Map
import numpy as np
import matplotlib.pyplot as plt



def pie_radius(xdata,ydata):
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(xdata, ydata)],
            radius=["40%", "75%"],
        )
        .set_global_opts(
            # title_opts=opts.TitleOpts(title="Pie-数据扇形展示"),
            toolbox_opts=opts.ToolboxOpts(
                is_show=True,  # 是否显示组件
                orient='vertical',  # 布局朝向  vertical表示纵向  horizontal表示横向
                pos_left='90%',
            ),
            legend_opts=opts.LegendOpts(
                orient="vertical", pos_top="15%", pos_left="2%"
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

strsql="SELECT DATE_FORMAT(time, '% %Y' )as years ,\
             COUNT( * ) as counts FROM qnzynews \
             GROUP BY DATE_FORMAT( time, '% %Y' ) \
             ORDER BY years DESC"
rows=selectdata(strsql)
rows=list(rows)
print(rows)
xdata=[]
ydata=[]
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata,ydata).render("pie.html")  #扇形图