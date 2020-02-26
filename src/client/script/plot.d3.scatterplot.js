/*d3*/

$(document).ready(function () {

    // Set random colors
    function get_random_color(n) {
        R = new Set()
        G = new Set()
        B = new Set()

        while (R.size < n) {R.add(Math.ceil(Math.random() * 255))}
        while (G.size < n) {G.add(Math.ceil(Math.random() * 255))}
        while (B.size < n) {B.add(Math.ceil(Math.random() * 255))}

        return [Array.from(R), Array.from(G), Array.from(B)]
    }

    // Set a container for recoding selected clusters
    function selected_clusters() {
        this.selected = new Set()

        this.add = function(_cluster) {this.selected.add(_cluster)}
        this.del = function(_cluster) {this.selected.delete(_cluster)}
    }

    // Set a tooltip
    var tooltip = d3
        .select("#plotRegi")
        .append("div")
        .attr("id", "tooltip")
        .style("display", "none")
        .style("position", "absolute")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("background-color", "white")

    // Draw scatter plot
    function scatterPlot(dat) {
        // Set the width & height of the graph
        var margin = {top: 40, right: 40, bottom: 40, left: 40},
            width = 650 - margin.left - margin.right,
            height = 650 - margin.top - margin.bottom

        // Set the scales of the graph
        var scale_x = d3
            .scaleLinear()
            .domain([-50, 50])
            .range([0, width])

        var scale_y = d3
            .scaleLinear()
            .domain([-50, 50])
            .range([height, 0])

        // Append the svg object and a canvas for the following drawing
        var svg = d3
            .select("#plotRegi")
            .append("svg")
            .attr("id", "Scatter")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)

        svg
            .append("g")
            .attr("id", "Canvas")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

        // Append the X & Y Axis
        svg
            .select("#Canvas")
            .append("g")
            .attr("id", "AxisX")
            .call(d3.axisBottom(scale_x).ticks(10))
            .attr("transform", "translate(0," + height + ")")

        svg
            .select("#Canvas")
            .append("g")
            .attr("id", "AxisY")
            .call(d3.axisLeft(scale_y).ticks(10))

        var color_list = get_random_color(30)

        // Drawing
        svg
            .select("#Canvas")
            .append("g")
            .attr("id", "scatterplot")

        var choosed = new selected_clusters()

        svg
            .select("#scatterplot")
            .selectAll("NONE")
            .data(dat.slice(0, 30000), d => d)
            .enter()
            .append("circle")
            .attr("class", d => "cluster_" + d.seurat_clusters)
            .attr("cx", d => scale_x(d.TSNE_1))
            .attr("cy", d => scale_y(d.TSNE_2))
            .attr("r", 2)
            .style("fill", d => "rgb(" + [color_list[0][d.seurat_clusters],
                                          color_list[1][d.seurat_clusters],
                                          color_list[2][d.seurat_clusters]] + ")")
            .style("opacity", 0.1)

            .on("mouseover", function() {
                tooltip
                    .style("display", "inline")
                    .style("left", (d3.mouse(this)[0] + d3.select("body").style("width") * 0.2 + width) + "px")
                    .style("top", (d3.mouse(this)[1] + d3.select("body").style("height") + height) + "px")
                    .text(d3.select(this).attr("class"))
            })

            .on("mouseout", function() {
                tooltip
                    .style("display", "none")
            })

            .on("click", function() {
                if (d3.select(this).style("opacity") == 0.1) {
                    d3
                        .selectAll("." + (d3.select(this).attr("class")))
                        .transition()
                        .duration(400)
                        .style("opacity", d3.select(this).style("opacity") * 10)

                    choosed.add(d3.select(this).attr("class"))
                } else {
                    d3
                        .selectAll("." + (d3.select(this).attr("class")))
                        .transition()
                        .duration(400)
                        .style("opacity", d3.select(this).style("opacity") / 10)

                    choosed.del(d3.select(this).attr("class"))
                }
            })
    }


    // Main
    d3.select("#Scatterplot_triger").on("click", function() {
        // Clean svg
        d3.select("#plotRegi").select("#Scatter").remove()
        d3.select("#plotRegi").select("#Box").remove()

        // Create dummy data
        d3.tsv("../demo_data/pbmc.tsv").then(d => scatterPlot(d))
    })

})