from pyecharts.charts import Page, Pie,Bar,Line
from pyecharts.faker import Collector, Faker
from pyecharts import options as opts
from link_mysql import  selectdata
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table  #表格
from pyecharts.options import ComponentTitleOpts,global_options
year=[]
data_2020=[]
data_2019=[]
data_2018=[]#全局变量
def year_line(x_data,y_data,y_data1,y_data2):
    line= (
        Line(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
        .add_xaxis(x_data)
        .add_yaxis("2020年",y_data,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            linestyle_opts=opts.LineStyleOpts( width=3.5))
        .add_yaxis("2019年", y_data1,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            linestyle_opts=opts.LineStyleOpts(width=3.5))
        .add_yaxis("2018年", y_data2,
            linestyle_opts=opts.LineStyleOpts(width=3.5))
    )
    return line
sqlstr2="select DATE_FORMAT(`上市日期`,'% %m') as 月份,COUNT(*)as 数量 FROM qy where DATE_FORMAT(上市日期,'% %Y')=2020 GROUP BY DATE_FORMAT(上市日期,'% %m') ORDER BY 月份"
sqlstr3="select DATE_FORMAT(`上市日期`,'% %m') as 月份,COUNT(*)as 数量 FROM qy where DATE_FORMAT(上市日期,'% %Y')=2019 GROUP BY DATE_FORMAT(上市日期,'% %m') ORDER BY 月份"
sqlstr4="select DATE_FORMAT(`上市日期`,'% %m') as 月份,COUNT(*)as 数量 FROM qy where DATE_FORMAT(上市日期,'% %Y')=2018 GROUP BY DATE_FORMAT(上市日期,'% %m') ORDER BY 月份"
# 获取2020数据
rows2 = selectdata(sqlstr2)

# 获取2019数据
rows3 = selectdata(sqlstr3)

# 获取2018数据
rows4 = selectdata(sqlstr4)


for j in rows2:
    data_2020.append(j[1])
print(data_2020)
for j in rows3:
    data_2019.append(j[1])
for j in rows4:
    data_2018.append(j[1])
month=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
year_line(month, data_2020, data_2019, data_2018).render('zx.html')