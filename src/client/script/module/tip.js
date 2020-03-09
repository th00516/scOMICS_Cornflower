/* Tip */


// Set a tip
var tip = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "tip")
    .style("opacity", 0)
    .style("position", "absolute")
    .style("left", "0px")
    .style("top", "0px")
    .style("width", "100px")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("background-color", "lightyellow")
    .style("font-weight", "bold")
    .style("font-style", "italic")