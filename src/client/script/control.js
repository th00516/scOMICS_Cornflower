/* jquery */


function drawScatterplot(seqMethod) {

    switch (seqMethod) {

        case "rna":
            $.getScript("../script/plot.scatterplot.js"); break

        case "atac":
            $.getScript("../script/plot.scatterplot.js"); break

    }

}

function drawBoxplot() {

    $.getScript("../script/plot.boxplot.js")

}