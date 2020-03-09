/* Prepare Canvas */


function prepareCanvas(k) {

    // Cleanup
    if (k == "cleanupAll") {

        d3.select("#controlPanel").select("#toolbox").remove()
        d3.select("#controlPanel").select("#selectedClusterList").remove()

    }

    d3.select("#plotRegi").select("#Scatter").remove()
    d3.select("#plotRegi").select("#Box").remove()
    d3.select("#plotRegi").select("#tip").remove()
    d3.select("#plotRegi").select("#init").remove()

    // Initializing
    d3.select("#plotRegi").append("h4").attr("id", "init").text("Initializing...")

}