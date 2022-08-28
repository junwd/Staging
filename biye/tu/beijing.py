from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts

# def beijing():
#     image = Image()
#     img_src = (
#         "https://cdn.pixabay.com/photo/2017/09/11/14/11/fisherman-2739115_960_720.jpg"
#     )
#     image.add(
#         src=img_src,
#         style_opts={"width": "100%", "height": "700px", "style": "margin-top: 20px"},
#     )
#     image.set_global_opts(
#     )
#     # image.render("image_base.html")
#     return image


# beijing().render("image_base.html")

import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Map, Line, Bar
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode


def beijing():
    line3 = (
        Line(init_opts=opts.InitOpts(
            width="1500px",
            height="670px",
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"}))

            .add_xaxis([None])
            .add_yaxis("", [None])
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2022贝壳租房",
                                      pos_left='center',
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=25, color='#51c2d5'),
                                      pos_top='5%'),
            yaxis_opts=opts.AxisOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(is_show=False))
    )

    line3.add_js_funcs(
        """
        var img = new Image(); img.src = 'https://images.pexels.com/photos/8110777/pexels-photo-8110777.jpeg';

        """
    )
    return line3


beijing().render('13_辅助.html')
