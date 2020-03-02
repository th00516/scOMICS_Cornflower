/* jquery */

$(document).ready(function () {

    $("#Scatterplot_triger").click(function () {
        $.getScript("../script/plot.d3.scatterplot.js")
    })
})