function get_graph1(date1, date2, location){

	$.ajax({
	        url: '/data.php',    // http://188.131.157.8:8000/graphic_data_award/
	        data: {
            	date1: date1,
				date2: date2,
				location: location,
        	},
	        type: 'get',
	        dataType: "json",
	        success(res) {
	            console.log(res.byTime);
	            let timeList = [];
	            let cntList = [];
	            for (let i = 0; i < res.byTime.length; ++i) {
	                if (res.byTime[i].time !== null) {
	                    timeList.push(res.byTime[i].time);
	                    cntList.push(res.byTime[i].cnt);
	                }
	            }

				(function(){
						
						var mychart = echarts.init(document.querySelector("#graph1"));
						
						option = {
						    color: ['#3398DB'],
						    
						    title:{
//						      text:"2018-2021年中国矿业大学资助信息分布",
							  left: 'center',
							  top:10,
						    },		    
						    
						    tooltip: {
						        trigger: 'axis',
						        axisPointer: {            
						            type: 'shadow',   
						            width:"20",
						            
						        }
						    },
						    grid: {
						        left: '1%',
						        right: '1%',
						        bottom: '5%',
						        containLabel: true
						    },
						    toolbox:{
						      feature:{
						          saveAsImage:{
						          	show:true,
						          	name: location + ': ' + date1 + '-' + date2 + '道路违规信息统计图',
						          },
						      }  
						    },
						    xAxis: [
						        {
						            type: 'category',
						            data: timeList,
						            axisTick: {show:false}
						        }
						    ],
						    yAxis: [
						        {
						            type: 'value',
						            show:false,
						            axisTick:{show:false,}
						        }
						    ],
						    series: [
						        {
						            name: '违规量',
						            type: 'bar',
						            barWidth: '30',
						            data: cntList,
						            itemStyle:{
						                barBorderRadius:5
						            }
						        },
						    ]
						};
						
						mychart.setOption(option);
						
						 window.addEventListener("resize",function(){
						     mychart.resize();
						 })		
						
				})();

				console.log(timeList);
	            console.log(cntList);
	        }
	    });
}

function get_graph2(year = 2019){

	$.ajax({
	        url: 'http://188.131.157.8:8000/graphic_data_award/',  
	        data: {
            	money_year: year
        	},
	        type: 'get',
	        dataType: "json",
	        success(res) {
	            console.log(res);
	            let award_category = [
		            {
		            	value:0,
		            	name:'本科',
		            },
		            
		            {
		            	value:0,
		            	name:'硕士研究生',
		            },
		            
		            {
		            	value:0,
		            	name:'博士研究生',
		            }
	            ]
	            for (let i = 0; i < res.results.length; ++i) {
	                if (res.results[i].money_name !== null) {
	                	for (let j = 0; j < 3; ++j){
	                		if (res.results[i].stu_type == award_category[j].name){
	                    		award_category[j].value = award_category[j].value + res.results[i].money_sum;	                			
	                		}
	                	}
	                }
	            }
				
				console.log(award_category);
				
				(function(){
						
						var mychart = echarts.init(document.querySelector("#graph2"));
						
						option = {
			
						    title:{
							  left: 'center',
							  top:10,
						    },	
			
						    tooltip: {
						        trigger: 'axis',
						        axisPointer: {            
						            type: 'shadow',   
						            width:"20",
						        }
						    },
			
							toolbox: {
							    show: true,
							    feature: {
							        saveAsImage: {
							        	show: true,
							        	name: year + '年中国矿业大学资助信息分布图2',
							        }
							    }
							},
			
						    tooltip: {
						        trigger: 'item',
						        formatter: '{a} <br/>{b}: {c} ({d}%)'
						    },
						    legend: {
						        bottom: 10,
						        data: ['本科', '硕士研究生', '博士研究生']
						    },
						    series: [
						        {
						            name: '学生类型',
						            type: 'pie',
						            radius: ['30%', '38%'],
						            avoidLabelOverlap: false,
						            label: {
						                show: false,
						                position: 'center'
						            },
						            labelLine: {
						                show: false
						            },
						            data: award_category,
						        }
						    ]
						};
			
						mychart.setOption(option);
						
						 window.addEventListener("resize",function(){
						     mychart.resize();
						 })		
				})();
			}
	    });
}


function get_graph3(date1, date2, location){

	$.ajax({
	        url: '/data.php',
	        data: {
				date1: date1,
				date2: date2,
				location: location,
        	},
	        type: 'get',
	        dataType: "json",
	        success(res) {
	            console.log(res);
				let actionList = [];
				let cntList = [];
	            for (let i = 0; i < res.byCategory.length; ++i) {
	                if (res.byCategory[i].action !== null) {
						actionList.push(res.byCategory[i].action);
						var obj = {
							value:res.byCategory[i].cnt,
							name:res.byCategory[i].action
						};
						cntList.push(obj);
	                }
	            }
	            
				(function(){
						
						var mychart = echarts.init(document.querySelector("#graph3"));
						option = {
							title:{
								left: 'center',
								top:0,
							},
						    toolbox: {
						        show: true,
						        feature: {
						            saveAsImage: {
						            	show: true,
						         		name: location + ': ' + date1 + '-' + date2 + '道路违规信息统计图',
						            }
						        }
						    },
		
						    tooltip: {
						        trigger: 'item',
						        formatter: '{a} <br/>{b} : {c} ({d}%)'
						    },
						    legend: {
						        bottom: '250px',
						        data: actionList
						    },
						    labelLine:{ 
        						show:false,   
    						},
						    series: [
						        {
						            name: '类型占比',
						            type: 'pie',
						            radius: '30%',
						            center: ['50%', '30%'],
						            data: cntList,
						            emphasis: {
						                itemStyle: {
						                    shadowBlur: 10,
						                    shadowOffsetX: 0,
						                    shadowColor: 'rgba(0, 0, 0, 0.5)'
						                }
						            },
						            labelLine:{
						                show:false  
						            },
						            label:{
						                show:false
						            }							            
						        }
						    ]
						};
						mychart.setOption(option);
						 window.addEventListener("resize",function(){
						     mychart.resize();
						 })
				})();
			}
	});
}



// $(function(){
//
// 	get_graph1();
// 	// get_graph2();
// 	get_graph3();
// 	console.log(111111111111);
//
//
// })
