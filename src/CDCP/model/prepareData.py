#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




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

        }


    def formatData(self, dataDir):
        """"""

        self.DATATABLE = dt.fread(dataDir + '/meta', nthreads=8)
        self.COLOR = dt.fread(dataDir + '/color', nthreads=8)

        self.FEATURE['geneList'] = self.DATATABLE.keys()[6:self.DATATABLE.ncols]

        self.FEATURE['typeSet'] = sorted(set(self.DATATABLE['TYPE'].to_list()[0]))
        self.FEATURE['sourceSet'] = sorted(set(self.DATATABLE['SOURCE'].to_list()[0]))

        self.FEATURE['posExpRate'] = {
            _: np.nonzero(self.DATATABLE[_].to_numpy())[0].size / self.DATATABLE.nrows * 100
            for _ in self.FEATURE['geneList']
        }