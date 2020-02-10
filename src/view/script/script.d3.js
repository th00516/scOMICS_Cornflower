var width = 250;
var height = 250;

var svg = d3.select("body").append("svg")
            .attr("width", width)
            .attr("height", height);

var dataset = [ 30 , 20 , 45 , 12 , 21 ];

svg.selectAll("rect").data(dataset).enter().append("rect")
   .attr("x", 10)
   .attr("y", function(d, i){return i * 30;})
   .attr("width", function(d, i){return d * 10;})
   .attr("height", 28)
   .attr("fill", "green");