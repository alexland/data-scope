
$(function() {

	var xStart = Date.UTC(2012, 0, 01);
	var xStep = 60 * 60 * 1000; 		// hours

	$("#slider1").rangeinput({		
		progress: true,
		value: 1,
		min: 0,
		max: 10,
		step: 0.2,
		keyboard: true,
	});		

	$("#slider2").rangeinput({		
		progress: true,
		value: 1,
		min: 0,
		max: 10,
		step: 0.2,
		keyboard: true,
	});		

	var chart;
	var options = {
		dateFormat: "%d%b%y",
		chart: {
			renderTo: 'plotContainer',
			zoomType: 'x',
			events: {
				load: function(event) {
					getdata(this);
				}
			} 
		},
		colors: ['#A763A7', '#E58742', '#59785C', '#7BA788', '#65BAC3'],
		plotOptions: {
            line: {
				pointInterval: xStep,
				pointStart: xStart,
				lineWidth: 1,
                marker: {
                    enabled: false,
                    states: {
                        hover: {
                            enabled: true,
                            radius: 5
                        }
                    }
                },
                shadow: false,
                states: {
                    hover: {
                        lineWidth: 1                        
                    }
                }
            },
        },
		tooltip: {
			backgroundColor: '#8C92AC',
			borderColor: '#8C92AC',
			borderWiddth: 0,
			formatter: function() {
				return  ''+ Highcharts.dateFormat("%d%b%y", this.x)+': '+ Highcharts.numberFormat(this.y, 2, '.');
			}
		},
        title: {
        	text: ''
        },
		xAxis: {
			type: 'datetime',
			dateTimeLabelFormats: {
				day: '%e%b%y'
			},
			gridLineColor: '#5D8AA8',
			gridLineWidth: 0.7,
		},
		yAxis: {
			min: 0,
			max: 9,
			title: {
				text: '',
				gridLineColor: '#5D8AA8',
				gridLineWidth: 0.7,
			}
		},   
		series: [
			{
				name: 'ds1',
				color: '#004225',
				data: []
			}
		],
		legend: {
            enabled: false
        },
        credits: {
            enabled: false
        }
	};
	
	chart = new Highcharts.Chart(options);

	function getdata(chart) {
			$.getJSON( $SCRIPT_ROOT + '/_fromDB0', 
				function(data) {
					chart.series[0].setData(data.result);
		    	}
			)
	};

	$('#plot1').bind('click', function() {
		$.getJSON($SCRIPT_ROOT + '/_fromDB01', 
			function(data) {
				chart.series[0].setData(data.result);
			}
		)
	});

	$('#plot2').bind('click', function() {
		$.getJSON($SCRIPT_ROOT + '/_fromDB02', 
			function(data) {
				chart.series[0].setData(data.result);	
			}
		)
	});

	$("input:checkbox[name=addSeries]").attr("checked", false);

	$("input:checkbox[name=addSeries][value=g1]").click(function() {
		if (this.checked) {
			$.getJSON($SCRIPT_ROOT + '/_fromDB04a',
				function(data) {
					chart.addSeries({
						data: data.result,
						name: 'g1',
						id: 'id_g1',
						pointInterval: xStep,
						pointStart: xStart
					})
			});
		}
		else {
			chart.get('id_g1').remove();
		}
	});

	$("input:checkbox[name=addSeries][value=g2]").click(function() {
		if (this.checked) {
			$.getJSON($SCRIPT_ROOT + '/_fromDB04b',
				function(data) {
					chart.addSeries({
						data: data.result,
						name: 'g2',
						id: 'id_g2',
						pointInterval: xStep,
						pointStart: xStart
					})
			});
		}
		else {
			chart.get('id_g2').remove();
		}
	});

	$("input:checkbox[name=addSeries][value=g3]").click(function() {
		if (this.checked) {
			$.getJSON($SCRIPT_ROOT + '/_fromDB04c',
				function(data) {
					chart.addSeries({
						data: data.result,
						name: 'g3',
						id: 'id_g3',
						pointInterval: xStep,
						pointStart: xStart
					})
			});
		}
		else {
			chart.get('id_g3').remove();
		}
	});

	$("input:checkbox[name=addSeries][value=g4]").click(function() {
		if (this.checked) {
			$.getJSON($SCRIPT_ROOT + '/_fromDB04d',
				function(data) {
					chart.addSeries({
						data: data.result,
						name: 'g4',
						id: 'id_g4',
						pointInterval: xStep,
						pointStart: xStart
					})
			});
		}
		else {
			chart.get('id_g4').remove();
		}
	});

	$("input:radio[name=rollup]").attr("checked", false);
	$("input:radio[name=rollup][value=days]").attr("checked", true);

	$("input[name=rollup]").click(function() {

		var rbSelected = $('input[name="rollup"]:checked').val();
	
		switch (rbSelected) {

			case "days":
				$.getJSON( $SCRIPT_ROOT + '/_fromDB0', 
					function(data) {
						chart.series[0].setData(data.result);
		    		}
				);
				break;
				
			case "weeks":
				$.getJSON( $SCRIPT_ROOT + '/_fromDB0', 
					function(data) {
						d = data.result;
						d1 = d.map(function(x) {
							return x + 1;
						});
						chart.series[0].setData(d1);
		    		}
				);	
				break;

			case "months":
				$.getJSON( $SCRIPT_ROOT + '/_fromDB0', 
					function(data) {
						d = data.result;
						d1 = d.map(function(x) {
							return x + 2;
						});
						chart.series[0].setData(d1);
		    		}
				);	
				break;

			case "years":
				$.getJSON( $SCRIPT_ROOT + '/_fromDB0', 
					function(data) {
						d = data.result;
						d1 = d.map(function(x) {
							return x + 3;
						});
						chart.series[0].setData(d1);
		    		}
				);	
				break;
		}
	});
});
