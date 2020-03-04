/* jquery */


function draw_scatterplot(t) {
    if (t === "gl") {
        $.getScript("../script/plot.scatterplot.webgl.js")
    } else {
        $.getScript("../script/plot.scatterplot.js")
    }
}

function draw_boxplot() {
    $.getScript("../script/plot.boxplot.js")
}

function draw_focal_scatterplot() {
        $.getScript("../script/plot.focal_scatterplot.webgl.js")
}