Highcharts.setOptions({
    global: {
        useUTC: false
    }
});
jQuery(document).ready(function ($) {
	$('.toggleswitch').toggleSwitch({
            onChangeOn: function () {
		$.post( "http://valve.tinypipes.net/demoControl/", {"enabled":"true" } );		
            },
            onChangeOff: function () {
		$.post( "http://valve.tinypipes.net/demoControl/", {"enabled":"false" } );			
            }
	});
    });


      var chart; // global
      
      /**
       * Request data from the server, add it to the graph and set a timeout to request again
       */
      function requestData() {
      $.ajax({
      url: 'http://valve.tinypipes.net/data-energy/', 
      success: function(point) {
      var series = chart.series[0],
      shift = series.data.length > 50; // shift if the series is longer than 20
      points=eval(point);
      for(var i=0;i<points.length;i++)
		  {
		      var timeStamp=points[i][0];
		      var duplicate=false;
		      for(var j=0;j<series.data.length;j++)
		      {
			  if(series.data[j].x==timeStamp)
			      duplicate=true;
		      }
		      if(!duplicate)
		      {
			  
			  chart.series[0].addPoint(points[i], true, shift);
			  console.log("added new data: "+ points[i]);
			  console.log(series.data);
		      }
		  }

      // call it again after one second
      setTimeout(requestData, 1000);
      },
	  error: function (ajaxContext){
	      requestData();
	  },
      cache: false
      });
      }
      
      $(document).ready(function() {
      chart = new Highcharts.Chart({
      chart: {
      renderTo: 'container',
      defaultSeriesType: 'spline',
      events: {
      load: requestData
      }
      },
      title: {
      text: 'Live tinyPipes Data:  Energy Generated by Demo Panel'
      },
      xAxis: {
      type: 'datetime',
dateTimeLabelFormats: { //force all formats to be hour:minute:second
            second: '%H:%M:%S',
            minute: '%H:%M:%S',
            hour: '%H:%M:%S',
            day: '%H:%M:%S',
            week: '%H:%M:%S',
            month: '%H:%M:%S',
            year: '%H:%M:%S'
        },
tickPixelInterval: 150,
      },
      yAxis: {
      minPadding: 0.2,
      maxPadding: 0.2,
      title: {
      text: 'Power Generation (W)',
      margin: 80
      }
      },
        plotOptions: {
            series: {
                marker: {
                    enabled: true
                }
            }
        },
        
      series: [{
      name: 'panel power generation',
      data: []
      }]
      });
      });
