
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid, Page
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector
from pyecharts.globals import SymbolType
from link_mysql import  selectdata
# sql = "SELECT qy.`公司名称`,qy.`省份`,qy.`城市`, qy.`上市日期`,COUNT(qy.`城市`) AS 'shulian' FROM qy where 城市<>'--' GROUP BY  qy.`城市` ORDER BY shulian DESC LIMIT 10"
def liquid_data_precision(a,b) -> Liquid:
    c = (
        Liquid()
        .add(
            "上海",
            [a],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=b))
    )
    return c
sql = "SELECT`城市`,COUNT(`城市`) AS 数量 FROM qy where 城市<>'--' GROUP BY `城市` ORDER BY 数量 DESC LIMIT 10"

x = selectdata(sql)
wmin= []
shuju= []

for i in x:
    wmin.append(i[0])
    shuju.append(i[1])
print(wmin)
print(shuju)
l = shuju[0] + shuju[1] + shuju[2] + shuju[3] + shuju[4] + shuju[5] + shuju[6] + shuju[7] + shuju[8] + shuju[9]
print(l)
s = shuju[1] / l
print(s)
r = round(s, 4)# 保留4位小数
print(r)
biao =""
print(biao)

liquid_data_precision(s,biao).render('Liquid3.html')




