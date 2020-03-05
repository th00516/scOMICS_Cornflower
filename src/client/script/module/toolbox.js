/* Toolbox */


// Set a toolbox
var toolbox = d3
    .select("#plotRegi")
    .append("div")
    .attr("id", "toolbox")
    .style("display", "none")
    .style("position", "absolute")
    .style("left", "83%")
    .style("top", "213px")
    .style("width", "90px")
    .style("padding", "5px")
    .style("border-style", "solid")
    .style("border-width", "2px")
    .style("background-color", "lightblue")
    .style("font-weight", "bold")
    .style("opacity", 0.9)

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

toolbox
    .append("table")
    .append("button")
    .attr("id", "focus")
    .style("width", "85px")
    .style("height", "30px")
    .style("font-weight", "bold")
    .text("Focus")