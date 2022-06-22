from MySQL import  selectdata
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
def pie_radius(xdata,ydata):
    v = Faker.choose()
    c = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(xdata, ydata)],
            radius=["25%", "55%"],
            center=["50%", "50%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
        # .render("pie_rosetype.html")
    )

    return c
strsql="SELECT db.`name`, db.fan FROM db ORDER BY db.fan DESC LIMIT 10"
rows=selectdata(strsql)
rows=list(rows)
print(rows)
xdata=[]
ydata=[]
for i in rows:
    # print(i[1])
    xdata.append(i[0])
    ydata.append(i[1])
pie_radius(xdata,ydata).render("Original.html")