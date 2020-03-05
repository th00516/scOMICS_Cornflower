/* Tip */


// Set a tip
var tip = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "tip")
    .style("display", "none")
    .style("position", "absolute")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("background-color", "lightyellow")
    .style("font-weight", "bold")
    .style("font-style", "italic")
    .style("opacity", 0.9)