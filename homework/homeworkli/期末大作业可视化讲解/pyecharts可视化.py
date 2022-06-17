# pyecharts官网：http://pyecharts.org/#/zh-cn/intro
#echarts官网：https://echarts.apache.org/zh/index.html

#帖子：https://www.kesci.com/home/project/5e50e7f50e2b66002c2057b3

# ***示例------------pyecharts-gallery官网网址:https://github.com/pyecharts/pyecharts-gallery

#截图工具：https://getsharex.com/





#----------------------------柱状图---------------------------------------
#示例1：
# from pyecharts.charts import Bar
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.render("bar.html")

#示例
# import pyecharts.options as opts
# from pyecharts.charts import Bar
#
# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [5, 20, 36, 10, 75, 90]
# v2 = [10, 25, 8, 60, 20, 80]
#
# (
#     Bar()
#     .add_xaxis(attr)
#     .add_yaxis("商家A", v1, stack="stack1")
#     .add_yaxis("商家B", v2, stack="stack1")
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(title_opts=opts.TitleOpts(title="柱状图数据堆叠示例"))
#     .render("bar_stack.html")
# )




#示例1---继续
# from pyecharts.charts import Bar
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render("bar1.html")


#示例1---继续
# from pyecharts.charts import Bar
# from pyecharts import options as opts
#
# # V1 版本开始支持链式调用
# # 你所看到的格式其实是 `black` 格式化以后的效果
# # 可以执行 `pip install black` 下载使用
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )
# bar.render("bar1.html")

#示例1---继续
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # 内置主题类型可查看 pyecharts.globals.ThemeType
# from pyecharts.globals import ThemeType
#
# bar = (
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
# ).render("bar3.html")


#示例2：
# import pandas as pd
# from pivottablejs import pivot_ui
# from IPython.display import IFrame
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # orders=pd.read_excel('D:/testdata/course_orders.xlsx')
# course_orders=pd.read_excel('D:/testdata/course_orders.xlsx')
# # print(course_orders.head())
# # pivot_ui(course_orders)
#
# course_orders=course_orders.groupby("商品名称")["订单编号"].count().sort_values(ascending=False)
# # print(course_orders)
# x=course_orders.index.tolist()  #转换为list类型
# y=course_orders.values.tolist()  #转换为list类型
# bar=Bar()
# bar.add_xaxis(x)
# bar.add_yaxis("学员人数",y)
# bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题",subtitle="副标题"))
# bar.render("./html/bar2.html")


#示例3：3D柱状图

# import pandas as pd
# from pivottablejs import pivot_ui
# from IPython.display import IFrame
# from pyecharts.charts import Bar3D
# from openpyxl.styles import fonts
# #
# #
# #
# from pyecharts import options as opts
# user_analysis=pd.read_excel('D:/testdata/user_analysis.xlsx') #此数据记录2015-2018年的某公众号的粉丝增长数据
# # print(user_analysis["时间"])
# # print(type(user_analysis))   #<class 'pandas.core.frame.DataFrame'>
# # print(user_analysis.head())
# # t=user_analysis["时间"][0]
# # print(t.year)
#
# user_analysis["年份"]=user_analysis["时间"].apply(lambda s:s.year)
# user_analysis["月份"]=user_analysis["时间"].apply(lambda s:s.month)
# # print(user_analysis.head(2))
#
# user_data=user_analysis.groupby(["月份","年份"],as_index=False)["净增关注人数"].sum()
# # print(user_data.head())
#
# user_data["年份"]=user_data["年份"]-2015
# user_data["月份"]=user_data["月份"]-1
# # print(user_data.values.tolist())
#
# x_axis=["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
# y_axis=["2015年","2016年","2017年","2018年"]
# bar3d=Bar3D()
# bar3d.add("每个月粉丝增长率",x_axis,y_axis,user_data.values.tolist())
# bar3d.render("./html/3dbar1.html")




#2---------------------箱线图----------------------------------------

# import pandas as pd
# from pivottablejs import pivot_ui
# from pyecharts.charts import Boxplot
# user_analysis=pd.read_excel('D:/testdata/user_analysis.xlsx') #此数据记录2015-2018年的某公众号的粉丝增长数据
# user_analysis["年份"]=user_analysis["时间"].apply(lambda s:s.year)
# user_analysis["天"]=user_analysis["时间"].apply(lambda s:s.dayofyear)
# # print(user_analysis.head(2))
# user_analysis=user_analysis[["年份","天","净增关注人数"]]
# print(user_analysis.head())

#透视分析
#
# user_data=user_analysis.pivot(index="天",columns="年份",values="净增关注人数")
# # print(user_data.head())
# # print(user_data[2015].dropna())    #dropna()去掉null值显示
#
# year=[2015,2016,2017,2018]
# user_nums=[user_data[2015].dropna().tolist(),user_data[2016].dropna().tolist(),
#            user_data[2017].dropna().tolist(),user_data[2018].dropna().tolist()]
# # print(user_nums)
#
# boxplot=Boxplot()
# boxplot.add_xaxis(year)
# boxplot.add_yaxis("不同年份的净增长粉丝数分布",boxplot.prepare_data(user_nums))
# boxplot.render("./html/boxplot.html")


#3----------------------------散点图-----------------------------------------------------

# import pandas as pd
# from pyecharts.charts import EffectScatter
# from pyecharts import options as opts
# data=pd.read_csv('D:/testdata/scatter.csv',encoding='gb18030')
# # print(data)
#
# v1=data["芯片质量"].tolist()
# v2=data["电脑性能"].tolist()
#
# es=EffectScatter()
# es.add_xaxis(v1)
# es.add_yaxis("芯片质量与电脑性能之间的关系",v2)
# es.set_global_opts(title_opts=opts.TitleOpts(title="电脑性能评估",subtitle="副标题"))
# es.render("./html/scatter.html")


#4---------------------------Funnel漏斗图-----------------------------------------------------

#示例：
# from pyecharts.charts import Funnel
# attrs=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
# value=[20,40,60,80,100,120]
# funnel=Funnel()
# funnel.add("商品",[[attrs[i],value[i]] for i in range(len(value))])
# funnel.render("./html/Funnel.html")


#示例：
# from pyecharts.charts import Funnel
# from pyecharts import options as opts
# x_data = ["展现", "点击", "访问", "咨询", "订单"]
# y_data = [100, 80, 60, 40, 20]
#
# data = [[x_data[i], y_data[i]] for i in range(len(x_data))]
#
# (
#     Funnel()
#     .add(
#         series_name="",
#         data_pair=data,
#         gap=2,
#         tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
#         label_opts=opts.LabelOpts(is_show=True, position="inside"),
#         itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
#     )
#     .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图", subtitle="纯属虚构"))
#     .render("./html/funnel_chart.html")
# )

#实际数据
# from pyecharts.charts import Funnel
# import  pandas as pd
# # data=pd.read_clipboard()  #数据粘贴板
# data=pd.read_excel('D:/testdata/Funnel.xlsx')
# # print(data)
#
# v1=data['阶段'].tolist()
# v2=data['市场金额'].tolist()
#
# funnel=Funnel()
# funnel.add("市场分析",[[v1[i],v2[i]] for i in range(len(v1))])
# funnel.render("./html/Funnel1.html")



#5、--------------------------gauge：仪表盘------------------------

# from pyecharts import options as opts
# from pyecharts.charts import Gauge
#
# c = (
#     Gauge()
#     .add("", [("完成率", 66.6)])
#     .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
#     .render("./html/gauge_base.html")
# )


#6、-----------------------------------地理坐标图-------------------------

#官网案例：
# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.faker import Faker
#
# c = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-基本示例")
#     )
#     .render("geo_base.html")
# )


#示例1：

# import pandas as pd
# from pyecharts.charts import Geo
# from pyecharts import options as opts
# data=pd.read_excel('D:/testdata/Geodata.xlsx',sheet_name='全国')
# # print(data)
# air=data['空气质量指数'].tolist()
# # print(min(air))
# # print(max(air))
# city=data['城市'].tolist()
# # print(city)
#
# c = (
#     Geo()
#     .add_schema(maptype="china")
#     .add("空气质量指数", [list(z) for z in zip(city, air)])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="空气质量指数")
#     )
#     .render("./html/Geo.htm")
# )


#示例2：
# import pandas as pd
# from pyecharts.charts import Geo
# from pyecharts import options as opts
# data=pd.read_excel('D:/testdata/Geodata.xlsx',sheet_name='省份')
# # print(data)
# city=data['城市'].tolist()
# # print(city)
# usernums=data['用户数'].tolist()
#
# c = (
#     Geo()
#     .add_schema(maptype="湖北")
#     .add("某公众号在湖北不同城市的粉丝数量", [list(z) for z in zip(city, usernums)])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="某公众号在湖北不同城市的粉丝数量")
#     )
#     .render("./html/Geo1.htm")
# )


#示例3;
# import pandas as pd
# from pyecharts.charts import Geo
# from pyecharts import options as opts
# data=pd.read_excel('D:/testdata/Geodata.xlsx',sheet_name='city_geo')
# # print(data)
# data.index=data['city']
# data=data.drop('city',axis=1)
# # print(data)
# # print(data.T)  #转置
# data=data.T.to_dict(orient='list')
# # print(data)
# k,v=zip(*data.items())
# # print(list(k))
# c = (
#     Geo()
#     .add_schema(maptype="湖北")
#     .add("湖北省各州市经纬度", [list(z) for z in zip(list(k),list(v))])
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="湖北省各州市经纬度")
#     )
#     .render("./html/Geo2.htm")
# )


#------------------------------------GeoLines地理坐标系线图（公路交通）-----------

#示例：官网案例
# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.globals import ChartType, SymbolType
#
# c = (
#     Geo()
#     .add_schema(
#         maptype="china",
#         itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
#     )
#     .add(
#         "",
#         [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)],
#         type_=ChartType.EFFECT_SCATTER,
#         color="white",
#     )
#     .add(
#         "geo",
#         [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")],
#         type_=ChartType.LINES,
#         effect_opts=opts.EffectOpts(
#             symbol=SymbolType.ARROW, symbol_size=6, color="blue"
#         ),
#         linestyle_opts=opts.LineStyleOpts(curve=0.2),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Lines-background"))
#     .render("geo_lines_background.html")
# )

#示例1：数据来源：畅途网：https://www.changtu.com/chezhan/

# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.globals import ChartType, SymbolType
# import pandas as pd
# data=pd.read_excel('D:/testdata/公路数据.xlsx')
# # print(data)
# data['出发地']='南宁'
# data['目的地']=data['目的地'].apply(lambda s:s.strip('市'))
# # print(data)
# data=data.drop_duplicates()  #去掉重复值
# data_pairs=data.values.tolist() #转换为list数据类型
# # print(data_pairs)
#
# c = (
#     Geo()
#     .add_schema(
#         maptype="广西",
#         itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
#     )
#     .add(
#         "",
#         data_pairs,
#         type_=ChartType.EFFECT_SCATTER,
#         color="white",
#     )
#     .add(
#         "广西",
#         data_pairs,
#         type_=ChartType.LINES,
#         effect_opts=opts.EffectOpts(
#             symbol=SymbolType.ARROW, symbol_size=6, color="blue"
#         ),
#         linestyle_opts=opts.LineStyleOpts(curve=0.2),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#                      visualmap_opts=opts.VisualMapOpts(),
#                      title_opts=opts.TitleOpts(title="Geo-广西地图")
#                      )
#
# ).render('./html/Geo_Lines.html')




#示例2：数据来源12306，网址：https://kyfw.12306.cn/otn/czxx/init

# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.globals import ChartType, SymbolType
# from warnings import filterwarnings
# import pandas as pd
# data=pd.read_excel('D:/testdata/铁路数据1.xlsx')
# # print(data)
# data=data[['始发站','终到站']]
# # print(data)
# def dropDNXB(s):
#     except_citys=set(['济南','靖西'])
#     dnxb=set(['东','南','西','北'])
#     if except_citys.issuperset(set([s])):
#         return s
#     elif dnxb.issuperset(s[-1]):
#         return s[:-1]
#     else:
#         return s
# #
# # print(dropDNXB("贵阳北"))
# # print(dropDNXB('南京'))
#
# filterwarnings('ignore')  #去除警告
# data.loc[:,'始发站']=data['始发站'].apply(lambda s:dropDNXB(s))
# data.loc[:,'终到站']=data['终到站'].apply(lambda s:dropDNXB(s))
# data=data.drop_duplicates() #删除重复项
# data=data.values.tolist()
# # print(data)
#
# c = (
#     Geo()
#     .add_schema(
#         maptype="china",
#         itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
#     )
#     .add(
#         "",
#         "",
#         type_=ChartType.EFFECT_SCATTER,
#         color="white",
#     )
#     .add(
#         "南宁铁路",
#         data,
#         type_=ChartType.LINES,
#         effect_opts=opts.EffectOpts(
#             symbol=SymbolType.ARROW, symbol_size=6, color="blue"
#         ),
#         linestyle_opts=opts.LineStyleOpts(curve=0.2),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(title_opts=opts.TitleOpts(title="Geo-南宁铁路"))
#     .render('1.html')
#
# )



#示例3：航班数据预处理
# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.globals import ChartType, SymbolType
# from warnings import filterwarnings
# import pandas as pd
# data_airports=pd.read_excel('D:/testdata/航线数据.xlsx',sheet_name='airports')
# data_routes=pd.read_excel('D:/testdata/航线数据.xlsx',sheet_name='routes')
#
#
# # print(data.head())
# # data=data['Airport ID','City','Country','IATA','Latitude','Longitude','Altitude']
# data_geo=data_airports[['City','Latitude','Longitude']] #提取所需要的字段
# data_geo.index=data_geo['City']                 #将数据集的index设置为City
# data_geo=data_geo[['Longitude','Latitude']]    #删除City字段，因为其已经在索引中存在
# data_geo=data_geo.T.to_dict(orient='list')      #对数据集进行行列转置，然后转换成字典类型
# # print(data_geo)
#
# #筛选起飞或者降落在北京的航班
# data_airports=data_airports[data_airports['City']=='Beijing']
# # print(data_airports)
# airlineID=data_airports[data_airports['City']=='Beijing']['Airport ID'].tolist()
# # print(airlineID)
# airlines=data_routes[data_routes['Source airport ID'].isin(airlineID)|data_routes['Destination airport ID'].isin(airlineID)]
# print(len(airlines))
# # print(airlines)
#
# #北京起飞的航班
#
# source=airlines[airlines['Source airport ID'].isin(airlineID)][['Source airport ID','Destination airport ID']].drop_duplicates()
# # print(source)
# source['Source airport']='Beijing'
# # print(source)
# source=pd.merge(source,data_airports,left_on='Destination airport ID',right_on='Airport ID',how='left')[['Source airport','City']]
# air_source=source.values.tolist()
# print(air_source)





#收入数据自动统计与展示
#数据预处理
# import pandas as pd
# import os
# from datetime import datetime
# # df=pd.read_csv('D:/testdata/2016.csv')
# df=pd.read_excel('D:/testdata/2016.xls')
# # print(df)
# # print(df.columns)
#
# #汇总总的收入
# df['商家实际收入（元）']=df['平台红包(元)']+df['用户实付(元)']-df['第三方支付费用(元)']-df['渠道推广费用(元)']-df['平台服务费用(元)']
#
# sum_income=df[['商家实际收入（元）','订单时间']]
# print(sum_income)



















# from pyecharts.charts import Bar,Timeline
# from pyecharts import options as opts
# from pyecharts.globals import ThemeType
#
# bar=(
#     Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT,bg_color="white"))
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),  #解决标签名字过长的问题
#         title_opts=opts.TitleOpts(title="主标题",subtitle="副标题"),
#         toolbox_opts=opts.ToolboxOpts(
#             is_show=True,  # 是否显示组件
#             orient='vertical',  # 布局朝向  vertical表示纵向  horizontal表示横向
#             pos_left='90%',
#         ),
#     )
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("数量",[5, 20, 36, 10, 75, 90])
# )
#
# bar.render("1.htm")