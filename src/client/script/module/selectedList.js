/* Selected list */


// Set a selected list
var selectedList = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "selectedList")
    .style("display", "none")
    .style("position", "absolute")
    .style("left", "83%")
    .style("top", "513px")
    .style("max-height", "307px")
    .style("overflow-y", "scroll")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")
    .style("opacity", 0.9)