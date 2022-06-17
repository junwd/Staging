(function(){
    var mychart = echarts.init(document.querySelector(".kk"))
    // Generate data
   
var opts = [];
var timedata = ["2015", "2016", "2017","2018","2019"];
var name = [["北京市", "上海市", "深圳市","成都市","杭州市","广州市","苏州市","宁波市","湖州市","长沙市"],
            [ "深圳市", "北京市","上海市","无锡市","苏州市","杭州市","广州市","成都市","武汉市","南京市"],
            [ "深圳市","上海市","杭州市", "北京","浙江","江苏","南京市","广州市","广东","宁波市"],
             [ "深圳市", "北京市","上海市","南京市","成都市","武汉市","无锡市","绍兴市","长沙市","杭州市"],
              ["北京市", "上海市", "青岛市", "杭州市","苏州市","深圳市","南京市","成都市","宁波市","广州市"]];
var data1 = [["28", "19", "14","12","9","7","6","6","5","5"],
             ["29", "17","17","13","13","13","10","7","7","6"],
             ["38", "29", "24", "22","19","15","14","14","13","13"],
             ["11", "9", "9", "6","5","5","5","4","3","3"],
             ["15", "14", "7", "7","7","7","5","4","4","4"]];
// var data2 = [["4", "1", "5"],["4", "1"],["4", "1", "5", "9"]];
for (var i = 0; i < timedata.length; i++) {
    conditions = [{
        '类别': timedata[i]
    }]
    opts.push({
        // backgroundColor: '#051F54',
        xAxis: {
            "type": "category",
            "axislabel": {
                "interval": 0
            },
            splitLine: {
                show: false
            },
            data: name[i]
        },
        series: {
            type: 'bar',
            barWidth: 23,
            itemStyle: {//图形样式
                normal: {
                    barBorderRadius: 20,
					color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 1, color: 'rgb(29, 141, 211)'
                    },{
                        offset: 0, color: 'rgb(56, 206, 191)'
                    }], false),
                },
            },
            name: "城市",
            data: data1[i],
        }
    })
}

var option = {
    baseOption: {
        grid: {
            // x: '26%',
            top: '18%',
            bottom: '20%',
            height:'62%',
            width: '80%',
        },
        timeline: {
            axisType: "category",
            autoPlay: true,
            //rewind: true,
            playInterval: 2000,
            //orient: "vertical",
            lineStyle: {
                color: "#fff"
            },
            label: {
                fontSize: 12,
                textStyle: {
                    color: "#fff"
                }
            },
            checkpointStyle: {
                color: "#4c647c"
            },
            left: "4%",
            right: "4%",
            top: '95%',
            bottom: "13%",
            //padding: [30, 10, 20, -10],
            data: timedata
        },
        legend: {
            right:'37%',
            top:'2%',
            itemWidth: 18,
            itemHeight: 10,
            textStyle: {
    			color: '#fff',
    			fontStyle: 'normal',
    			fontFamily: '微软雅黑',
    			fontSize: 12,            
            },
        },
        calculable: true,
        xAxis: {
            type: 'category',
			axisTick:{//坐标轴刻度相关设置。
				show: false,
			},
			axisLine:{//坐标轴轴线相关设置
				lineStyle:{
					color:'#fff',
					opacity:1
				}
			},
            axisLabel: {
                interval: 0,
                //rotate:40,
                textStyle: {
                     fontSize:12,
				     color:'#fff',
                }
            },
            splitLine: {
                show: false
            },
            data: opts
        },
        yAxis: {
            type: 'value',
			axisLabel: {
				textStyle: {
					color: '#fff',
					fontStyle: 'normal',
					fontFamily: '微软雅黑',
					fontSize: 12,
				}
			},
            axisTick:{//坐标轴刻度相关设置。
				show: false,
			},
			axisLine:{//坐标轴轴线相关设置
				lineStyle:{
					color:'#fff',
					opacity:1
				}
			},
			splitLine: {
				show: true,
				lineStyle: {
					color: ['#000'],
					opacity:0.06
				}
			}
        }
    },

    //图表内数据
    options: opts,
};
    mychart.setOption(option);
})();