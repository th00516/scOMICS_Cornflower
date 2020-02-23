/*boxplot*/

$(document).ready(function() {

    // set the dimensions and margins of the graph
    var margin = {top: 40, right: 40, bottom: 40, left: 40},
    width = 600 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom

    // append the svg object to the body of the page
    var svg = d3.select("#d3PlotRegi")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

    // Show the X & Y scale and a few features for the box
    var scale_x = d3.scaleLinear()
        .domain([0, 3])
        .range([0, width])

    var scale_y = d3.scaleLinear()
        .domain([0, 50])
        .range([height, 0])

    svg.call(d3.axisLeft(scale_y))

    var col_list = ['red', 'blue']
    var box_width = 50

    // create dummy data
    var raw_data = new Array([12, 19, 11, 13, 12, 22, 13, 4, 15, 16, 18, 19, 20, 12, 11, 9],
                             [21, 19, 31, 23, 12, 42, 33, 24, 5, 36, 10, 11, 43, 2, 15, 19])

    var data = new Array()

    for (i of [0, 1]) {
        // Compute summary statistics used for the box
        data[i] = new Object()

        data[i].Data = raw_data[i].sort(d3.ascending)
        data[i].Q1 = d3.quantile(data[i].Data, 0.25)
        data[i].Median = d3.quantile(data[i].Data, 0.5)
        data[i].Q3 = d3.quantile(data[i].Data, 0.75)
        data[i].InterQTR = data[i].Q3 - data[i].Q1
        data[i].Min = data[i].Q3 - 1.5 * data[i].InterQTR > 0  ? data[i].Q3 - 1.5 * data[i].InterQTR : 0
        data[i].Max = data[i].Q1 + 1.5 * data[i].InterQTR < 50 ? data[i].Q1 + 1.5 * data[i].InterQTR : 50

        // Show the main vertical line
        svg
            .append("line")
            .attr("x1", scale_x(i + 1))
            .attr("x2", scale_x(i + 1))
            .attr("y1", scale_y(data[i].Min))
            .attr("y2", scale_y(data[i].Max))
            .attr("stroke", "black")
            .attr("stroke-width", "2px")

        // Show the box
        svg
            .append("rect")
            .attr("x", scale_x(i + 1) - box_width / 2)
            .attr("y", scale_y(data[i].Q3))
            .attr("height", (scale_y(data[i].Q1) - scale_y(data[i].Q3)))
            .attr("width", box_width)
            .style("fill", col_list[i])
            .attr("stroke", "black")
            .attr("stroke-width", "2px")

        // show median, min and max horizontal lines
        svg
            .selectAll("NONE")
            .data([data[i].Min, data[i].Median, data[i].Max])
            .enter()
            .append("line")
            .attr("x1", scale_x(i + 1) - box_width / 2)
            .attr("x2", scale_x(i + 1) + box_width / 2)
            .attr("y1", d => scale_y(d))
            .attr("y2", d => scale_y(d))
            .attr("stroke", "black")
            .attr("stroke-width", "2px")
    }

});