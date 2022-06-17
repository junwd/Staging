(function(){
    var mychart = echarts.init(document.querySelector(".kk"))
    var data1 = [{
        name: '0-1K',
        value: 8570,
        sum: 20,
    },
    {
        name: '1K-2K',
        value: 25975,
        sum: 10
    },
    {
        name: '2K-3K',
        value: 15662,
        sum: 10
    },
    {
        name: '3K-4K',
        value: 6387,
        sum: 10
    },
    {
        name: '4K-5K',
        value: 3012,
        sum: 50
    },
    {
        name: '5K-6K',
        value: 1546,
        sum: 50
    },
    {
        name: '6K以上',
        value: 1987,
        sum: 50
    }
    
];

var data2 = [{
        name: '0-1k',
        value: 3595,
        sum: 20,
    },
    {
        name: '1k-2k',
        value: 19525,
        sum: 10
    },
    {
        name: '2k-3k',
        value: 18604,
        sum: 10
    },
    {
        name: '3k-4k',
        value: 8112,
        sum:10
    },
    {
        name: '4k-5k',
        value: 4590,
        sum: 50
    },
    {
        name: '5k-6k',
        value: 2504,
        sum: 50
    },
    {
        name: '6k以上',
        value: 3361,
        sum: 50
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
                top : '2%',
                right : '30%',
                itemWidth : 20,
                itemHeight : 10,
                itemGap: 40,
                orient: 'horizontal',
                icon : 'circle',
        
                textStyle : {
                    color : '#ffffff',
                    fontSize : 10,
                },
                data: ['赶集网', '贝壳租房']
            },
    grid: [{
        show: false,
        left: '-5%',
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
        formatter: '{b} : {c}'
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
                        //return '\n\n\n\n' + value;
                     // return '\n' + value
                    //  return value
                     // return value + 'virus'
                    // return value.split("").join("\n");  
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
                    color: '#e7dd53cb',
                    fontSize: 10,
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
            name: '赶集网',
            type: 'bar',
            gridIndex: 0,
            showBackground: true,
            backgroundStyle: {
                barBorderRadius: 15,
            },
            xAxisIndex: 0,
            yAxisIndex: 0,
            data: data1,
            barWidth: 10,
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
                    barBorderRadius: 15,

                },
            },

            label: {
                normal: {
                    show: true,
                    position: 'insideLeft',
                    textStyle: {
                        color: '#fff',
                        fontSize: '10'
                    }
                }
            }
        },
        {
            name: '贝壳租房',
            type: 'bar',
            xAxisIndex: 2,
            yAxisIndex: 2,
            gridIndex: 2,
            showBackground: true,
            backgroundStyle: {
                barBorderRadius: 15,
            },
            data: data2,
            barWidth: 10,
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
                    barBorderRadius: 15,

                },
            },
            label: {
                normal: {
                    show: true,
                    position: 'insideRight',
                    textStyle: {
                        color: '#ffff',
                        fontSize: '10'
                    }
                }
            }
        }
    ]
};
    mychart.setOption(option);
})();