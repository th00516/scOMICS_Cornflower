/* Scatterplot */


$("#showScatterplot").bind("click", function drawScatterplot() {

    /* Preparing */
    prepareCanvas("cleanupAll")

    $.getScript("../script/module/toolbox.js")
    $.getScript("../script/module/selectedList.js")
    $.getScript("../script/module/tip.js")


    /* Element initialization */
    choosed = new selectedClusters()
    colorList = generateRandomColor()

    // Initializing
    d3.select("#plotRegi").append("h4").attr("id", "init").text("Initializing...")


    /* Running */
    sample = $("#sampleSelection option:selected")
    seqType = $("#seqTypeSelection option:selected")
    clusterType = $("#clusterTypeSelection option:selected")

    d3.tsv("../demo_data/" + sample.val() + "." + seqType.val() + ".tsv").then(d => scatterPlot(d))


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
            resolution: 1,
            backgroundColor: 0xFFFFFF

        })

        app.renderer.view.id = "canvasPanel"


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


        // Append activity
        let keys_list = Object.keys(spriteGroup)
        for (let k of keys_list) {

            spriteGroup[k].alpha = 0.5

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

                    let keys_list = Object.keys(spriteGroup).sort()
                    for (let k of keys_list) { spriteGroup[k].alpha = 0.1 }

                    selectedClusterList.append("hr")

                    let selected_keys_list = Array.from(choosed.selected)
                    for (let k of selected_keys_list) {

                        spriteGroup[k].alpha = 1

                        selectedClusterList
                            .append("table")
                            .text(k + "|" + spriteNumber[k])

                    }

                } else {

                    let keys_list = Object.keys(spriteGroup).sort()
                    for (let k of keys_list) { spriteGroup[k].alpha = 0.5 }

                    selectedClusterList.append("hr")

                    selectedClusterList
                        .append("table")
                        .text("(ALL)")

                }

            })

            app.stage.addChild(spriteGroup[k])

        }

        document.getElementById("plotRegi").appendChild(app.renderer.view)


        // Set up toolbox
        toolbox
            .select("#clear")
            .on("click", function () {

                if (choosed.selected.size > 0) {

                    selectedClusterList.text("SELECTED")

                    selectedClusterList.append("hr")

                    selectedClusterList
                        .append("table")
                        .text("(ALL)")

                    let keys_list = Object.keys(spriteGroup)
                    for (let k of keys_list) { spriteGroup[k].alpha = 0.5 }

                    for (let k of choosed.selected) { choosed.del(k) }

                }

            })

        toolbox
            .select("#exp")
            .on("click", function () {

                if (choosed.selected.size > 0) {

                    drawBoxplot()

                } else {

                    let keys_list = Object.keys(spriteGroup)
                    for (let k of keys_list) { choosed.selected.add(k) }

                    drawBoxplot()

                }

            })

    }

})