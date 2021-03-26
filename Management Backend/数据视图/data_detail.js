function get_graph1(year = 2019){

	$.ajax({
	        url: 'http://188.131.157.8:8000/graphic_data_award/',  
	        data: {
            	money_year: year
        	},
	        type: 'get',
	        dataType: "json",
	        success(res) {
	            console.log(res);
	            let award_name = [];
	            let award_data = [];
	            for (let i = 0; i < res.results.length; ++i) {
	                if (res.results[i].money_name !== null) {
	                    award_name.push(res.results[i].money_name);
	                    award_data.push(res.results[i].money_sum);
	                }
	            }

				(function(){
						
						var mychart = echarts.init(document.querySelector(".graph1"));
						
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
				//		        containLabel: true
						    },
						    toolbox:{
						      feature:{
						          saveAsImage:{
						          	show:true,
						          	name: year + '年中国矿业大学资助信息分布图1',
						          },
						      }  
						    },
						    xAxis: [
						        {
						            type: 'category',
						            data: award_name,
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
						            name: '资助费用',
						            type: 'bar',
						            barWidth: '30',
						            data: award_data,
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

				console.log(award_name);
	            console.log(award_data);
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
						
						var mychart = echarts.init(document.querySelector(".graph2"));
						
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
						            radius: ['50%', '70%'],
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


function get_graph3(year = 2019){

	$.ajax({
	        url: 'http://188.131.157.8:8000/graphic_data_college/',  
	        data: {
            	money_year: year
        	},
	        type: 'get',
	        dataType: "json",
	        success(res) {
	            console.log(res);
				let college = [];
				let college_name = [];
	            for (let i = 0; i < res.results.length; ++i) {
	                if (res.results[i].money_name !== null) {
						college_name.push(res.results[i].stu_college);
						var col_obj = {
							value:res.results[i].money_sum,
							name:res.results[i].stu_college
						};
						college.push(col_obj);
	                }
	            }
	            
				(function(){
						
						var mychart = echarts.init(document.querySelector(".graph3"));
						
						option = {
							
							title:{
								left: 'center',
								top:10,
							},
		
						    toolbox: {
						        show: true,
						        feature: {
						            saveAsImage: {
						            	show: true,
						         		name: year + '年中国矿业大学资助信息分布图3',   	
						            }
						        }
						    },
		
						    tooltip: {
						        trigger: 'item',
						        formatter: '{a} <br/>{b} : {c} ({d}%)'
						    },
						    legend: {
						        bottom: '10',
						        data: college_name
						    },
						    labelLine:{ 
        						show:false,   
    						},
						    series: [
						        {
						            name: '学院占比',
						            type: 'pie',
						            radius: '70%',
						            center: ['50%', '50%'],
						            data: college,
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



$(function(){
	
	get_graph1();
	get_graph2();
	get_graph3();
	
	
	$('.content .title a').click(function(){
		
		let info = $(this).attr('data-index');
		
		let split_info = info.split('-');
		console.log(info.split('-'));
		if (split_info[0] == 1)
			get_graph1(split_info[1]);

		if (split_info[0] == 2)
			get_graph2(split_info[1]);
		
		if (split_info[0] == 3)
			get_graph3(split_info[1]);		
		
	})
	
	
})
