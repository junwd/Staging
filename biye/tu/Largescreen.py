from pyecharts.charts import Page

from table import table, xdata9
from bar_with_axis_off import bar_with_axis_off, xdata1, ydata1
from bar_with_default_selected_series import bar_with_default_selected_series, xdata2, ydata2
from bar_with_linear_gradient_color import bar_with_linear_gradient_color, xdata3, ydata3
from pie_custom_radius import pie_custom_radius, xdata4, ydata4
from pie_multiple import pie_multiple, xdata6, ydata6, xdata5, ydata5
from chiyun_yun import yun, xdata11
from beijing import beijing
from pyecharts.commons.utils import JsCode
def page_draggable_layout():
    page = Page(layout=Page.DraggablePageLayout, page_title="基于Python的贝壳分析大屏", )
    page.add(
        beijing(),
        bar_with_axis_off(xdata1, ydata1),
        bar_with_default_selected_series(xdata2, ydata2),
        bar_with_linear_gradient_color(xdata3, ydata3),
        yun(xdata11),
        pie_multiple(xdata6, ydata6, xdata5, ydata5),
        pie_custom_radius(xdata4, ydata4),
        table(xdata9),
    )
    # page.render("ls.html")
    page.save_resize_html("ls.html", cfg_file="chart_config.json", dest="大屏.html")


if __name__ == "__main__":
    page_draggable_layout()
