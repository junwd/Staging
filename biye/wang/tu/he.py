from pyecharts.charts import Page
from bai import bar, x1data, y1data
from bar import bars, x3data, y3data
from barlos import barlos, x4data, y4data, z4data
from pie import pie, x2data, y2data
from bar_rev import bar_rev, x6data, y6data


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout, page_title="基于Python的贝壳分析大屏", )
    page.add(
        bar(x1data, y1data),
        bars(x3data, y3data),
        barlos(x4data, y4data, z4data),
        pie(x2data, y2data),
        bar_rev(x6data, y6data)
    )
    # page.render("page.html")
    page.save_resize_html("page.html", cfg_file="chart_config.json", dest="大屏.html")


if __name__ == "__main__":
    page_draggable_layout()
