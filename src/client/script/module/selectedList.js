/* Selected list */


// Set a selected list
var selectedClusterList = d3
    .select("#controlPanel")
    .append("div")
    .attr("id", "selectedClusterList")
    .style("width", "200px")
    .style("max-height", "400px")
    .style("overflow-y", "scroll")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("margin-bottom", "20px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")
    .text("SELECTED")