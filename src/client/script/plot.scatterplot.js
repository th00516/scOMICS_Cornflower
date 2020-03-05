/* Scatterplot */


/* Preparing */
$.getScript("../script/module/prepareCanvas.js")

$("#Scatter").ready(function () {
    $.getScript("../script/module/toolbox.js")
    $.getScript("../script/module/selectedList.js")
    $.getScript("../script/module/tip.js")
})


/* Running */
sample = $("#sampleSelection option:selected")
d3.tsv("../demo_data/" + sample.val() + ".tsv").then(d => scatterPlot(d))


/* Element initialization */
choosed = new selectedClusters()
colorList = generateRandomColor()


/* Drawing */
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

    // Generate canvas
    d3.select("#plotRegi").select("#init").remove()

    let app = new PIXI.Application({
        width: width,
        height: height,
        antialias: true,
        resolution: 1,
        backgroundColor: 0x000000
    })

    app.renderer.view.id = "Scatter"

    document.getElementById("plotRegi").appendChild(app.renderer.view)

    // Append sprite
    let spriteGroup = new Object()
    let spriteNumber = new Object()

    d3
        .select(app.renderer.view)
        .selectAll("NONE")
        .data(dat, d => d)
        .enter()
        .each(d => {
            let cluster = "cluster_" + d.seurat_clusters

            if (!spriteGroup.hasOwnProperty(cluster)) {
                spriteGroup[cluster] = new PIXI.Container()
                spriteNumber[cluster] = 1

            }

            const circle = new PIXI.Graphics()

            spriteNumber[cluster] += 1

            circle.interactive = true
            circle.buttonMode = true
            circle.beginFill(
                "0x" +
                colorList[0][d.seurat_clusters] +
                colorList[1][d.seurat_clusters] +
                colorList[2][d.seurat_clusters]
            )
            circle.drawCircle(scale_x(d.TSNE_1), scale_y(d.TSNE_2), 3)
            circle.endFill()

            circle.on("mouseover", function () {
                tip
                    .style("display", "block")
                    .style("left", (event.pageX + 15) + "px")
                    .style("top", (event.pageY + 15) + "px")
                    .text(cluster)
            })

            circle.on("pointerout", function () {
                tip.style("display", "none")
            })

            circle.on("pointertap", function () {
                if (choosed.has(cluster)) {
                    choosed.del(cluster)
                } else {
                    choosed.add(cluster)
                }

                if (choosed.selected.size > 0) {
                    selectedList
                        .style("display", "block")

                    selectedList
                        .text("SELECTED")
                        .append("hr")




                    // Set up toolbox
                    toolbox
                        .style("display", "block")

                    toolbox
                        .select("#clear")
                        .on("click", function () {
                            if (choosed.selected.size > 0) {
                                selectedList.text("")
                                selectedList.style("display", "none")

                                toolbox.style("display", "none")

                                for (let k of Object.keys(spriteGroup).sort()) {
                                    spriteGroup[k].alpha = 0.5
                                }

                                for (var x of choosed.selected) { choosed.del(x) }
                            }
                        })

                    toolbox
                        .select("#exp")
                        .on("click", function () {
                            $.getScript("../script/control.js")
                            drawBoxplot()
                        })

                    toolbox
                        .select("#focus")
                        .on("click", function () {
                            $.getScript("../script/control.js")
                        })
                    //




                    for (let k of Object.keys(spriteGroup).sort()) {
                        if (choosed.has(k)) {
                            spriteGroup[k].alpha = 0.9

                            selectedList
                                .append("table")
                                .text(k + "|" + spriteNumber[k])
                        } else {
                            spriteGroup[k].alpha = 0.1
                        }
                    }
                } else {
                    for (let k of Object.keys(spriteGroup).sort()) {
                        spriteGroup[k].alpha = 0.5
                    }

                    selectedList.text("")
                    selectedList.style("display", "none")

                    toolbox.style("display", "none")
                }
            })

            spriteGroup[cluster].addChild(circle)

            spriteGroup[cluster].alpha = 0.5

            app.stage.addChild(spriteGroup[cluster])
        })

    app.render(app.stage)
}