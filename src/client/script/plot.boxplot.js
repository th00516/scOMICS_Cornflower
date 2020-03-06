/* Boxplot */


/* Preparing */
$.getScript("../script/module/prepareCanvas.js")

$("#Scatter").ready(function () {
    $.getScript("../script/module/toolbox.js")
    $.getScript("../script/module/selectedList.js")
})


/* Running */
sample = $("#sampleSelection option:selected")
d3.tsv("../demo_data/" + sample.val() + ".tsv").then(d => boxPlot(d))



/* Drawing */
// Draw scatter plot
function boxPlot(dat) {
    var data = new Object()

    // Compute summary statistics used for the box
    for (let i = 0; i < dat.length; i++) {
        let K = "cluster_" + dat[i].seurat_clusters

        if (choosed.selected.has(K)) {
            if (!data.hasOwnProperty(K)) {
                data[K] = new Object()

                data[K].Cluster = dat[i].seurat_clusters
                data[K].Data = new Array()
            }

            data["cluster_" + dat[i].seurat_clusters].Data.push(dat[i].nCount_RNA / dat[i].nFeature_RNA)
        }
    }

    data = Object.values(data)


    // Set the width & height of the graph
    var margin = { top: 40, right: 40, bottom: 40, left: 40 },
        width = 800 - margin.left - margin.right,
        height = 800 - margin.top - margin.bottom


    // Set discrete X-axis
    function gen_xAxis() {
        let A = new Array()

        let block_num = choosed.selected.size + 1
        winWidth = width / block_num

        for (let n = 1; n < block_num; n++) {
            A.push(winWidth * n)
        }

        return A
    }


    // Set the scales of the graph
    var scale_x = d3
        .scaleOrdinal()
        .domain(Array.from(choosed.selected))
        .range(gen_xAxis())

    var scale_y = d3
        .scaleLinear()
        .domain([0, 50])
        .range([height, 0])


    // Set a few features for the graph
    var box_width = ((width - 100) - (40 * (choosed.selected.size - 1))) / (choosed.selected.size + 2)


    // Initializing ending
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
        .call(d3.axisBottom(scale_x))
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
        .attr("id", "boxplot")
        .append("rect")
        .attr("x", margin.left / 2)
        .attr("y", 0)
        .attr("width", width - margin.left / 2)
        .attr("height", height)
        .style("fill", "lightgrey")




    // Append the main vertical line
    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => boxStatistics(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x("cluster_" + d.Cluster) + "px")
        .attr("y1", d => scale_y(d.Max) + "px")
        .attr("x2", d => scale_x("cluster_" + d.Cluster) + "px")
        .attr("y2", d => scale_y(d.Min) + "px")
        .style("stroke", d => "#" +
            colorList[0][d.Cluster] +
            colorList[1][d.Cluster] +
            colorList[2][d.Cluster])
        .style("stroke-width", "3px")


    // Append the box
    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => boxStatistics(d))
        .enter()
        .append("rect")
        .attr("x", d => scale_x("cluster_" + d.Cluster) - box_width / 2 + "px")
        .attr("y", d => scale_y(d.Q3) + "px")
        .attr("width", box_width + "px")
        .attr("height", d => (scale_y(d.Q1) - scale_y(d.Q3)) + "px")
        .style("fill", "white")
        .style("stroke", d => "#" +
            colorList[0][d.Cluster] +
            colorList[1][d.Cluster] +
            colorList[2][d.Cluster])
        .style("stroke-width", "3px")


    // Append median, min and max horizontal lines
    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => boxStatistics(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x("cluster_" + d.Cluster) - box_width / 2)
        .attr("y1", d => scale_y(d.Min))
        .attr("x2", d => scale_x("cluster_" + d.Cluster) + box_width / 2)
        .attr("y2", d => scale_y(d.Min))
        .style("stroke", d => "#" +
            colorList[0][d.Cluster] +
            colorList[1][d.Cluster] +
            colorList[2][d.Cluster])
        .style("stroke-width", "3px")

    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => boxStatistics(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x("cluster_" + d.Cluster) - box_width / 2)
        .attr("y1", d => scale_y(d.Max))
        .attr("x2", d => scale_x("cluster_" + d.Cluster) + box_width / 2)
        .attr("y2", d => scale_y(d.Max))
        .style("stroke", d => "#" +
            colorList[0][d.Cluster] +
            colorList[1][d.Cluster] +
            colorList[2][d.Cluster])
        .style("stroke-width", "3px")

    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => boxStatistics(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x("cluster_" + d.Cluster) - box_width / 2)
        .attr("y1", d => scale_y(d.Median))
        .attr("x2", d => scale_x("cluster_" + d.Cluster) + box_width / 2)
        .attr("y2", d => scale_y(d.Median))
        .style("stroke", d => "#" +
            colorList[0][d.Cluster] +
            colorList[1][d.Cluster] +
            colorList[2][d.Cluster])
        .style("stroke-width", "3px")
    //




    //     // Append the option box
    //     svg
    //         .select("#box_" + (i + 1))
    //         .append("rect")
    //         .attr("id", "opt")
    //         .attr("x", scale_x(i + 1) - box_width / 2 - 10)
    //         .attr("y", scale_y(data[i].Max) - 10)
    //         .attr("width", box_width + 20)
    //         .attr("height", (scale_y(data[i].Min) - scale_y(data[i].Max)) + 20)
    //         .style("fill", "grey")
    //         .style("opacity", 0)

    //         .on("mouseover", function () {
    //             if (d3.select(this).style("opacity") == 0) {
    //                 d3.select(this).style("opacity", 0.3)
    //             }
    //         })

    //         .on("mouseout", function () {
    //             if (d3.select(this).style("opacity") == 0.3) {
    //                 d3.select(this).style("opacity", 0)
    //             }
    //         })

    //         .on("click", function () {
    //             if (d3.select(this).style("opacity") != 0.5) {
    //                 d3.select(this).style("opacity", 0.5)
    //             } else {
    //                 d3.select(this).style("opacity", 0.3)
    //             }
    //         })
    // }
}