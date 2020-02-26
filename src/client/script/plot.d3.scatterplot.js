/*d3*/

$(document).ready(function() {

    var margin = {top: 40, right: 40, bottom: 40, left: 40},
         width = 600 - margin.left - margin.right,
        height = 550 - margin.top - margin.bottom

    // Set random colors
    function get_random_color(n) {
        R = new Set()
        G = new Set()
        B = new Set()

        while (R.size < n) {R.add(Math.round(Math.random() * 255))}
        while (G.size < n) {G.add(Math.round(Math.random() * 255))}
        while (B.size < n) {B.add(Math.round(Math.random() * 255))}

        return [Array.from(R), Array.from(G), Array.from(B)]
    }


d3.select("#Scatterplot").on("click", function() {
    // Clean svg
    d3.select("#plotRegi").select("#Scatter").remove()
    d3.select("#plotRegi").select("#Box").remove()

    // Create dummy data
    d3.tsv("../demo_data/pbmc.tsv").then(d => scatterPlot(d))

    function scatterPlot(dat) {
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

        for (var i = 0; i <= 20; i++) {
            svg
                .select("#scatter")
                .selectAll("NONE")
                .data(dat, d => d)
                .enter()
                .filter(d => d.seurat_clusters == i)
                .append("g")
                .attr("id", "scatter_" + (i + 1))
                .append("circle")
                .attr("cx", d => scale_x(d.TSNE_1))
                .attr("cy", d => scale_y(d.TSNE_2))
                .attr("r", 2)
                .style("fill", "white")
                .style("fill-opacity", 0)
                .style("stroke", "rgb(" + [color_list[0][i], 
                                           color_list[1][i], 
                                           color_list[2][i]] + ")")
                .style("stroke-width", "1px")
                .style("stroke-opacity", 0.1)
        }

        d3
            .select("scatter_1")
            .on("mouseover", function() {
                d3.select(this).style("stroke", "red")
            })

            .on("mouseout", function() {
                d3.select(this).style("opacity", 0)
            })
    }
})

})