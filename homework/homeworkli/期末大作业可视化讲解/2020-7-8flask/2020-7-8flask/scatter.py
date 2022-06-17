from pyecharts.charts import Pie,Bar,Scatter
from pyecharts import options as opts
from linkdatabase import selectdata
from pyecharts.charts import Map
import numpy as np
import matplotlib.pyplot as plt

def scatter_tu(xdata,ydata):
    scratter=Scatter()
    scratter.add_xaxis(xdata)
    scratter.add_yaxis("信息分布与年份",ydata)
    scratter.render("scratter.htm")



strsql="SELECT DATE_FORMAT(time, '% %Y' )as years ,\
             COUNT( * ) as counts FROM qnzynews \
             GROUP BY DATE_FORMAT( time, '% %Y' ) \
             ORDER BY years DESC"
rows=selectdata(strsql)
rows=list(rows)
# print(rows)
xdata=[]
ydata=[]
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
scatter_tu(xdata,ydata)#扇形图