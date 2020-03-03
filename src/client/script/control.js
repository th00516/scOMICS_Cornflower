/* jquery */


function draw_scatterplot(t) {
    if (t === "gl") {
        $.getScript("../script/plot.d3.scatterplot.webgl.js")
    } else {
        $.getScript("../script/plot.d3.scatterplot.js")
    }
}

function draw_boxplot() {
    $.getScript("../script/plot.d3.boxplot.js")
}