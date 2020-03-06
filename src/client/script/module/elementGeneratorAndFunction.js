/* Element generator and function*/


// Generate random colors
function generateRandomColor() {
    R = new Set()
    G = new Set()
    B = new Set()

    while (R.size < 100) { R.add(Math.ceil(Math.random() * 150 + 50).toString(16)) }
    while (G.size < 100) { G.add(Math.ceil(Math.random() * 150 + 50).toString(16)) }
    while (B.size < 100) { B.add(Math.ceil(Math.random() * 150 + 50).toString(16)) }

    return [Array.from(R), Array.from(G), Array.from(B)]
}


// Statistics for boxplot
function boxStatistics(D) {
    D.Data = D.Data.sort(d3.ascending)

    D.Q1 = d3.quantile(D.Data, 0.25)
    D.Median = d3.quantile(D.Data, 0.5)
    D.Q3 = d3.quantile(D.Data, 0.75)
    D.InterQTR = D.Q3 - D.Q1
    D.Min = D.Q1 - 1.5 * D.InterQTR > 0 ? D.Q1 - 1.5 * D.InterQTR : 0
    D.Max = D.Q3 + 1.5 * D.InterQTR < 100 ? D.Q3 + 1.5 * D.InterQTR : 100

    return D
}