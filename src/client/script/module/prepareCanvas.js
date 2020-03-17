/* Prepare Canvas */


function prepareCanvas(k) {

    // Cleanup
    if (k == "cleanupAll") {

        $("#controlPanel > #toolbox").remove()
        $("#controlPanel > #selectedClusterList").remove()

    }

    $("#plotRegi > #canvasPanel").remove()
    $("#plotRegi > #Box").remove()
    $("#plotRegi > #tip").remove()
    $("#plotRegi > #init").remove()

}