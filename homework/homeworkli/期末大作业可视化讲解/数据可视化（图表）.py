#绘制图表的三种方式
#1.生成html
#2.在jupyter notebook中展示
#3.保存png等格式的文件

#jupyter notebook的设置：
#upyter Notebook 设置黑色背景主题、字体大小、代码自动补全
#网址： https://www.bbsmax.com/A/A7zgRoZWd4/


#pyecharts生成图片
#需要做两件事
#1.安装软件 ：snapshot-selenium
# 或者：pip install snapshot-selenium

# 2.配置环境变量
#我们需要把我们的chromedriver驱动放到我们path环境变量下

#官网：https://github.com/pyecharts/pyecharts-gallery


#--------------------------柱状图---------------------------------------

#主要的知识点：
#pyecharts全局参数设置
#jupyter notebook 和 pyecharm 基本图表绘制
#如何绘制一个简单Bar图
#设置图表大小
#封装一些绘制图表的函数
#设置图例
#区域缩放的配置项

#1.入门绘制一个简单的Bar图
#示例1：柱状图
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# x=["java","python","javascript"]
# y=[111,100,67]
# x=["0-59分","60-79分","80-89分","90-100分"]
# y=[3,6,30,10]
# bar=Bar() #实例对象
# bar.add_xaxis(xaxis_data=x) #x轴坐标的数据
# bar.add_yaxis(series_name='',y_axis=y) #图例名称+y周的坐标
# bar.set_global_opts(title_opts=opts.TitleOpts(title="拓展任务",subtitle="拓展任务评分统计"))
# bar.render('./html1/bar112.html')

#示例1继续：-----添加数据项
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# x=["java","python","javascript"]
# y1=[111,100,67]
# y2=[233,342,190]

# bar=Bar() #实例对象
# bar.add_xaxis(xaxis_data=x) #x轴坐标的数据
# bar.add_yaxis(series_name='平台A',y_axis=y1) #图例名称+y周的坐标
# bar.add_yaxis(series_name='平台B',y_axis=y2)
# bar.set_global_opts(title_opts=opts.TitleOpts(title="平台A与平台B",subtitle="平台数据对比"))
# bar.render('./html1/bar2.html')


#示例1继续-----------x轴与Y轴数据进行转换/设置图表大小
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# # x=["java","python","javascript"]
# # y1=[111,100,67]
# # y2=[233,342,190]
# x=["0-59分","60-79分","80-89分","90-100分"]
# y1=[3,6,30,10]
# y2=[4,7,28,11]
# bar=Bar(init_opts=opts.InitOpts(width='1200px',height='600px')) #实例对象+调整宽度+高度
# bar.add_xaxis(xaxis_data=x) #x轴坐标的数据
# bar.add_yaxis(series_name='A班',y_axis=y1) #图例名称+y周的坐标
# bar.add_yaxis(series_name='B班',y_axis=y2)
# bar.reversal_axis()      #x轴与Y轴数据进行转换
# bar.set_global_opts(title_opts=opts.TitleOpts(title="A班与B班",subtitle="拓展任务成绩对比"))
# bar.render('./html1/bar3.html')



#示例1：继续-----------文本倾斜度设置
#在set_global_opts 参数设置，可以通过Labelopts类中属性 rotate来进行操作

# from pyecharts.charts import Bar
# from pyecharts import options as opts
# x=["java","python","javascript"]
# y1=[111,100,67]
# y2=[233,342,190]
# bar=Bar(init_opts=opts.InitOpts(width='1200px',height='600px')) #实例对象+调整宽度+高度
# bar.add_xaxis(xaxis_data=x) #x轴坐标的数据
# bar.add_yaxis(series_name='平台A',y_axis=y1) #图例名称+y周的坐标
# bar.add_yaxis(series_name='平台B',y_axis=y2)
# bar.reversal_axis()      #x轴与Y轴数据进行转换
# bar.set_global_opts(
#     title_opts=opts.TitleOpts(title="平台A与平台B",subtitle="平台数据对比"),
#     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=50))
#      )
# bar.render('./html1/bar4.html')

#示例1：封装Bar绘制图表的函数
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# def bar_charts()->Bar():
#     x=["java","python","javascript"]
#     y1=[111,100,67]
#     c=Bar(init_opts=opts.InitOpts(width='1000px',height='600px'))
#     c.add_xaxis(xaxis_data=x)
#     c.add_yaxis(series_name='',y_axis=y1)
#     c.reversal_axis()
#     c.set_global_opts(
#         title_opts=opts.TitleOpts(title='用户量统计'),
#         yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate='50')),
#         toolbox_opts=opts.ToolboxOpts(
#             is_show=True,
#             orient='vertical',
#             pos_left='90%'
#         )
#     )
#     return c
#
# #调用函数
# if __name__=="__main__":
#     c=bar_charts()
#     c.render("./html1/bar5.html")

#示例1：继续---设置图例+区域缩放的配置项

# from pyecharts.charts import Bar
# from pyecharts import options as opts
# x=["java","python","javascript"]
# y1=[111,100,67]
# y2=[233,342,190]
# bar=Bar(init_opts=opts.InitOpts(width='1200px',height='600px')) #实例对象+调整宽度+高度
# bar.add_xaxis(xaxis_data=x) #x轴坐标的数据
# bar.add_yaxis(series_name='平台A',y_axis=y1) #图例名称+y周的坐标
# bar.add_yaxis(series_name='平台B',y_axis=y2)
# bar.reversal_axis()      #x轴与Y轴数据进行转换
# bar.set_global_opts(
#     title_opts=opts.TitleOpts(title="平台A与平台B",subtitle="平台数据对比"),
#     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=50)),
#     legend_opts=opts.LegendOpts(is_show=True),  #is-show=True 图例是否显示,默认为True
#     datazoom_opts=opts.DataZoomOpts(type_='slider',range_start=0,range_end=1000)
#
#      )
# bar.render('./html1/bar6.html')



#示例2：pyecharts生成图片
# from snapshot_selenium import snapshot as driver
# from pyecharts import options as opts
# from pyecharts.charts import Bar
# from pyecharts.render import make_snapshot
# def bar_chart()->Bar:
#     x=["java","python","javascript"]
#     y1=[111,100,67]
#     y2=[233,342,190]
#     bar=Bar() #实例对象
#     bar.add_xaxis(xaxis_data=x) #x轴坐标的数据
#     bar.add_yaxis(series_name='平台A',y_axis=y1) #图例名称+y周的坐标
#     bar.add_yaxis(series_name='平台B',y_axis=y2)
#     bar.set_global_opts(title_opts=opts.TitleOpts(title="平台A与平台B",subtitle="平台数据对比"))
#     return bar
# c=bar_chart()
# make_snapshot(driver,c.render(),'bar.png')

#----------------------折线图--------------------------------------
#知识点：
#绘制一个简单的Line charts
#pyecharts 增加标题与图例
#pyecharts 增加提示项目信息
#pyecharts 工具箱设置

#示例1：
# import pyecharts.options as opts
# from pyecharts.charts import Line
# x=['seaborn','matplotlib','plotly','pyecharts','python']
# y1=[230,345,450,560,230]
# y2=[450,800,600,340,460]

# def line_charts()->Line:
#     c=Line()
#     c.add_xaxis(xaxis_data=x)
#     c.add_yaxis(series_name='',y_axis=y1)
#     c.add_yaxis(series_name='',y_axis=y2)
#     return c
# #绘制图表
# c=line_charts()
# c.render("./html1/line111.html")

#示例1：继续：增加标题与图例
# import pyecharts.options as opts
# from pyecharts.charts import Line
# x=['seaborn','matplotlib','plotly','pyecharts','python']
# y1=[230,345,450,560,230]
# y2=[450,800,600,340,460]
# def line_charts()->Line:
#     c=Line()
#     c.add_xaxis(xaxis_data=x)
#     c.add_yaxis(series_name='平台A-',y_axis=y1) #series_name=图例名称
#     c.add_yaxis(series_name='平台B-',y_axis=y2)
#     #全局数据项的设置
#     c.set_global_opts(
#         title_opts=opts.TitleOpts(title='可视化软件的用户量情况统计'),
#         legend_opts=opts.LegendOpts(is_show=True)
#     ) #is_show=True 默认 展示图例，False是不显示图例
#
#     return c
# #绘制图表
# c=line_charts()
# c.render("./html1/line2.html")


#示例1：继续---增加工具箱（提示项）
#pyecharts中提供类Tooltipopts

# import pyecharts.options as opts
# from pyecharts.charts import Line
# x=['seaborn','matplotlib','plotly','pyecharts','python']
# y1=[230,345,450,560,230]
# y2=[450,800,600,340,460]
# def line_charts()->Line:
#     c=Line()
#     c.add_xaxis(xaxis_data=x)
#     c.add_yaxis(series_name='平台A-',y_axis=y1) #series_name=图例名称
#     c.add_yaxis(series_name='平台B-',y_axis=y2)
#     #全局数据项的设置
#     c.set_global_opts(
#         title_opts=opts.TitleOpts(title='可视化软件的用户量情况统计'),
#         legend_opts=opts.LegendOpts(is_show=True),
#         tooltip_opts=opts.TooltipOpts(trigger='axis',axis_pointer_type='cross')
#     ) #is_show=True 默认 展示图例，False是不显示图例
#
#     return c
# #绘制图表
# c=line_charts()
# c.render("./html1/line3.html")


#示例1：继续：工具箱设置

# import pyecharts.options as opts
# from pyecharts.charts import Line
# # x=['seaborn','matplotlib','plotly','pyecharts','python']
# # y1=[230,345,450,560,230]
# # y2=[450,800,600,340,460]
# x=["0-59分","60-79分","80-89分","90-100分"]
# y1=[3,6,30,10]
# y2=[4,7,28,11]
# def line_charts()->Line:
#     c=Line()
#     c.add_xaxis(xaxis_data=x)
#     c.add_yaxis(series_name='A班',y_axis=y1) #series_name=图例名称
#     c.add_yaxis(series_name='B班',y_axis=y2)
#     #全局数据项的设置
#     c.set_global_opts(
#         title_opts=opts.TitleOpts(title='A班与B班拓展任务成绩对比情况'),
#         legend_opts=opts.LegendOpts(is_show=True),
#         tooltip_opts=opts.TooltipOpts(trigger='axis',axis_pointer_type='cross'),
#         toolbox_opts=opts.ToolboxOpts(
#             is_show=True,  # 是否显示组件
#             orient='vertical', # 布局朝向  vertical表示纵向  horizontal表示横向
#             pos_left='90%',
#         )
#     ) #is_show=True 默认 展示图例，False是不显示图例
#
#
#     return c
# #绘制图表
# c=line_charts()
# c.render("./html1/line41.html")



#---------------:折线图+柱状图 组合-----------------------------------
#柱状图：y轴显示不同平台的销售数量
#折线图：y轴另外一侧显示不同平台课程对应的价格
# from pyecharts.charts import Bar,Line
# from pyecharts import options as opts
# x=['python','Seaborn','plotly','pyecharts']
# #1.绘制柱状图
# def bar_charts()->Bar():
#     y1=[1140,556,234,440]
#     y2=[570,1340,2300,400]
#     bar=Bar(init_opts=opts.InitOpts(width='1000px',height='600px'))
#     bar.add_xaxis(xaxis_data=x)
#     bar.add_yaxis(series_name='平台A-销售数量',y_axis=y1)
#     bar.add_yaxis(series_name='平台B-销售数量',y_axis=y2)
#     bar.set_global_opts(
#         title_opts=opts.TitleOpts(title='不同平台的销售情况统计'),
#         legend_opts=opts.LegendOpts(is_show=True),
#     )
#     bar.extend_axis(yaxis=opts.AxisOpts(
#         name='价格',
#         type_='value',
#         min_=0,
#         max_=200,
#         interval=10,
#         axislabel_opts=opts.LabelOpts(formatter='{value}元')
#         ))
#     return bar
#
#
# #2.绘制折线图
# def line_charts()->Line():
#     y=[159,29,49,79]
#     c=Line()
#     c.add_xaxis(xaxis_data=x)
#     c.add_yaxis(series_name='价格',yaxis_index=1,y_axis=y,label_opts=opts.LabelOpts(is_show=False))
#
#     return c
#
#
#
# #3.Bar+Line组合
# bar=bar_charts()
# line=line_charts()
# bar.overlap(line).render("./html1/bar_line.html")


#:------------------饼图：pie-----------------------------------
#pie需要的数据格式
#[[x1,y1],[x2,y2],....]
#构建饼图的数据
#为pie示例对象添加数据
#设置标题
#设置每一项占比


#示例1：
# from pyecharts.charts import Pie
# from pyecharts import options as opts
#
# #构建数据
#
x=['直接访问','营销推广','博客引擎','搜索引擎']
y=[340,450,230,670]
# # print(list(zip(x,y)))  #[('直接访问', 340), ('营销推广', 450), ('博客引擎', 230), ('搜索引擎', 670)]
# data=[list(z) for z in list(zip(x,y))]
# # print(data)   #[['直接访问', 340], ['营销推广', 450], ['博客引擎', 230], ['搜索引擎', 670]]
# def pie_charts()->Pie():
#     c=Pie(init_opts=opts.InitOpts(width='800px',height='500px'))
#     c.add(series_name='访问来源',data_pair=data)
#     c.set_global_opts(
#         title_opts=opts.TitleOpts(title="课程不同的销售来源分析",pos_left='center',pos_top='5%'),
#         toolbox_opts=opts.ToolboxOpts(
#             is_show=True,
#             orient='vertical',
#             pos_left='95%'
#         )
#     )
#     #设置每一项的占比
#     c.set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter='{a}<br/>{b}:{c}({d}%)'),
#                       label_opts=opts.LabelOpts(formatter="{b}:{c}"))   #显示比例
#     return c
#
# c=pie_charts()
# c.render('./html1/pie1.html')



#示例2：圆弧状pie

# from pyecharts.charts import Pie
# from pyecharts import options as opts
#
# #构建数据
#
# x=['直接访问','营销推广','博客引擎','搜索引擎']
# y=[340,450,230,670]
# # print(list(zip(x,y)))  #[('直接访问', 340), ('营销推广', 450), ('博客引擎', 230), ('搜索引擎', 670)]
# data=[list(z) for z in list(zip(x,y))]
# # print(data)
# def pie_radius_charts()->Pie():
#     c=Pie()
#     c.add(series_name='访问来源',data_pair=data,radius=['40%','75%'])
#     #设置全局变量
#     c.set_global_opts(
#         title_opts=opts.TitleOpts(title='用户量不同的点击统计情况'),
#         legend_opts=opts.LegendOpts(orient='vartical',pos_left='2%',pos_top='20%')
#     )
#     #设置占比
#     c.set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter='{a}<br/>{b}:{c} ({d}%)'))
#
#     return c
# c=pie_radius_charts()
# c.render('./html1/pie2.html')



#：----------------------------散点图：scatter-------------------------------------

#构建scatter散点图的数据
#示例1：
# from pyecharts.charts import Scatter
# from pyecharts import options as opts
# import numpy as np
# x=np.linspace(1,10,30)
# # print(x)
# y1=np.cos(x)
# y2=np.sin(x)
# #绘制散点图
# scatter=Scatter(init_opts=opts.InitOpts(width='1000px',height='600px'))
# scatter.add_xaxis(xaxis_data=x)
# scatter.add_yaxis(series_name='y=cos(x)函数散点图',y_axis=y1,label_opts=opts.LabelOpts(is_show=False))
# scatter.add_yaxis(series_name='y=sin(x)函数散点图',y_axis=y2,label_opts=opts.LabelOpts(is_show=False))
# scatter.set_global_opts(title_opts=opts.TitleOpts(title='第一个散点图',pos_top='20px',pos_left='center'))
# scatter.render('./html1/scatter1.html')


#示例2：如何设置散点图大小
#标记的大小，课设置一些数字 。symbol_size:Numberic=0

#Echarts提供类型：circle rect roundRect triangle diamond pin arrow none
# symbol=' '

# from pyecharts.charts import Scatter
# from pyecharts import options as opts
# import numpy as np
# x=np.linspace(1,10,30)
# # print(x)
# y1=np.cos(x)
# y2=np.sin(x)
# #绘制散点图
# scatter=Scatter(init_opts=opts.InitOpts(width='1000px',height='600px'))
# scatter.add_xaxis(xaxis_data=x)
# scatter.add_yaxis(
#     series_name='y=cos(x)函数散点图',
#     y_axis=y1,
#     label_opts=opts.LabelOpts(is_show=False),
#     symbol_size=15,  #控制散点图 点的大小
#     symbol='triangle'  #控制散点图 点的形状 ：triangle:三角形 ，diamond正方形
#     )
# scatter.add_yaxis(
#     series_name='y=sin(x)函数散点图',
#     y_axis=y2,
#     label_opts=opts.LabelOpts(is_show=False)
#     )
# scatter.set_global_opts(
#     title_opts=opts.TitleOpts(title='第一个散点图',pos_top='20px',pos_left='center')
# )
# scatter.render('./html1/scatter2.html')



#：-------------------------词云图：WordCloud词云------------------------
# from pyecharts.charts import WordCloud
# from pyecharts import options as opts
#
# data_pair=[
#     ('窦骁何超莲反手抱',4889550 ),
#     ('特朗普遭52家科技巨头联名起诉',2330135),
#     ('雷军十年演讲',2097428),
#     ('罗霈颖死因',2011357 ),
#     ('王思聪 鞠婧祎',1870),
#     ('雷军首次回应与董明珠赌约',1302024)
# ]
#
# wordcloud=WordCloud()
# wordcloud.add(series_name='热搜词榜单',data_pair=data_pair)
# wordcloud.set_global_opts(title_opts=opts.TitleOpts(title='词云图'))
# wordcloud.render('./html1/wordcloud.html')


#-----------------pyecharts geo 地理图-------------------------

# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.globals import ChartType
# import pyecharts
# import warnings
# warnings.filterwarnings('ignore')
# # print('pyecharts version=',pyecharts.__version__)  #查看pyecharts的版本
# #绘制地理图
# data=[['广东',3000],['山东',2800],['上海',2300],['北京',2100],['浙江',2000]]
#
# def geo_charts()->Geo():
#     c=Geo()
#     c.add_schema(
#         maptype='china',
#         is_roam=False,
#         label_opts=opts.LabelOpts(is_show=True)
#     )
#     c.add(
#         series_name='geo',
#         data_pair=data,
#         type_=ChartType.EFFECT_SCATTER,
#         symbol_size=12,symbol='pin'
#     )
#     c.set_global_opts(title_opts=opts.TitleOpts(title='中国城市GDP的数据汇总'))
#     return c
#
# geo=geo_charts()
# geo.render('./html1/geo_china.html')

from selenium import webdriver   #导入selenium库中的webdriver接口
driver=webdriver.Chrome()     #创建phantomjs浏览器对象
driver.get("http://www.baidu.com/")  #发请求get()
driver.save_screenshot("百度.png")    #获取网页截屏
print("图片保存成功")
driver.quit()   #关闭
