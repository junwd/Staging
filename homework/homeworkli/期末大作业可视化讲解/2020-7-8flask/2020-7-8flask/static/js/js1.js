//建立axjx所需的json数据
        var app={
            year:[],
            count:[]


        };

        //发送ajax请求
        $(document).ready(function () {
       getData();
       console.log(app.year);
       console.log(app.count)
    });
//设计画图
    function getData()
    {
         $.ajax({
         //渲染的是127.0.0.1/test 下的json数据
            url:'/getdata',
            data:{},
            type:'POST',
            async:false,
            dataType:'json',
            success:function(data) {
                app.year = data.year;
                app.count = data.count;
  }
            })
    }

$(function () {
echarts_1();
echarts_2();
echarts_3();
echarts_4();


function echarts_1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('mybar'));

     var option_bar = {

    "series": [
        {
            "type": "bar",
            "data": app.count,
            "barCategoryGap": "70%",
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "itemStyle": {
                "normal": {
                    "color": new echarts.graphic.LinearGradient(0, 0, 0, 1, [{                    offset: 0,                    color: 'rgba(0, 244, 255, 1)'                }, {                    offset: 1,                    color: 'rgba(0, 77, 167, 1)'                }], false),
                    "barBorderRadius": [
                        30,
                        30,
                        30,
                        30
                    ],
                    "shadowColor": "rgb(0, 160, 221)"
                }
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selected": {
                "": true
            }
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 3,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid",

                }
            },
             axisLabel: {
                                show: true,
                                textStyle: {
                                    color: "#ffffff"
                                },


                            },

            "data":app.year
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }


            },
            axisLabel: {
                            show: true,
                            textStyle: {
                                color: '#ffffff'
                            }
                        }
        }
    ]
}
myChart.setOption(option_bar);
}

function echarts_2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('myline'));


        var option_line = {
    "animation": true,

    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "series": [
        {
            "type": "line",
            "name": "2020\u5e74",
            "connectNulls": false,
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "step": false,
            "data":app.count,
            "hoverAnimation":true,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "width": 4,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                },
                "data": [
                    {
                        "type": "max"
                    }
                ]
            }
        },
        {
            "type": "line",
            "name": "2019\u5e74",
            "connectNulls": false,
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "step": false,
            "data": [
                [
                    "1\u6708",
                    5
                ],
                [
                    "2\u6708",
                    7
                ],
                [
                    "3\u6708",
                    42
                ],
                [
                    "4\u6708",
                    37
                ],
                [
                    "5\u6708",
                    55
                ],
                [
                    "6\u6708",
                    47
                ],
                [
                    "7\u6708",
                    23
                ],
                [
                    "8\u6708",
                    23
                ],
                [
                    "9\u6708",
                    49
                ],
                [
                    "10\u6708",
                    46
                ],
                [
                    "11\u6708",
                    45
                ],
                [
                    "12\u6708",
                    45
                ]
            ],
            "hoverAnimation": true,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "width": 4,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            },
            "markPoint": {
                "label": {
                    "show": true,
                    "position": "inside",
                    "color": "#fff",
                    "margin": 8
                },
                "data": [
                    {
                        "type": "max"
                    }
                ]
            }
        },
        {
            "type": "line",
            "name": "2018\u5e74",
            "connectNulls": false,
            "symbolSize": 4,
            "showSymbol": true,
            "smooth": false,
            "step": false,
            "data": [
                [
                    "1\u6708",
                    3
                ],
                [
                    "2\u6708",
                    11
                ],
                [
                    "3\u6708",
                    30
                ],
                [
                    "4\u6708",
                    38
                ],
                [
                    "5\u6708",
                    31
                ],
                [
                    "6\u6708",
                    39
                ],
                [
                    "7\u6708",
                    9
                ],
                [
                    "8\u6708",
                    18
                ],
                [
                    "9\u6708",
                    26
                ],
                [
                    "10\u6708",
                    22
                ],
                [
                    "11\u6708",
                    17
                ],
                [
                    "12\u6708",
                    230
                ]
            ],
            "hoverAnimation": true,
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "lineStyle": {
                "width": 4,
                "opacity": 1,
                "curveness": 0,
                "type": "solid"
            },
            "areaStyle": {
                "opacity": 0
            }
        }
    ],
    "legend": [
        {
            "data": [
                "2020\u5e74",
                "2019\u5e74",
                "2018\u5e74"
            ],
            "selected": {
                "2020\u5e74": true,
                "2019\u5e74": true,
                "2018\u5e74": true
            }
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "xAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            },
            "data": [
                "2020年",
                "2019年",
                "2018年",
                "2017年",
                "2016年",
                "2015年",
                "2014年",
                "2013年",
                "2012年",
                "2011年",
                "2010年",
                "2009年",
                "2008年"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ]
};
       myChart.setOption(option_line);
}


})

function echarts_3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('mypie'));
        var option_pie = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "pie",
            "clockwise": true,
            "data":app.count,
            "radius": [
                "40%",
                "75%"
            ],
            "center": [
                "50%",
                "50%"
            ],
            "label": {
                "show": true,
                "position": "top",
                "margin": 8,
                "formatter": "{b}: {c}"
            },
            "rippleEffect": {
                "show": true,
                "brushType": "stroke",
                "scale": 2.5,
                "period": 4
            }
        }
    ],
    "legend": [
        {
            "data": [
                " 2020",
                " 2019",
                " 2018",
                " 2017",
                " 2016",
                " 2015",
                " 2014",
                " 2013",
                " 2012",
                " 2011",
                " 2010",
                " 2009",
                " 2008"
            ],
            "selected": {},
            "show": true,
            "left": "2%",
            "top": "15%",
            "orient": "vertical",
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "title": [
        {}
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "itemSize": 15,
        "itemGap": 10,
        "left": "90%",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "save as image",
                "type": "png"
            },
            "restore": {
                "show": true,
                "title": "restore"
            },
            "dataView": {
                "show": true,
                "title": "data view",
                "readOnly": false
            },
            "dataZoom": {
                "show": true,
                "title": {
                    "zoom": "data zoom",
                    "back": "data zoom restore"
                }
            }
        }
    }
}
myChart.setOption(option_pie);
}

function echarts_4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('myscratter'));
    console.log(myChart);
     var option_scatter = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",

    ],
    "series": [
        {
            "type": "scatter",
            "name": "\u4fe1\u606f\u5206\u5e03\u4e0e\u5e74\u4efd",
            "symbolSize": 10,
            "data": app.count,
            "label": {
                "show": true,
                "position": "right",
                "margin": 8
            }
        }
    ],
    "legend": [
        {
            "data": [
                "\u4fe1\u606f\u5206\u5e03\u4e0e\u5e74\u4efd"
            ],
            "selected": {
                "\u4fe1\u606f\u5206\u5e03\u4e0e\u5e74\u4efd": true
            }
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    "xAxis": [
        {
            "show": true,
            "scale": true ,

            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 4,
                    "color":"red",
                    "opacity": 0.5,
                    "curveness": 4,
                    "type": "solid"
                }
            },
            "data": [
                " 2020",
                " 2019",
                " 2018",
                " 2017",
                " 2016",
                " 2015",
                " 2014",
                " 2013",
                " 2012",
                " 2011",
                " 2010",
                " 2009",
                " 2008"
            ]
        }
    ],
    "yAxis": [
        {
            "show": true,
            "scale": false,
            "nameLocation": "end",
            "nameGap": 15,
            "gridIndex": 0,
            "inverse": false,
            "offset": 0,
            "splitNumber": 5,
            "minInterval": 0,
            "splitLine": {
                "show": false,
                "lineStyle": {
                    "width": 1,
                    "opacity": 1,
                    "curveness": 0,
                    "type": "solid"
                }
            }
        }
    ]
}
       myChart.setOption(option_scatter);
}



















