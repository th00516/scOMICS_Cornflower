#!/usr/bin/env python3


import sys
from mysql.connector import connect


class dataModel:

    def __init__(self):

        self.option = {

            'dataQualityLevel': ['low', 'high', 'ref'],

            'studyType': ['RNA-Seq', 'DNA-Seq', 'ATAC-Seq']
            'seqMethod': ['full-length', '5-terminal', '3-terminal'],
            'libMethod': ['iDrop', '10x'],

        }

        self.sampleObj = {

            'identity': '',

            'species': '',
            'sex': '',
            'age': '',
            'tissue': '',
            'sampleDescription': 0,

        }

        self.dataObj = {

            'identity': '',
            'alias': [],

            # Append sample object here
            'totalUsedSample': [],

            'studyType': '',
            'seqMethod': '',
            'libMethod': '',

            'totalCellNumber': 0,

            'dataQualityLevel': '',

        }

        self.runObj = {

            'identity': '',

            'usedData': '',
            'usedSampleInData': [],

            'usedCellNumber': 0,

            'runningParameter': '',

            'clusterNumber': 0,
            'cellNumberInEachCluster': [],
            'markerGeneInEachCluster': [[]],

            'expSpan': [0, 0],
            'expSpanInEachCluster': [[]],

        }

        self.dbObj = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflower',

        )

    @staticmethod
    def autoGenerateSampleIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateDataIdentity():
        """"""

        pass

    def parseInputFile(self, sampleFiles):
        """"""

        for sampleFile in sampleFiles:

            pass

    def exportDataToDB(self):
        """"""

        dbCursor = self.dbObj.cursor()

    def manageDB(self):
        """"""

        dbAdminCursor = self.dbObj.cursor()
