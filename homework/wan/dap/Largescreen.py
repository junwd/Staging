from pyecharts.charts import Page

from Funnelchart import Funnelchart, a, d
from Piechart import piechart, h, t
from Polarcoordinatesystem import Polarcoordinatesystem, m, v
from histogram import histogram, f, s
from pie_radius import pie_radius, w, r
from place import place, k, p


def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout, page_title="基于Python的链家分析大屏", )
    page.add(

        Funnelchart(a, d),
        histogram(f, s),
        pie_radius(w, r),
        piechart(h, t),
        place(k, p),
        Polarcoordinatesystem(m, v)
    )
    # page.render("cs.html")
    page.save_resize_html("cs.html",cfg_file="chart_config.json", dest="css.html")

if __name__ == "__main__":
    page_draggable_layout()
