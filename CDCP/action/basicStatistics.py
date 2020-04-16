#!/usr/bin/env python3




import numpy as np




class Parser:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj


        self.FIELD_FEATURE = {

            'maxGeneExp': 0,
            'minGeneExp': 0,
            'aveGeneExp': 0,
            'numExpCell': 0,
            'posExpRate': 0

        }


    def getFieldFeature(self, fieldName):
        """"""

        self.FIELD_FEATURE['maxGeneExp'] = self.METADATA.DATATABLE[fieldName].max()[0, 0]
        self.FIELD_FEATURE['minGeneExp'] = self.METADATA.DATATABLE[fieldName].min()[0, 0]
        self.FIELD_FEATURE['aveGeneExp'] = self.METADATA.DATATABLE[fieldName].mean()[0, 0]
        self.FIELD_FEATURE['numExpCell'] = np.nonzero(self.METADATA.DATATABLE[fieldName].to_numpy())[0].size
        self.FIELD_FEATURE['posExpRate'] = self.FIELD_FEATURE['numExpCell'] / self.METADATA.FEATURE['numCell']


    def compareFields(self, fieldName1, fieldName2):
        """"""

        posOrNeg = self.METADATA.DATATABLE[fieldName1].to_numpy() * self.METADATA.DATATABLE[fieldName2].to_numpy()
        posOrNeg[posOrNeg > 0] = 1
        
        self.METADATA.DATATABLE[fieldName1 + '_' + fieldName2] = posOrNeg
