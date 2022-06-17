from link_mysql import  selectdata
import pyecharts.options as opts
from pyecharts.charts import Gauge
sql = "SELECT`省份`,COUNT(`省份`) AS 数量 FROM qy where 省份<>'--' GROUP BY `省份` ORDER BY 数量 DESC LIMIT 10"
x = selectdata(sql)
wmin = []
shuju = []

for i in x:
    wmin.append(i[0])
    shuju.append(i[1])
print(wmin)
print(shuju)
l = shuju[0] + shuju[1] + shuju[2] + shuju[3] + shuju[4] + shuju[5] + shuju[6] + shuju[7] + shuju[8] + shuju[9]
print(l)
s = shuju[0] / l
print(s)
r = round(s, 4)# 保留4位小数
print(r)
biao = wmin[0]+"\n在前十公司中所占的比例"
print(biao)
def qiu(xdata,ydata):
    c =(
    Gauge(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(series_name="业务指标", data_pair=[["完成率",xdata]])
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )
    # .render("gauge.html")
)
    return c
qiu(s,biao).render('Liquid_tu.html')