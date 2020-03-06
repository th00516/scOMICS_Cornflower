/* Prepare Canvas */


function prepareCanvas(k) {

    // Cleanup
    if (k == "cleanupAll") {

        d3.select("#plotRegi").select("#Scatter").remove()
        d3.select("#plotRegi").select("#Box").remove()

        d3.select("#plotRegi").select("#tip").remove()
        d3.select("#plotRegi").select("#selectedList").remove()
        d3.select("#plotRegi").select("#toolbox").remove()

    } else {

        d3.select("#plotRegi").select("#Scatter").remove()
        d3.select("#plotRegi").select("#Box").remove()

    }

    // Initializing
    d3.select("#plotRegi").select("#init").remove()
    d3.select("#plotRegi").append("h4").attr("id", "init").text("Initializing...")
    
}