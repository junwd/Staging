from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import random
import datetime

# Pyecharts图表生成需要一些静态资源文件，通过下面代码更改为kesci提供的资源，提高加载速度～
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

# 直方图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
       )

bar.render_notebook()

# 折线图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data)
        )

line.render_notebook()

# 箱形图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [[random.randint(100, 200) for i in range(10)] for item in x_data]

Box = Boxplot()
Box.add_xaxis(x_data)
Box.add_yaxis("", Box.prepare_data(y_data))
Box.render_notebook()

# 散点图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

scatter = (Scatter()
           .add_xaxis(x_data)
           .add_yaxis('', y_data)
           )

scatter.render_notebook()

# 带涟漪效果散点图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

effectScatter = (EffectScatter()
                 .add_xaxis(x_data)
                 .add_yaxis('', y_data)
                 )

effectScatter.render_notebook()

# k线图
date_list = ["2020/4/{}".format(i + 1) for i in range(30)]
y_data = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    [2295.35, 2346.5, 2295.35, 2345.92],
    [2347.22, 2358.98, 2337.35, 2363.8],
    [2360.75, 2382.48, 2347.89, 2383.76],
    [2383.43, 2385.42, 2371.23, 2391.82],
    [2377.41, 2419.02, 2369.57, 2421.15],
    [2425.92, 2428.15, 2417.58, 2440.38],
    [2411, 2433.13, 2403.3, 2437.42],
    [2432.68, 2334.48, 2427.7, 2441.73],
    [2430.69, 2418.53, 2394.22, 2433.89],
    [2416.62, 2432.4, 2414.4, 2443.03],
    [2441.91, 2421.56, 2418.43, 2444.8],
    [2420.26, 2382.91, 2373.53, 2427.07],
    [2383.49, 2397.18, 2370.61, 2397.94],
    [2378.82, 2325.95, 2309.17, 2378.82],
    [2322.94, 2314.16, 2308.76, 2330.88],
    [2320.62, 2325.82, 2315.01, 2338.78],
    [2313.74, 2293.34, 2289.89, 2340.71],
    [2297.77, 2313.22, 2292.03, 2324.63],
    [2322.32, 2365.59, 2308.92, 2366.16],
    [2364.54, 2359.51, 2330.86, 2369.65],
    [2332.08, 2273.4, 2259.25, 2333.54],
    [2274.81, 2326.31, 2270.1, 2328.14],
    [2333.61, 2347.18, 2321.6, 2351.44],
    [2340.44, 2324.29, 2304.27, 2352.02],
    [2326.42, 2318.61, 2314.59, 2333.67],
    [2314.68, 2310.59, 2296.58, 2320.96],
    [2309.16, 2286.6, 2264.83, 2333.29],
    [2282.17, 2263.97, 2253.25, 2286.33],
]

kline = (Kline()
         .add_xaxis(date_list)
         .add_yaxis('', y_data)
         )

kline.render_notebook()

# 热力图
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

heat = (HeatMap()
        .add_xaxis(hour_list)
        .add_yaxis("", week_list, data)
        )

heat.render_notebook()

# 象形图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

pictorialBar = (PictorialBar()
                .add_xaxis(x_data)
                .add_yaxis('', y_data)
                )

pictorialBar.render_notebook()

# 层叠图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data_bar = [123, 153, 89, 107, 98, 23]
y_data_line = [153, 107, 23, 89, 123, 107]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data_bar)
       )

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data_line)
        )

overlap = bar.overlap(line)
overlap.render_notebook()

# GEO-地理坐标系
# 虚假数据
province = [
    '广东',
    '湖北',
    '湖南',
    '四川',
    '重庆',
    '黑龙江',
    '浙江',
    '山西',
    '河北',
    '安徽',
    '河南',
    '山东',
    '西藏']
data = [(i, random.randint(50, 150)) for i in province]

geo = (
    Geo()
        .add_schema(maptype="china")
        .add("", data)
)
geo.render_notebook()

# MAP-地图
province = [
    '广东',
    '湖北',
    '湖南',
    '四川',
    '重庆',
    '黑龙江',
    '浙江',
    '山西',
    '河北',
    '安徽',
    '河南',
    '山东',
    '西藏']
data = [(i, random.randint(50, 150)) for i in province]

map_ = (
    Map()
        .add("", data, 'china')
)
map_.render_notebook()

# BMAP-百度地图

province = [
    '广东',
    '湖北',
    '湖南',
    '四川',
    '重庆',
    '黑龙江',
    '浙江',
    '山西',
    '河北',
    '安徽',
    '河南',
    '山东',
    '西藏']
data = [(i, random.randint(50, 150)) for i in province]

bmap = (
    BMap()
        .add_schema(baidu_ak="FAKE_AK", center=[120.13066322374, 30.240018034923])
        .add("", data)
)
bmap.render_notebook()

# 饼图
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data = [123, 153, 89, 107, 98, 23]

pie = (Pie()
       .add('', [list(z) for z in zip(cate, data)])
       )

pie.render_notebook()

# 漏斗图
cate = ['访问', '注册', '加入购物车', '提交订单', '付款成功']
data = [30398, 15230, 10045, 3109, 1698]

funnel = (Funnel()
          .add("", [list(z) for z in zip(cate, data)])
          )

funnel.render_notebook()

# 仪表盘
gauge = (Gauge()
         .add("", [('转化率', 34)])
         )

gauge.render_notebook()

# 日历图

import math

# 虚假数据
begin = datetime.date(2019, 1, 1)
end = datetime.date(2019, 12, 31)
data = [[str(begin + datetime.timedelta(days=i)), abs(math.cos(i / 100)) * random.randint(1000, 1200)]
        for i in range((end - begin).days + 1)]

calendar = (
    Calendar()
        .add("", data, calendar_opts=opts.CalendarOpts(range_="2019"))
)

calendar.render_notebook()

# 关系图
nodes = [
    {"name": "结点1", "symbolSize": 1},
    {"name": "结点2", "symbolSize": 2},
    {"name": "结点3", "symbolSize": 3},
    {"name": "结点4", "symbolSize": 4},
    {"name": "结点5", "symbolSize": 5},
    {"name": "结点6", "symbolSize": 6},
    {"name": "结点7", "symbolSize": 7},
    {"name": "结点8", "symbolSize": 8},
]
links = [{'source': '结点1', 'target': '结点2'},
         {'source': '结点1', 'target': '结点3'},
         {'source': '结点1', 'target': '结点4'},
         {'source': '结点2', 'target': '结点1'},
         {'source': '结点3', 'target': '结点4'},
         {'source': '结点3', 'target': '结点5'},
         {'source': '结点3', 'target': '结点6'},
         {'source': '结点4', 'target': '结点1'},
         {'source': '结点4', 'target': '结点2'},
         {'source': '结点4', 'target': '结点7'},
         {'source': '结点4', 'target': '结点8'},
         {'source': '结点5', 'target': '结点1'},
         {'source': '结点5', 'target': '结点4'},
         {'source': '结点5', 'target': '结点6'},
         {'source': '结点5', 'target': '结点7'},
         {'source': '结点5', 'target': '结点8'},
         {'source': '结点6', 'target': '结点1'},
         {'source': '结点6', 'target': '结点7'},
         {'source': '结点6', 'target': '结点8'},
         {'source': '结点7', 'target': '结点1'},
         {'source': '结点7', 'target': '结点2'},
         {'source': '结点7', 'target': '结点8'},
         {'source': '结点8', 'target': '结点1'},
         {'source': '结点8', 'target': '结点2'},
         {'source': '结点8', 'target': '结点3'},
         ]

graph = (
    Graph()
        .add("", nodes, links)
)

graph.render_notebook()

# 平行坐标系
data = [
    ['一班', 78, 91, 123, 78, 82, 67, "优秀"],
    ['二班', 89, 101, 127, 88, 86, 75, "良好"],
    ['三班', 86, 93, 101, 84, 90, 73, "合格"],
]

parallel = (
    Parallel()
        .add_schema(
        [
            opts.ParallelAxisOpts(
                dim=0,
                name="班级",
                type_="category",
                data=["一班", "二班", "三班"],
            ),
            opts.ParallelAxisOpts(dim=1, name="英语"),
            opts.ParallelAxisOpts(dim=2, name="数学"),
            opts.ParallelAxisOpts(dim=3, name="语文"),
            opts.ParallelAxisOpts(dim=4, name="物理"),
            opts.ParallelAxisOpts(dim=5, name="生物"),
            opts.ParallelAxisOpts(dim=6, name="化学"),
            opts.ParallelAxisOpts(
                dim=7,
                name="评级",
                type_="category",
                data=["优秀", "良好", "合格"],
            ),
        ]
    )
        .add("", data)
)

parallel.render_notebook()

# 极坐标系
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
data = [123, 153, 89, 107, 98, 23]

polar = (
    Polar()
        .add_schema(
        radiusaxis_opts=opts.RadiusAxisOpts(data=cate, type_="category"),
    )
        .add("", data, type_='bar')
)

polar.render_notebook()

# 雷达图

data = [
    [78, 91, 123, 78, 82, 67],
    [89, 101, 127, 88, 86, 75],
    [86, 93, 101, 84, 90, 73],
]

radar = (Radar()
         .add_schema(schema=[
    opts.RadarIndicatorItem(name="语文", max_=150),
    opts.RadarIndicatorItem(name="数学", max_=150),
    opts.RadarIndicatorItem(name="英语", max_=150),
    opts.RadarIndicatorItem(name="物理", max_=100),
    opts.RadarIndicatorItem(name="生物", max_=100),
    opts.RadarIndicatorItem(name="化学", max_=100),
]
)
         .add('', data)
         )
radar.render_notebook()

# 旭日图
data = [
    {"name": "湖南",
     "children": [
         {"name": "长沙",
          "children": [
              {"name": "雨花区", "value": 55},
              {"name": "岳麓区", "value": 34},
              {"name": "天心区", "value": 144},
          ]},
         {"name": "常德",
          "children": [
              {"name": "武陵区", "value": 156},
              {"name": "鼎城区", "value": 134},
          ]},
         {"name": "湘潭", "value": 87},
         {"name": "株洲", "value": 23},
     ],
     },
    {"name": "湖北",
     "children": [
         {"name": "武汉",
          "children": [
              {"name": "洪山区", "value": 55},
              {"name": "东湖高新", "value": 78},
              {"name": "江夏区", "value": 34},
          ]},
         {"name": "鄂州", "value": 67},
         {"name": "襄阳", "value": 34},
     ],
     },
    {"name": "北京", "value": 235}
]

sunburst = (Sunburst()
            .add("", data_pair=data)
            )

sunburst.render_notebook()

# 桑基图
nodes = [
    {"name": "访问"},
    {"name": "注册"},
    {"name": "付费"},
]

links = [
    {"source": "访问", "target": "注册", "value": 50},
    {"source": "注册", "target": "付费", "value": 30},
]

sankey = (
    Sankey()
        .add("", nodes, links)
)

sankey.render_notebook()

# 河流图
cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
date_list = ["2020/4/{}".format(i + 1) for i in range(30)]

data = [[day, random.randint(10, 50), c] for day in date_list for c in cate]

river = (
    ThemeRiver()
        .add(
        series_name=cate,
        data=data,
        singleaxis_opts=opts.SingleAxisOpts(type_="time")
    )
)

river.render_notebook()

# 词云图
words = [
    ("hey", 230),
    ("jude", 124),
    ("dont", 436),
    ("make", 255),
    ("it", 247),
    ("bad", 244),
    ("Take", 138),
    ("a sad song", 184),
    ("and", 12),
    ("make", 165),
    ("it", 247),
    ("better", 182),
    ("remember", 255),
    ("to", 150),
    ("let", 162),
    ("her", 266),
    ("into", 60),
    ("your", 82),
    ("heart", 173),
    ("then", 365),
    ("you", 360),
    ("can", 282),
    ("start", 273),
    ("make", 265),
]

wc = (
    WordCloud()
        .add("", words)
)

wc.render_notebook()

# 表格
from pyecharts.components import Table

table = Table()

headers = ["City name", "Area", "Population", "Annual Rainfall"]
rows = [
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Adelaide", 1295, 1158259, 600.5],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
]
table.add(headers, rows)

table.render_notebook()

# 3D散点图
data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(100)]

scatter3D = (Scatter3D()
             .add("", data)
             )

scatter3D.render_notebook()

# 3D折线图
data = []
for t in range(0, 1000):
    x = math.cos(t / 10)
    y = math.sin(t / 10)
    z = t / 10
    data.append([x, y, z])

line3D = (Line3D()
          .add("", data,
               xaxis3d_opts=opts.Axis3DOpts(type_="value"),
               yaxis3d_opts=opts.Axis3DOpts(type_="value"))
          )

line3D.render_notebook()

# 3D直方图
data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
hour_list = [str(i) for i in range(24)]
week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

bar3D = (
    Bar3D()
        .add(
        "",
        data,
        xaxis3d_opts=opts.Axis3DOpts(hour_list, type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(week_list, type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
)

bar3D.render_notebook()

# 3D地图
province = [
    '广东',
    '湖北',
    '湖南',
    '四川',
    '重庆',
    '黑龙江',
    '浙江',
    '山西',
    '河北',
    '安徽',
    '河南',
    '山东',
    '西藏']
data = [(i, random.randint(50, 150)) for i in province]

map3d = (
    Map3D()
        .add("", data_pair=data, maptype='china')
)
map3d.render_notebook()

# 3D地球
from pyecharts.faker import POPULATION

mapglobe = (
    MapGlobe()
        .add_schema()
        .add(
        series_name="",
        maptype="world",
        data_pair=POPULATION[1:]
    )
)

mapglobe.render_notebook()

# 树图
data = [
    {"name": "湖南",
     "children": [
         {"name": "长沙",
          "children": [
              {"name": "雨花区", "value": 55},
              {"name": "岳麓区", "value": 34},
              {"name": "天心区", "value": 144},
          ]},
         {"name": "常德",
          "children": [
              {"name": "武陵区", "value": 156},
              {"name": "鼎城区", "value": 134},
          ]},
         {"name": "湘潭", "value": 87},
         {"name": "株洲", "value": 23},
     ],
     }
]

tree = (
    Tree()
        .add("", data)
)

tree.render_notebook()

# 矩形树图
data = [
    {"name": "湖南",
     "children": [
         {"name": "长沙",
          "children": [
              {"name": "雨花区", "value": 55},
              {"name": "岳麓区", "value": 34},
              {"name": "天心区", "value": 144},
          ]},
         {"name": "常德",
          "children": [
              {"name": "武陵区", "value": 156},
              {"name": "鼎城区", "value": 134},
          ]},
         {"name": "湘潭", "value": 87},
         {"name": "株洲", "value": 23},
     ],
     },
    {"name": "湖北",
     "children": [
         {"name": "武汉",
          "children": [
              {"name": "洪山区", "value": 55},
              {"name": "东湖高新", "value": 78},
              {"name": "江夏区", "value": 34},
          ]},
         {"name": "鄂州", "value": 67},
         {"name": "襄阳", "value": 34},
     ],
     },
    {"name": "北京", "value": 235}
]

treemap = (
    TreeMap()
        .add("", data)
)

treemap.render_notebook()

# 组合图表
begin = datetime.date(2020, 4, 1)
end = datetime.date(2020, 4, 20)

cate = ['Apple', 'Huawei', 'MI', 'Oppo', 'Vivo', 'Samsung']


# 随机生成数据的方法


def random_data(n): return [random.randint(100, 200) for i in range(n)]


# 新建一个timeline对象
tl = Timeline()
tl.add_schema()

for i in range((end - begin).days + 1):
    day = begin + datetime.timedelta(days=i)

    bar = (Bar()
           .add_xaxis(cate)
           .add_yaxis('电商渠道', random_data(len(cate)))
           )

    tl.add(bar, day)

tl.render_notebook()

# Tab-选项卡
cate = ['Apple', 'Huawei', 'MI', 'Oppo', 'Vivo', 'Samsung']

# 时间范围
begin = datetime.date(2020, 4, 1)
end = datetime.date(2020, 4, 20)
date_list = [str(begin + datetime.timedelta(days=i))
             for i in range((end - begin).days + 1)]


# 随机生成数据的方法


def random_data(n): return [random.randint(0, 100) for i in range(n)]


# 新建一个tab对象
tab = Tab()

for c in cate:
    day = begin + datetime.timedelta(days=i)

    line = (Line()
            .add_xaxis(date_list)
            .add_yaxis('', random_data(len(date_list)))
            )

    tab.add(line, c)

tab.render_notebook()

# Page-顺序多图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
       )

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data)
        )

page = Page()
page.add(bar, line)
page.render_notebook()

# Grid-并行多图
x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]

bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
       )

line = (Line()
        .add_xaxis(x_data)
        .add_yaxis('', y_data)
        )

grid = (Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_bottom="65%", pos_left="50%"))
        .add(line, grid_opts=opts.GridOpts(pos_left="15%"))
        )
grid.render_notebook()


