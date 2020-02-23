/*boxplot*/

// create dummy data
var data1 = [12, 19, 11, 13, 12, 22, 13, 4, 15, 16, 18, 19, 20, 12, 11, 9],
data2 = [21, 19, 31, 23, 12, 42, 33, 24, 5, 36, 10, 11, 43, 2, 15, 19]

// Compute summary statistics used for the box 1
var data1_sorted = data1.sort(d3.ascending)
var q1_1 = d3.quantile(data1_sorted, 0.25)
var median_1 = d3.quantile(data1_sorted, 0.5)
var q3_1 = d3.quantile(data1_sorted, 0.75)
var interQTR_1 = q3_1 - q1_1
var min_1 = q1_1 - 1.5 * interQTR_1 > 0 ? q1_1 - 1.5 * interQTR_1 : 0
var max_1 = q1_1 + 1.5 * interQTR_1 < 50 ? q1_1 + 1.5 * interQTR_1 : 50

// Compute summary statistics used for the box 2
var data2_sorted = data2.sort(d3.ascending)
var q1_2 = d3.quantile(data2_sorted, 0.25)
var median_2 = d3.quantile(data2_sorted, 0.5)
var q3_2 = d3.quantile(data2_sorted, 0.75)
var interQTR_2 = q3_2 - q1_2
var min_2 = q1_2 - 1.5 * interQTR_2 > 0 ? q1_2 - 1.5 * interQTR_2 : 0
var max_2 = q1_2 + 1.5 * interQTR_2 < 50 ? q1_2 + 1.5 * interQTR_2 : 50 

// set the dimensions and margins of the graph
var margin = {top: 40, right: 40, bottom: 40, left: 40},
width = 600 - margin.left - margin.right,
height = 600 - margin.top - margin.bottom

$(document).ready(function() {

    // append the svg object to the body of the page
    var svg = d3.select("#d3PlotRegi")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

    // Show the X & Y scale
    var x = d3.scaleLinear()
        .domain([0, 3])
        .range([0, width])

    var y = d3.scaleLinear()
        .domain([0, 50])
        .range([height, 0])

    // svg.call(d3.axisBottom(x))
    svg.call(d3.axisLeft(y))

    // a few features for the box
    var box_width = 50

    // Show the main vertical line 1
    svg
        .append("line")
        .attr("x1", x(1))
        .attr("x2", x(1))
        .attr("y1", y(min_1))
        .attr("y2", y(max_1))
        .attr("stroke", "black")
        .attr("stroke-width", "2px")

    // Show the main vertical line 2
    svg
        .append("line")
        .attr("x1", x(2))
        .attr("x2", x(2))
        .attr("y1", y(min_2))
        .attr("y2", y(max_2))
        .attr("stroke", "black")
        .attr("stroke-width", "2px")

    // Show the box 1
    svg
        .append("rect")
        .attr("x", x(1) - box_width / 2)
        .attr("y", y(q3_1))
        .attr("height", (y(q1_1) - y(q3_1)))
        .attr("width", box_width)
        .style("fill", "red")
        .attr("stroke", "black")
        .attr("stroke-width", "2px")

    // Show the box 2
    svg
        .append("rect")
        .attr("x", x(2) - box_width / 2)
        .attr("y", y(q3_2))
        .attr("height", (y(q1_2) - y(q3_2)))
        .attr("width", box_width)
        .style("fill", "blue")
        .attr("stroke", "black")
        .attr("stroke-width", "2px")

    // show median, min and max horizontal lines
    svg
        .select("xx")
        .data([min_1, median_1, max_1])
        .append("line")
        .attr("x1", x(1) - box_width / 2)
        .attr("x2", x(1) + box_width / 2)
        .attr("y1", d => y(d))
        .attr("y2", d => y(d))
        .attr("stroke", "black")
        .attr("stroke-width", "2px")

    svg
        .select("xx")
        .data([min_2, median_2, max_2])
        .append("line")
        .attr("x1", x(2) - box_width / 2)
        .attr("x2", x(2) + box_width / 2)
        .attr("y1", d => y(d))
        .attr("y2", d => y(d))
        .attr("stroke", "black")
        .attr("stroke-width", "2px")

});