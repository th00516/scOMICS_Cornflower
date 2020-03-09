/* Toolbox */


// Set a toolbox
var toolbox = d3
    .select("#controlPanel")
    .append("div")
    .attr("id", "toolbox")
    .style("width", "200px")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("margin-bottom", "20px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")

toolbox
    .append("table")
    .append("button")
    .attr("id", "clear")
    .style("width", "85px")
    .style("height", "30px")
    .style("font-weight", "bold")
    .text("Clear")

toolbox
    .append("hr")

toolbox
    .append("table")
    .append("button")
    .attr("id", "exp")
    .style("width", "85px")
    .style("height", "30px")
    .style("font-weight", "bold")
    .text("Exp.")