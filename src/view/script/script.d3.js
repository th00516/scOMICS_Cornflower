/*d3*/

$(document).ready(function() {

    $("#d3PlotRegi").html(function() {
        var marge = {top:40, bottom:40, left:40, right:40};
        var dataset = [250, 210, 170, 130, 90];

        var svg = d3.select("svg");
        var G = svg.append("g")
                   .attr("transform", 
                         "translate(" + marge.top + "," + marge.left + ")");
        var rectHeight = 100;

        G.selectAll("rect")
         .data(dataset)
         .enter()
         .append("rect")
         .attr("x", 20)
         .attr("y", function(d, i){
                        return i * rectHeight;
                    })
         .attr("width", function(d){
                            return d;
                        })
    	 .attr("height", rectHeight - 5)
    	 .attr("fill", "blue");
    });

});