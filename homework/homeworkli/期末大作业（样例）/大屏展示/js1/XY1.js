(function(){
    var myChart = echarts.init(document.querySelector(".kk"))
    var data1 = [{
        name: 'psy',
        value: 23.4,
        sum: 30,
    },
    {
        name: '窝均产仔数',
        value: 16,
        sum: 20
    },
    {
        name: '窝均产健仔数',
        value: 15,
        sum: 20
    },
    {
        name: '窝均断奶头数',
        value: 15,
        sum: 20
    },
    {
        name: '配种分娩率',
        value: 96,
        sum: 100
    },
    {
        name: '乳猪成活率',
        value: 98,
        sum: 100
    },
    {
        name: '保育成活率',
        value: 97,
        sum: 100
    },
    {
        name: '育肥成活率',
        value: 95,
        sum: 100
    },
    {
        name: '全群成活率',
        value: 94,
        sum: 100
    },
    {
        name: '死淘率',
        value: 5,
        sum: 100
    }
];

var data2 = [{
        name: 'psy',
        value: 20.4,
        sum: 30,
    },
    {
        name: '窝均产仔数',
        value: 10,
        sum: 20
    },
    {
        name: '窝均产健仔数',
        value: 12,
        sum: 20
    },
    {
        name: '窝均断奶头数',
        value: 13,
        sum: 20
    },
    {
        name: '配种分娩率',
        value: 90,
        sum: 100
    },
    {
        name: '乳猪成活率',
        value: 90,
        sum: 100
    },
    {
        name: '保育成活率',
        value: 91,
        sum: 100
    },
    {
        name: '育肥成活率',
        value: 94,
        sum: 100
    },
    {
        name: '全群成活率',
        value: 94,
        sum: 100
    },
    {
        name: '死淘率',
        value: 6,
        sum: 100
    }
];
// data = data.sort((a, b) => {
//     return b.value - a.value
// });
getArrByKey = (data, k) => {
    let key = k || "value";
    let res = [];
    if (data) {
        data.forEach(function(t) {
            res.push(t[key]);
        });
    }
    return res;
};
opt = {
    index: 0
}
colorLeft = ['#0CEBEA', '#368BFF'];
colorRight = ['#00CC99', '#64FE67']

option = {
    legend : {
                top : '5%',
                right : '10%',
                itemWidth : 50,
                itemHeight : 22,
                itemGap: 40,
                orient: 'horizontal',
                icon : 'circle',
        
                textStyle : {
                    color : '#ffffff',
                    fontSize : 20,
                },
                data: ['规模猪场', '中小猪场']
            },
    grid: [{
        show: false,
        left: '2%',
        top: '10%',
        bottom: '8%',
        width: '39%',

    }, {
        show: false,
        left: '50%',
        top: '10%',
        bottom: '8%',
        width: '0%',

    }, {
        show: false,
        right: '2%',
        top: '10%',
        bottom: '8%',
        width: '39%',
    }],
    tooltip: {
        show: true,
        formatter: '{b} : {c}%'
    },
    xAxis: [{
            type: 'value',
            inverse: true,
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            position: 'bottom',
            axisLabel: {
                show: false,
            },
            splitLine: {
                show: false
            }
        }, {
            gridIndex: 1,
            show: false,
        },
        {
            gridIndex: 2,
            show: true,
            type: 'value',
            inverse: false,
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            position: 'bottom',
            axisLabel: {
                show: false,
                //     formatter:function(value)  
                //   {  
                //         //return '\n\n\n\n' + value;
                //      // return '\n' + value
                //      return value
                //      // return value + 'virus'
                //     // return value.split("").join("\n");  
                //   },
                textStyle: {
                    color: 'white'
                }
            },
            splitLine: {
                show: false
            }
        }
    ],
    yAxis: [{
            gridIndex: 0,
            triggerEvent: true,
            show: true,
            inverse: true,
            data: getArrByKey(data1, 'name'),
            axisLine: {
                show: false
            },
            splitLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false
            }
        },
        {
            gridIndex: 1,
            type: 'category',
            inverse: true,
            position: 'left',
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                show: true,
                interval: 0,
                align: 'auto',
                verticalAlign: 'middle',
                textStyle: {
                    color: '#ffffff',
                    fontSize: 16,
                    align: 'center',

                },

            },
            data: getArrByKey(data1, 'name'),
        },
        {
            gridIndex: 2,
            triggerEvent: true,
            show: true,
            inverse: true,
            data: getArrByKey(data2, 'name'),
            axisLine: {
                show: false
            },
            splitLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                show: false,
            }
        }
    ],
    series: [

        {
            name: '规模猪场',
            type: 'bar',
            gridIndex: 0,
            showBackground: true,
            backgroundStyle: {
                barBorderRadius: 30,
            },
            xAxisIndex: 0,
            yAxisIndex: 0,
            data: data1,
            barWidth: 20,
            // barCategoryGap: '40%',
            itemStyle: {
                normal: {
                    show: true,
                    // 线性渐变，前四个参数分别是 x0, y0, x2, y2, 范围从 0 - 1，分别表示右,下,左,上。例如（0，0，0，1）表示从正上开始向下渐变；如果是（1，0，0，0），则是从正右开始向左渐变。
                    // 相当于在图形包围盒中的百分比，如果最后一个参数传 true，则该四个值是绝对的像素位置
                    color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                        offset: 0,
                        color: colorLeft[0] //指0%处的颜色
                    }, {
                        offset: 1,
                        color: colorLeft[1] //指100%处的颜色
                    }], false),
                    barBorderRadius: 30,

                },
            },

            label: {
                normal: {
                    show: true,
                    position: 'insideLeft',
                    textStyle: {
                        color: '#ffffff',
                        fontSize: '12'
                    }
                }
            }
        },
        {
            name: '中小猪场',
            type: 'bar',
            xAxisIndex: 2,
            yAxisIndex: 2,
            gridIndex: 2,
            showBackground: true,
            backgroundStyle: {
                barBorderRadius: 30,
            },
            data: data2,
            barWidth: 20,
            // barCategoryGap: '40%',
            itemStyle: {
                normal: {
                    show: true,
                    // 线性渐变，前四个参数分别是 x0, y0, x2, y2, 范围从 0 - 1，分别表示右,下,左,上。例如（0，0，0，1）表示从正上开始向下渐变；如果是（1，0，0，0），则是从正右开始向左渐变。
                    // 相当于在图形包围盒中的百分比，如果最后一个参数传 true，则该四个值是绝对的像素位置
                    color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                        offset: 0,
                        color: colorRight[0] //指0%处的颜色
                    }, {
                        offset: 1,
                        color: colorRight[1] //指100%处的颜色
                    }], false),
                    barBorderRadius: 30,

                },
            },
            label: {
                normal: {
                    show: true,
                    position: 'insideRight',
                    textStyle: {
                        color: '#ffffff',
                        fontSize: '12'
                    }
                }
            }
        }
    ]
};
    myChart.setOption(option);
})();