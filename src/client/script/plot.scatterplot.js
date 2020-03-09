/* Scatterplot */


/* Preparing */
prepareCanvas("cleanupAll")


$("#Scatter").ready(function () {

    $.getScript("../script/module/toolbox.js")
    $.getScript("../script/module/selectedList.js")
    $.getScript("../script/module/tip.js")

})


/* Running */
sample = $("#sampleSelection option:selected")
seqType = $("#seqTypeSelection option:selected")
clusterType = $("#clusterTypeSelection option:selected")

d3.tsv("../demo_data/" + sample.val() + "." + seqType.val() + ".tsv").then(d => scatterPlot(d))


/* Element initialization */
var choosed = new selectedClusters()
var colorList = generateRandomColor()


/* Drawing */
// Draw scatter plot
function scatterPlot(dat) {
    // Set the width & height of the graph
    let margin = { top: 40, right: 40, bottom: 40, left: 40 },

        width = 820 - margin.left - margin.right,
        height = 800 - margin.top - margin.bottom


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
        resolution: window.devicePixelRatio || 1,
        backgroundColor: 0x000000

    })

    app.renderer.view.id = "Scatter"


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

            circle.beginFill(
                "0x" +
                colorList[0][d.seurat_clusters] +
                colorList[1][d.seurat_clusters] +
                colorList[2][d.seurat_clusters]
            )
            circle.drawCircle(scale_x(d[clusterType.val() + "_1"]), scale_y(d[clusterType.val() + "_2"]), 3)
            circle.endFill()

            spriteGroup[cluster].addChild(circle)

        })


    // Set up toolbox
    toolbox
        .select("#clear")
        .on("click", function () {

            if (choosed.selected.size > 0) {

                selectedClusterList.text("SELECTED")

                let keys_list = Object.keys(spriteGroup)
                for (let k of keys_list) { spriteGroup[k].alpha = 0.4 }

                for (let k of choosed.selected) { choosed.del(k) }

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


    // Append activity
    let keys_list = Object.keys(spriteGroup)
    for (let k of keys_list) {

        spriteGroup[k].alpha = 0.4

        spriteGroup[k].interactive = true

        spriteGroup[k].on("mouseover", function () {

            if (event) {

                tip
                    .style("display", "block")
                    .style("left", (event.pageX + 20) + "px")
                    .style("top", (event.pageY + 20) + "px")
                    .text(k)

            }

        })


        spriteGroup[k].on("pointerout", function () { tip.style("display", "none") })


        spriteGroup[k].on("pointertap", function () {

            if (choosed.has(k)) {

                choosed.del(k)

            } else {

                choosed.add(k)

            }


            selectedClusterList.text("SELECTED")

            if (choosed.selected.size > 0) {

                selectedClusterList.append("hr")

                let keys_list = Object.keys(spriteGroup).sort()
                for (let k of keys_list) {

                    if (choosed.has(k)) {

                        spriteGroup[k].alpha = 1

                        selectedClusterList
                            .append("table")
                            .text(k + "|" + spriteNumber[k])

                    } else {

                        spriteGroup[k].alpha = 0.1
                    }

                }


            } else {

                let keys_list = Object.keys(spriteGroup).sort()
                for (let k of keys_list) { spriteGroup[k].alpha = 0.5 }

            }

        })

        app.stage.addChild(spriteGroup[k])

    }

    app.render(app.stage)

    document.getElementById("plotRegi").appendChild(app.renderer.view)
}