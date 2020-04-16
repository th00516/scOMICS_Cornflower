#!/usr/bin/env python3




import datatable as dt

import numpy as np




class Metadata:
    """"""

    def __init__(self):
        """"""

        self.DATATABLE = None
        self.COLOR = None

        self.FEATURE = {

            'numCell': 0,
            'numGene': 0,

            'typeSet': [],
            'sourceSet': [],

            'color': []

        }


    def formatData(self, dataDir):
        """"""

        self.DATATABLE = dt.fread(dataDir + '/meta.tsv', nthreads=8)
        self.COLOR = dt.fread(dataDir + '/color.tsv', nthreads=8)

        self.FEATURE['numCell'] = self.DATATABLE.nrows
        self.FEATURE['numGene'] = self.DATATABLE.ncols - 6

        self.FEATURE['typeSet'] = sorted(set(self.DATATABLE['TYPE'].to_list()[0]))
        self.FEATURE['sourceSet'] = sorted(set(self.DATATABLE['SOURCE'].to_list()[0]))