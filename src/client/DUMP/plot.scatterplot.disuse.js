/* Scatterplot */


/* Preparing */
// Cleanup
d3.select("#plotRegi").select("#Scatter").remove()
d3.select("#plotRegi").select("#Box").remove()

d3.select("#plotRegi").select("#tip").remove()
d3.select("#plotRegi").select("#selected_list").remove()
d3.select("#plotRegi").select("#toolbox").remove()


/* Running */
// Initializing
d3.select("#plotRegi").select("#init").remove()
d3.select("#plotRegi").append("h4").attr("id", "init").text("Initializing...")

// Import data
d3.tsv("../demo_data/pbmc.tsv").then(d => scatterPlot(d))




/* Member */
// Set a tip, selected_list
var tip = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "tip")
    .style("display", "none")
    .style("position", "absolute")
    .style("padding", "5px")
    .style("border-style", "dotted")
    .style("border-width", "1px")
    .style("background-color", "lightyellow")
    .style("font-weight", "bold")
    .style("font-style", "italic")
    .style("opacity", 0.9)

var selected_list = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "selected_list")
    .style("display", "none")
    .style("position", "absolute")
    .style("padding", "5px")
    .style("border-style", "dotted")
    .style("border-width", "1px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")
    .style("opacity", 0.9)

// Set a scatter toolbox
var toolbox = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "toolbox")
    .style("display", "none")
    .style("position", "absolute")
    .style("width", "90px")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "1px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")
    .style("opacity", 0)

toolbox
    .append("table")
    .append("button")
    .attr("id", "clear")
    .style("width", "85px")
    .style("height", "30px")
    .style("font-weight", "bold")
    .text("Clear")

toolbox
    .append("hr")

toolbox
    .append("table")
    .append("button")
    .attr("id", "exp")
    .style("width", "85px")
    .style("height", "30px")
    .style("font-weight", "bold")
    .text("Exp.")




/* Function */
// Set random colors
function get_random_color() {
    R = new Set()
    G = new Set()
    B = new Set()

    while (R.size < 100) { R.add(Math.ceil(Math.random() * 150 + 50).toString(16)) }
    while (G.size < 100) { G.add(Math.ceil(Math.random() * 150 + 50).toString(16)) }
    while (B.size < 100) { B.add(Math.ceil(Math.random() * 150 + 50).toString(16)) }

    return [Array.from(R), Array.from(G), Array.from(B)]
}

color_list = get_random_color()

// Set a container for recoding selected clusters
function selected_clusters() {
    this.selected = new Set()

    this.has = _cluster => this.selected.has(_cluster)
    this.add = function (_cluster) { this.selected.add(_cluster) }
    this.del = function (_cluster) { this.selected.delete(_cluster) }
}

choosed = new selected_clusters()


// Draw scatter plot
function scatterPlot(dat) {
    // Set the width & height of the graph
    let margin = { top: 40, right: 40, bottom: 40, left: 40 },
        width = 850 - margin.left - margin.right,
        height = 700 - margin.top - margin.bottom

    // Set the scales of the graph
    let scale_x = d3
        .scaleLinear()
        .domain([-50, 50])
        .range([0, width])

        let scale_y = d3
        .scaleLinear()
        .domain([-50, 50])
        .range([height, 0])

    // Initializing ending
    d3.select("#plotRegi").select("#init").remove()

    // Append the svg object and a canvas for the following drawing
    let svg = d3
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

    // Drawing
    svg
        .select("#Canvas")
        .append("g")
        .attr("id", "scatterplot")

    svg
        .select("#scatterplot")
        .selectAll("NONE")
        .data(dat, d => d)
        .enter()
        .append("circle")
        .attr("class", "cluster_unselected")
        .attr("id", d => "cluster_" + d.seurat_clusters)
        .attr("cx", d => scale_x(d.TSNE_1) + "px")
        .attr("cy", d => scale_y(d.TSNE_2) + "px")
        .attr("r", 2)
        .style("fill", d => "#" +
            color_list[0][d.seurat_clusters] +
            color_list[1][d.seurat_clusters] +
            color_list[2][d.seurat_clusters])
        .style("opacity", 0.1)

        .on("mouseover", function () {
            tip
                .style("display", "block")
                .style("left", (event.pageX + 20) + "px")
                .style("top", (event.pageY + 20) + "px")
                .text(d3.select(this).attr("id"))

            if (choosed.selected.size > 0) {
                selected_list
                    .style("display", "block")
                    .style("left", (event.pageX + 35) + "px")
                    .style("top", (event.pageY + 55) + "px")
            }
        })

        .on("mouseout", function () {
            tip
                .style("display", "none")

            selected_list
                .style("display", "none")
        })

        .on("click", function () {
            selected_list
                .style("display", "block")
                .style("left", (event.pageX + 35) + "px")
                .style("top", (event.pageY + 55) + "px")
                .text("")

            if (choosed.has(d3.select(this).attr("id"))) {
                choosed.del(d3.select(this).attr("id"))
                d3.selectAll("#" + d3.select(this).attr("id")).attr("class", "cluster_unselected")
            } else {
                choosed.add(d3.select(this).attr("id"))
                d3.selectAll("#" + d3.select(this).attr("id")).attr("class", "cluster_selected")
            }

            d3.selectAll(".cluster_selected").transition().duration(1400).style("opacity", 0.9)
            d3.selectAll(".cluster_unselected").transition().duration(1400).style("opacity", 0.1)

            if (choosed.selected.size > 0) {
                selected_list
                    .selectAll("NONE")
                    .data(Array.from(choosed.selected))
                    .enter()
                    .append("table")
                    .text(d => d)

                toolbox
                    .style("display", "block")
                    .style("left", "85%")
                    .style("top", "150px")
                    .transition()
                    .duration(700)
                    .style("opacity", 0.9)

                toolbox
                    .select("#clear")
                    .on("click", function () {
                        if (choosed.selected.size > 0) {
                            d3.selectAll(".cluster_selected").attr("class", "cluster_unselected")
                            d3.selectAll(".cluster_unselected").transition().duration(1400).style("opacity", 0.1)

                            selected_list.text("")
                            selected_list.style("display", "none")

                            toolbox.style("display", "none")

                            for (var x of choosed.selected) { choosed.del(x) }
                        }
                    })

                toolbox
                    .select("#exp")
                    .on("click", function () {
                        $.getScript("../script/control.js")
                        draw_boxplot()
                    })
            } else {
                selected_list.style("display", "none")
                toolbox.style("display", "none")
            }
        })
}