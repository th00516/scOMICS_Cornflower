/* Selected list */


// Set a selected list
var selectedList = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "selected_list")
    .style("display", "none")
    .style("position", "absolute")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")
    .style("opacity", 0.9)