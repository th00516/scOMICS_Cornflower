/* d3 */


/* Preparing */
// Clean svg
d3.select("#plotRegi").select("#Scatter").remove()
d3.select("#plotRegi").select("#Box").remove()

d3.select("#plotRegi").select("#tip").remove()
d3.select("#plotRegi").select("#selected_list").remove()


/* Running */
// Initializing
d3.select("#plotRegi").select("#init").remove()
d3.select("#plotRegi").append("h4").attr("id", "init").text("Initializing...")

// Import data
d3.tsv("../demo_data/pbmc.tsv").then(d => boxPlot(d))




/* Function */
// Statistics for boxplot
function box_stat(D) {
    D.Data = D.Data.sort(d3.ascending)

    D.Q1 = d3.quantile(D.Data, 0.25)
    D.Median = d3.quantile(D.Data, 0.5)
    D.Q3 = d3.quantile(D.Data, 0.75)
    D.InterQTR = D.Q3 - D.Q1
    D.Min = D.Q1 - 1.5 * D.InterQTR > 0 ? D.Q1 - 1.5 * D.InterQTR : 0
    D.Max = D.Q3 + 1.5 * D.InterQTR < 100 ? D.Q3 + 1.5 * D.InterQTR : 100

    return D
}

// Draw scatter plot
function boxPlot(dat) {
    // Parse data
    var data = new Object()

    // Compute summary statistics used for the box
    let n = 1
    for (let i = 0; i < dat.length; i++) {
        let K = "cluster_" + dat[i].seurat_clusters

        if (choosed.selected.has(K)) {
            if (!data.hasOwnProperty(K)) {
                data[K] = new Object()

                data[K].ID = n
                data[K].Cluster = dat[i].seurat_clusters
                data[K].Data = new Array()

                n++
            }

            data["cluster_" + dat[i].seurat_clusters].Data.push(dat[i].nCount_RNA / dat[i].nFeature_RNA)
        }
    }

    data = Object.values(data)

    // Set the width & height of the graph
    var margin = { top: 40, right: 40, bottom: 40, left: 40 },
        width = 850 - margin.left - margin.right,
        height = 700 - margin.top - margin.bottom

    // Set the scales of the graph
    var scale_x = d3
        .scaleLinear()
        .domain([0, choosed.selected.size + 1])
        .range([0, width])

    var scale_y = d3
        .scaleLinear()
        .domain([0, 50])
        .range([height, 0])

    // Set a few features for the graph
    var box_width = width / choosed.selected.size - 40

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
        .call(d3.axisBottom(scale_x).ticks(choosed.selected.size + 1))
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

    // Append the main vertical line
    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => box_stat(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x(d.ID) + "px")
        .attr("y1", d => scale_y(d.Max) + "px")
        .attr("x2", d => scale_x(d.ID) + "px")
        .attr("y2", d => scale_y(d.Min) + "px")
        .style("stroke", d => "rgb(" + [
            color_list[0][d.Cluster],
            color_list[1][d.Cluster],
            color_list[2][d.Cluster]
        ] + ")")
        .style("stroke-width", "2px")

    // Append the box
    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => box_stat(d))
        .enter()
        .append("rect")
        .attr("x", d => scale_x(d.ID) - box_width / 2 + "px")
        .attr("y", d => scale_y(d.Q3) + "px")
        .attr("width", box_width + "px")
        .attr("height", d => (scale_y(d.Q1) - scale_y(d.Q3)) + "px")
        .style("fill", "white")
        .style("stroke", d => "rgb(" + [
            color_list[0][d.Cluster],
            color_list[1][d.Cluster],
            color_list[2][d.Cluster]
        ] + ")")
        .style("stroke-width", "2px")

    // Append median, min and max horizontal lines
    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => box_stat(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x(d.ID) - box_width / 2)
        .attr("y1", d => scale_y(d.Min))
        .attr("x2", d => scale_x(d.ID) + box_width / 2)
        .attr("y2", d => scale_y(d.Min))
        .style("stroke", d => "rgb(" + [
            color_list[0][d.Cluster],
            color_list[1][d.Cluster],
            color_list[2][d.Cluster]
        ] + ")")
        .style("stroke-width", "2px")

    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => box_stat(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x(d.ID) - box_width / 2)
        .attr("y1", d => scale_y(d.Max))
        .attr("x2", d => scale_x(d.ID) + box_width / 2)
        .attr("y2", d => scale_y(d.Max))
        .style("stroke", d => "rgb(" + [
            color_list[0][d.Cluster],
            color_list[1][d.Cluster],
            color_list[2][d.Cluster]
        ] + ")")
        .style("stroke-width", "2px")

    svg
        .select("#boxplot")
        .selectAll("NONE")
        .data(data, d => box_stat(d))
        .enter()
        .append("line")
        .attr("x1", d => scale_x(d.ID) - box_width / 2)
        .attr("y1", d => scale_y(d.Median))
        .attr("x2", d => scale_x(d.ID) + box_width / 2)
        .attr("y2", d => scale_y(d.Median))
        .style("stroke", d => "rgb(" + [
            color_list[0][d.Cluster],
            color_list[1][d.Cluster],
            color_list[2][d.Cluster]
        ] + ")")
        .style("stroke-width", "2px")


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