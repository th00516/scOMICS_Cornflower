/*d3*/

// Set the dimensions, margins and scales of the graph
var margin = { top: 40, right: 40, bottom: 40, left: 40 },
    width = 710 - margin.left - margin.right,
    height = 660 - margin.top - margin.bottom

d3.select("#toolbox").select("#exp").on("click", function () {
    // Clean svg
    d3.select("#plotRegi").select("#Scatter").remove()
    d3.select("#plotRegi").select("#Box").remove()

    // Create dummy data
    var raw_data = new Array([12, 19, 11, 13, 12, 22, 13, 4, 15, 16, 18, 19, 20, 12, 11, 9],
        [21, 19, 31, 23, 12, 42, 33, 24, 5, 36, 10, 11, 43, 2, 15, 19],
        [33, 12, 42, 33, 24, 5, 36, 10, 11, 13, 12, 22, 13, 4, 15, 16])

    // Set a few features for the data
    var box_num = raw_data.length

    // Set the scales of the graph
    var scale_x = d3
        .scaleLinear()
        .domain([0, box_num + 1])
        .range([0, width])

    var scale_y = d3
        .scaleLinear()
        .domain([-10, 90])
        .range([height, 0])

    // Set a few features for the graph
    var box_width = 50

    // Append the svg object to the body of the page
    var svg = d3
        .select("#plotRegi")
        .append("svg")
        .attr("id", "Box")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)

    // Append a canvas for the following drawing
    svg
        .append("g")
        .attr("id", "Canvas")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

    // Append the X & Y Axis
    svg
        .select("#Canvas")
        .append("g")
        .attr("id", "AxisX")
        .call(d3.axisBottom(scale_x).ticks(3))
        .attr("transform", "translate(0," + height + ")")

    svg
        .select("#Canvas")
        .append("g")
        .attr("id", "AxisY")
        .call(d3.axisLeft(scale_y).ticks(10))

    // Set colors
    var col_list = ["red", "blue", "green"]

    // Drawing
    var data = new Array()

    for (i = 0; i < box_num; i++) {
        // Compute summary statistics used for the box
        data[i] = new Object()

        data[i].Data = raw_data[i].sort(d3.ascending)
        data[i].Q1 = d3.quantile(data[i].Data, 0.25)
        data[i].Median = d3.quantile(data[i].Data, 0.5)
        data[i].Q3 = d3.quantile(data[i].Data, 0.75)
        data[i].InterQTR = data[i].Q3 - data[i].Q1
        data[i].Min = data[i].Q1 - 1.5 * data[i].InterQTR > 0 ? data[i].Q1 - 1.5 * data[i].InterQTR : 0
        data[i].Max = data[i].Q3 + 1.5 * data[i].InterQTR < 50 ? data[i].Q3 + 1.5 * data[i].InterQTR : 50

        svg
            .select("#Canvas")
            .append("g")
            .attr("id", "box_" + (i + 1))

        // Append the main vertical line
        svg
            .select("#box_" + (i + 1))
            .append("line")
            .attr("x1", scale_x(i + 1))
            .attr("y1", scale_y(data[i].Max))
            .attr("x2", scale_x(i + 1))
            .attr("y2", scale_y(data[i].Min))
            .style("stroke", col_list[i])
            .style("stroke-width", "2px")

        // Append the box
        svg
            .select("#box_" + (i + 1))
            .append("rect")
            .attr("x", scale_x(i + 1) - box_width / 2)
            .attr("y", scale_y(data[i].Q3))
            .attr("width", box_width)
            .attr("height", (scale_y(data[i].Q1) - scale_y(data[i].Q3)))
            .style("fill", "white")
            .style("stroke", col_list[i])
            .style("stroke-width", "2px")

        // Append median, min and max horizontal lines
        svg
            .select("#box_" + (i + 1))
            .selectAll("NONE")
            .data([data[i].Min, data[i].Median, data[i].Max], d => d)
            .enter()
            .append("line")
            .attr("x1", scale_x(i + 1) - box_width / 2)
            .attr("y1", d => scale_y(d))
            .attr("x2", scale_x(i + 1) + box_width / 2)
            .attr("y2", d => scale_y(d))
            .style("stroke", col_list[i])
            .style("stroke-width", "2px")

        // Append the option box
        svg
            .select("#box_" + (i + 1))
            .append("rect")
            .attr("id", "opt")
            .attr("x", scale_x(i + 1) - box_width / 2 - 10)
            .attr("y", scale_y(data[i].Max) - 10)
            .attr("width", box_width + 20)
            .attr("height", (scale_y(data[i].Min) - scale_y(data[i].Max)) + 20)
            .style("fill", "grey")
            .style("opacity", 0)

            .on("mouseover", function () {
                if (d3.select(this).style("opacity") == 0) {
                    d3.select(this).style("opacity", 0.3)
                }
            })

            .on("mouseout", function () {
                if (d3.select(this).style("opacity") == 0.3) {
                    d3.select(this).style("opacity", 0)
                }
            })

            .on("click", function () {
                if (d3.select(this).style("opacity") != 0.5) {
                    d3.select(this).style("opacity", 0.5)
                } else {
                    d3.select(this).style("opacity", 0.3)
                }
            })
    }
})