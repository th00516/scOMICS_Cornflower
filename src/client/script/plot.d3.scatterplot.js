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

    // Draw scatter plot
    function scatterPlot(dat) {
        var margin = { top: 40, right: 40, bottom: 40, left: 40 },
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

        // Append the svg object to the body of the page
        var svg = d3
            .select("#plotRegi")
            .append("svg")
            .attr("id", "Scatter")
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
            .attr("id", "scatter")

        svg
            .select("#scatter")
            .selectAll("NONE")
            .data(dat.slice(0, 10000), d => d)
            .enter()
            .append("circle")
            .attr("class", d => "cluster_" + d.seurat_clusters)
            .attr("cx", d => scale_x(d.TSNE_1))
            .attr("cy", d => scale_y(d.TSNE_2))
            .attr("r", 4)
            .style("fill", d => "rgb(" + [color_list[0][d.seurat_clusters],
                                          color_list[1][d.seurat_clusters],
                                          color_list[2][d.seurat_clusters]] + ")")
            .style("opacity", 0.05)

            .on("click", function() {
                if (d3.select(this).style("opacity") == 0.05) {
                    d3
                        .selectAll("." + (d3.select(this).attr("class")))
                        .transition()
                        .duration(300)
                        .style("opacity", 0.5)
                } else {
                    d3
                        .selectAll("." + (d3.select(this).attr("class")))
                        .transition()
                        .duration(300)
                        .style("opacity", 0.05)
                }
            })
    }

    // Main
    d3.select("#Scatterplot").on("click", function() {
        // Clean svg
        d3.select("#plotRegi").select("#Scatter").remove()
        d3.select("#plotRegi").select("#Box").remove()

        // Create dummy data
        d3.tsv("../demo_data/pbmc.tsv").then(d => scatterPlot(d))
    })

})