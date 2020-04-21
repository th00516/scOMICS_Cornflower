#!/usr/bin/env python3




import numpy as np
from datatable import f




class Parser:
    """"""

    def __init__(self, metadataObj):
        """"""

        self.METADATA = metadataObj


    def compareFields(self, fieldName1, fieldName2):
        """"""

        if fieldName1 + '/' + fieldName2 not in self.METADATA.DATATABLE.keys():

            posOrNeg = self.METADATA.DATATABLE[fieldName1].to_numpy() * self.METADATA.DATATABLE[fieldName2].to_numpy()
            posOrNeg[posOrNeg > 0] = 1
            
            self.METADATA.DATATABLE[fieldName1 + '/' + fieldName2] = posOrNeg