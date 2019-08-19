var chart
var chart1
var draw = new Vue
(
	{
		el: '#vue_0',
		data:
		{
			uid:'1503345074',
			test:'',
			is_word:false,
			is_recommend:false,
			refile:'reco.json',
		},
		methods:
		{
			 draw_year: function () {		
				  document.getElementById('main').style.visibility="hidden";			 
				  $.getJSON('data/'+draw.uid+'/year.json',function(data)
				  {
					var sum=0
					for (var i = 0; i < data.length; i++) {sum+=data[i].count}
					if (chart!=null)chart.destroy();
					chart=new G2.Chart({
						container: "mountNode",
						forceFit: true,
						height: 700,
						padding: [20, 100, 50, 50]
						});
				  chart.source(data, {
					percent: {
					  formatter: function formatter(val) {
						val = val * 100 + '%';
						return val;
					  }
					}
				  });
				  chart.coord('theta', {
					radius: 0.75,
					innerRadius: 0.6
				  });
				  chart.tooltip({
					showTitle: false,
					itemTpl: '<li><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}: {value}</li>'
				  });
				  // 辅助文本
				  chart.guide().html({
					position: ['50%', '50%'],
					html: '<div style="color:#8c8c8c;font-size: 20px;text-align: center;width: 10em;">'+sum+'条<br><span style="color:#8c8c8c;font-size:20px;width: 10em;">说说</span></div>',
					alignX: 'middle',
					alignY: 'middle'
				  });
				  var interval = chart.intervalStack().position('count').color('year').label('count', {
					formatter: function formatter(count, year) {
					  return year.point.year + ': ' + count;
					}
				  }).tooltip('year*count', function(year,count) {
				  
					percent = count / sum * 100
					percent=percent.toFixed(2)
					percent=percent + '%';
					return {
					  name: year,
					  value: percent
					};
				  }).style({
					lineWidth: 1,
					stroke: '#fff'
				  });
				  chart.render();
				  interval.setSelected(data[0]);
				  });
				  if (draw.is_recommend)
				  {
					   $.getJSON('reco/'+this.refile,function(d)
					   {  
							$.getJSON('data/'+d[draw.uid]+'/year.json',function(data)
							{
							   var sum=0
							   for (var i = 0; i < data.length; i++) {
								  sum+=data[i].count
							   }							
							   if (chart1!=null) chart1.destroy();
							   chart1=new G2.Chart({
								container: "mountNode1",
								forceFit: true,
								height: 700,
								padding: [20, 100, 50, 50]
								});
							   chart1.source(data, {
								percent: {
								  formatter: function formatter(val) {
									val = val * 100 + '%';
									return val;
								  }
								}
							  });
							  chart1.coord('theta', {
								radius: 0.75,
								innerRadius: 0.6
							  });
							  chart1.tooltip({
								showTitle: false,
								itemTpl: '<li><span style="background-color:{color};" class="g2-tooltip-marker"></span>{name}: {value}</li>'
							  });
							  chart1.guide().html({
								position: ['50%', '50%'],
								html: '<div style="color:#8c8c8c;font-size: 20px;text-align: center;width: 10em;">'+d[draw.uid]+'<br>'+sum+'条<br><span style="color:#8c8c8c;font-size:20px;width: 10em;">说说</span></div>',
								alignX: 'middle',
								alignY: 'middle'
							  });
							  var interval = chart1.intervalStack().position('count').color('year').label('count', {
								formatter: function formatter(count, year) {
								  return year.point.year + ': ' + count;
								}
							  }).tooltip('year*count', function(year,count) {
							  
								percent = count / sum * 100
								percent=percent.toFixed(2)
								percent=percent + '%';
								return {
								  name: year,
								  value: percent
								};
							  }).style({
								lineWidth: 1,
								stroke: '#fff'
							  });
							  chart1.render();
							  interval.setSelected(data[0]);
							});
						})
					}
			 },
			 draw_month: function() {
				 document.getElementById('main').style.visibility="hidden";
				  $.getJSON('data/'+draw.uid+'/month.json'+"?timestamp=" + new Date().getTime(),function(data) {
					if (chart!=null)
						chart.destroy();
						chart = new G2.Chart({
						container: "mountNode",
						forceFit: true,
						height: 700,
					  });
					  chart.source(data);
					  chart.scale('time', {
						tickCount: data.length/12+1
						})
					chart.axis('time', {
					label: {
					  textStyle: {
						fill: '#aaaaaa'
					  },
					  formatter: function formatter(text) {
						return text.substr(0,4)
					  }
					},
					title: {
					  offset: 80
					}
				  }); 
					  chart.interval().position('time*count');
					  chart.render();	
				 })
				 if (draw.is_recommend)
				 {
					  $.getJSON('reco/'+this.refile,function(da) {
						$.getJSON('data/'+da[draw.uid]+'/month.json',function(data) {
						if (chart1!=null)
							chart1.destroy();
						  chart1 = new G2.Chart({
							container: "mountNode1",
							forceFit: true,
							height: 700,
						  });
						  chart1.source(data);
						  chart1.scale('time', {
							tickCount: data.length/12+1
							})
						chart1.axis('time', {
						label: {
						  textStyle: {
							fill: '#aaaaaa'
						  },
						  formatter: function formatter(text) {
						   return text.substr(0,4)
						  }
						},
						title: {
						  offset: 80
						}
					  }); 
						  chart1.interval().position('time*count');
						  chart1.render();	
						})
					 })
				 }
			},
			 draw_day: function() {
				 	document.getElementById('main').style.visibility="hidden";
				    $.getJSON('data/'+draw.uid+'/day.json',function(data){
					if (chart!=null)
						chart.destroy();
						chart = new G2.Chart({
						container: 'mountNode',
						forceFit: true,
						height: 700,
					  });
					  chart.source(data);
					  chart.scale('day', {
						tickInterval: 1
					  });
					  chart.interval().position('day*count');
					  chart.render();
					});
					 if (draw.is_recommend)
					 {
						  $.getJSON('reco/'+this.refile,function(da) {
							$.getJSON('data/'+da[draw.uid]+'/day.json',function(data){
							if (chart1!=null)
								chart1.destroy();
								chart1 = new G2.Chart({
								container: 'mountNode1',
								forceFit: true,
								height: 700,
							  });
							  chart1.source(data);
							  chart1.scale('day', {
								tickInterval: 1
							  });
							  chart1.interval().position('day*count');
							  chart1.render();
							});
						 })
					 }
			 },
			 draw_hour: function() {
				 	document.getElementById('main').style.visibility="hidden";
				    $.getJSON('data/'+draw.uid+'/hour.json',function(data){
					if (chart!=null)
						chart.destroy();
					chart = new G2.Chart({
						container: 'mountNode',
						forceFit: true,
						height: 700,
					  });
					  chart.source(data);
					  chart.scale('hour', {
						tickInterval: 1
					  });
					  chart.interval().position('hour*count');
					  chart.render();
					});
					if (draw.is_recommend)
					 {
						  $.getJSON('reco/'+this.refile,function(da) {
							 $.getJSON('data/'+da[draw.uid]+'/hour.json',function(data){
								if (chart1!=null)
									chart1.destroy();
									chart1 = new G2.Chart({
									container: 'mountNode1',
									forceFit: true,
									height: 700,
								  });
									chart1.source(data);
								    chart1.scale('hour', {
									tickInterval: 1
								  });
								  chart1.interval().position('hour*count');
								  chart1.render();
								});
						 })
					 }
			 },
			 draw_word: function() 
			 {
				 	document.getElementById('main').style.visibility="visible";
					if (chart!=null)
						chart.destroy();
						chart = new G2.Chart({
						container: 'mountNode',
						forceFit: true,
						height: 0,
					  });	
					  if (chart1!=null)
						chart1.destroy();
						chart1 = new G2.Chart({
						container: 'mountNode',
						forceFit: true,
						height: 0,
					  });	
				require.config({
					paths: {
						echarts: 'http://echarts.baidu.com/build/dist'
					}
				});
				require(
					[
						'echarts',
						'echarts/chart/wordCloud' // 使用柱状图就加载bar模块，按需加载
					],
					function (ec) 
					{
						// 基于准备好的dom，初始化echarts图表
						var id=draw.uid
						
						if (draw.is_recommend) id=draw.test
						$.getJSON('data/'+id+'/word.json',function(d)
						{
							var container=document.getElementById('main')
							var scale=0.8
							container.style.width = window.innerWidth*scale+'px'; 
							container.style.height = window.innerHeight*scale+'px';
							var myChart = ec.init(container); 
							function createRandomItemStyle() {
								return {
									normal: {
										color: 'rgb(' + [
											Math.round(Math.random() * 160),
											Math.round(Math.random() * 160),
											Math.round(Math.random() * 160)
										].join(',') + ')'
									}
								};
							}
							option = {
								title: {
									//text: id,
									//y:'center',
								},
								tooltip: {
									show: true
								}
							}
							var s=[{
								name: 'mood detail',
								type: 'wordCloud',
								//gridSize: 10,
								size: ['80%', '80%'],
								textRotation : [0, 45, 90, -45],
								textPadding: 0,
								autoSize: {
									enable: true,
									minSize: 24
								}
							}]
							for (var i=0;i<d.length;i++)
								d[i]['itemStyle']=createRandomItemStyle()
							s[0]['data']=d
							option['series']=s
							myChart.setOption(option);
							window.onresize = myChart.resize
						})						
					}				
				)
			 },
			 recommend_time: function()
			 {
		     	this.refile='reco_time.json'
				this.recommend()
			 },
			 recommend_word: function()
			 {
				 this.refile='reco_word.json'
				 this.recommend()
			 },
			 recommend_all: function()
			 {
				 this.refile='reco.json'
				 this.recommend()
			 },
			 recommend: function()
			 {
				$.getJSON('reco/'+this.refile,function(da) {
					draw.test=da[draw.uid]
				if (!draw.is_recommend)
				{
					draw.is_recommend=true
					document.getElementById('frame1').classList.remove("col-lg-10")
					document.getElementById('frame1').classList.add("col-lg-4")
					document.getElementById('frame2').classList.add("col-lg-4")
					document.getElementById('frame2').classList.add("ml-sm-auto")
				}
				draw.draw_year()
				})
			 },
			 reset: function()
			 {
				if (draw.is_recommend)
				{
					draw.is_recommend=false
					document.getElementById('frame1').classList.remove("col-lg-4")
					document.getElementById('frame1').classList.add("col-lg-10")
					document.getElementById('frame2').classList.remove("col-lg-4")
					document.getElementById('frame2').classList.remove("ml-sm-auto")
				}
    			draw.draw_year()
			 }
		},
		watch:{
			'uid':function(newVal){
				this.reset()
				if (chart)
					chart.destroy();
				chart = new G2.Chart({
						container: 'mountNode',
						forceFit: true,
						height: 700,
					  });
				this.draw_year()
			}
		}
	}
)

draw.draw_year()