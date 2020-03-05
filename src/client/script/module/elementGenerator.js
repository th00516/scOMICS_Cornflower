/* Element generator */


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