/* Selected list */


// Set a selected list
var selectedList = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "selectedList")
    .style("position", "absolute")
    .style("left", "90px")
    .style("top", "300px")
    .style("width", "170px")
    .style("max-height", "400px")
    .style("overflow-y", "scroll")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")
    .style("opacity", 0.9)
    .text("SELECTED")