/*d3*/

$(document).ready(function () {

    // Set random colors
    function get_random_color(n) {
        R = new Set()
        G = new Set()
        B = new Set()

        while (R.size < n) { R.add(Math.ceil(Math.random() * 255)) }
        while (G.size < n) { G.add(Math.ceil(Math.random() * 255)) }
        while (B.size < n) { B.add(Math.ceil(Math.random() * 255)) }

        return [Array.from(R), Array.from(G), Array.from(B)]
    }

    // Set a container for recoding selected clusters
    function selected_clusters() {
        this.selected = new Set()

        this.has = _cluster => this.selected.has(_cluster)
        this.add = function (_cluster) { this.selected.add(_cluster) }
        this.del = function (_cluster) { this.selected.delete(_cluster) }
    }

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


    // Draw scatter plot
    function scatterPlot(dat) {
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
            .attr("id", "hide_show")
            .style("width", "85px")
            .style("height", "30px")
            .style("font-weight", "bold")
            .text("H / S")

        toolbox
            .append("table")
            .append("button")
            .attr("id", "exp")
            .style("width", "85px")
            .style("height", "30px")
            .style("font-weight", "bold")
            .text("Exp.")

        // Set the width & height of the graph
        var margin = { top: 40, right: 40, bottom: 40, left: 40 },
            width = 710 - margin.left - margin.right,
            height = 660 - margin.top - margin.bottom

        // Set the scales of the graph
        var scale_x = d3
            .scaleLinear()
            .domain([-50, 50])
            .range([0, width])

        var scale_y = d3
            .scaleLinear()
            .domain([-50, 50])
            .range([height, 0])

        // Initializing
        d3.select("#plotRegi").select("#init").remove()

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
            .data(dat.slice(0, 20000), d => d)
            .enter()
            .append("circle")
            .attr("class", "cluster_unselected")
            .attr("id", d => "cluster_" + d.seurat_clusters)
            .attr("cx", d => scale_x(d.TSNE_1))
            .attr("cy", d => scale_y(d.TSNE_2))
            .attr("r", 2)
            .style("fill", d => "rgb(" + [color_list[0][d.seurat_clusters],
            color_list[1][d.seurat_clusters],
            color_list[2][d.seurat_clusters]] + ")")
            .style("opacity", 0.9)

            .on("mouseover", function () {
                tip
                    .style("display", "block")
                    .style("left", (d3.event.pageX + 20) + "px")
                    .style("top", (d3.event.pageY + 20) + "px")
                    .text(d3.select(this).attr("id"))

                if (choosed.selected.size > 0) {
                    selected_list
                        .style("display", "block")
                        .style("left", (d3.event.pageX + 35) + "px")
                        .style("top", (d3.event.pageY + 55) + "px")
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
                    .style("left", (d3.event.pageX + 35) + "px")
                    .style("top", (d3.event.pageY + 55) + "px")
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
                                d3.selectAll(".cluster_unselected").transition().duration(1400).style("opacity", 0.9)

                                selected_list.style("opacity", 0).text("")
                                toolbox.transition().duration(700).style("opacity", 0)

                                for (var x of choosed.selected) { choosed.del(x) }
                            }
                        })

                    toolbox
                        .select("#hide_show")
                        .on("mousedown", function () {
                            if (choosed.selected.size > 0) {
                                d3.selectAll(".cluster_selected").transition().duration(300).style("opacity", 0.1)
                                d3.selectAll(".cluster_unselected").transition().duration(300).style("opacity", 0.9)
                            }
                        })
                        .on("mouseup", function () {
                            if (choosed.selected.size > 0) {
                                d3.selectAll(".cluster_selected").transition().duration(200).style("opacity", 0.9)
                                d3.selectAll(".cluster_unselected").transition().duration(200).style("opacity", 0.1)
                            }
                        })

                    toolbox
                        .select("#exp")
                        .on("click", function () {
                            d3.select("body").append("script").attr("src", "../script/plot.d3.boxplot.js")
                            // location.reload(true) 
                        })
                } else {
                    d3.selectAll(".cluster_selected").attr("class", "cluster_unselected")
                    d3.selectAll(".cluster_unselected").transition().duration(1400).style("opacity", 0.9)

                    selected_list.style("display", "none").text("")
                    toolbox.transition().duration(700).style("opacity", 0)
                }
            })
    }


    // Main
    d3.select("#Scatterplot_triger").on("click", function () {
        // Clean svg
        d3.select("#plotRegi").select("#Scatter").remove()
        d3.select("#plotRegi").select("#Box").remove()

        // Initializing
        d3.select("#plotRegi").append("h4").attr("id", "init").text("Initializing...")

        // Create dummy data
        d3.tsv("../demo_data/pbmc.tsv").then(d => scatterPlot(d))
    })

})