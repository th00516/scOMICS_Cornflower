/* d3-pixi */


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
function get_random_color(n) {
    R = new Set()
    G = new Set()
    B = new Set()

    while (R.size < n) { R.add(Math.ceil(Math.random() * 255).toString(16)) }
    while (G.size < n) { G.add(Math.ceil(Math.random() * 255).toString(16)) }
    while (B.size < n) { B.add(Math.ceil(Math.random() * 255).toString(16)) }

    return [Array.from(R), Array.from(G), Array.from(B)]
}

color_list = get_random_color(100)

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

    let app = new PIXI.Application({ width, height, antialias: true, transparent: true, resolution: 1 })

    app.view.id = "Scatter"

    document.getElementById("plotRegi").appendChild(app.view)

    d3
        .select(app.view)
        .selectAll("NONE")
        .data(dat, d => d)
        .enter()
        .each(d => {
            const circle = new PIXI.Graphics()

            circle.name = "cluster_" + d.seurat_clusters

            circle.interactive = true
            circle.buttonMode = true
            circle.beginFill(
                "0x" +
                color_list[0][d.seurat_clusters] +
                color_list[1][d.seurat_clusters] +
                color_list[2][d.seurat_clusters]
            )
            circle.alpha = 0.1
            circle.drawCircle(scale_x(d.TSNE_1), scale_y(d.TSNE_2), 2)
            circle.endFill()

            circle.on("pointerover", e => {
                tip
                    .style("display", "block")
                    .style("left", e.data.global.x + "px")
                    .style("top", e.data.global.y + "px")
                    .text("cluster_" + d.seurat_clusters)

                if (choosed.selected.size > 0) {
                    selected_list
                        .style("display", "block")
                        .style("left", (e.data.global.x + 35) + "px")
                        .style("top", (e.data.global.y + 35) + "px")
                }
            })

            circle.on("pointerout", e => {
                tip
                    .style("display", "none")
    
                selected_list
                    .style("display", "none")
            })    

            circle.on("click", e => {
                selected_list
                    .style("display", "block")
                    .style("left", (e.data.global.x + 35) + "px")
                    .style("top", (e.data.global.y + 35) + "px")
                    .text("")

                if (choosed.has("cluster_" + d.seurat_clusters)) {
                    choosed.del("cluster_" + d.seurat_clusters)
                    circle.alpha = 0.1
                } else {
                    choosed.add("cluster_" + d.seurat_clusters)
                    circle.alpha = 0.9

                    selected_list
                        .selectAll("NONE")
                        .data(Array.from(choosed.selected))
                        .enter()
                        .append("table")
                        .text(d => d.seurat_clusters)
                }
            })

            app.stage.addChild(circle)
        })

    app.renderer.render(app.stage)
}