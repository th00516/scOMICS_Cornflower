/* Prepare Canvas */


function prepareCanvas(k) {

    // Cleanup
    if (k == "cleanupAll") {

        d3.select("#controlPanel").select("#toolbox").remove()
        d3.select("#controlPanel").select("#selectedClusterList").remove()

    }

    d3.select("#plotRegi").select("#canvasPanel").remove()
    d3.select("#plotRegi").select("#Box").remove()
    d3.select("#plotRegi").select("#tip").remove()
    d3.select("#plotRegi").select("#init").remove()

}