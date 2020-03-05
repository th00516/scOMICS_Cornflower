/* Used data structure */


// Set a container for recoding selected clusters
function selectedClusters() {
    this.selected = new Set()

    this.has = _cluster => this.selected.has(_cluster)
    this.add = _cluster => this.selected.add(_cluster)
    this.del = _cluster => this.selected.delete(_cluster)
}