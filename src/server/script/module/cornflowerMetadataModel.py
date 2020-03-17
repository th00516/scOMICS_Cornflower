#!/usr/bin/env python3


import sys
from mysql.connector import connect


class cornflowerMetadataModel:

    def __init__(self):

        # metadata model #
        self.projModel = {

            'identity': '',
            'alias': [],

            'sample': [],

        }

        self.sampleModel = {

            'identity': '',
            'alias': [],

            'species': '',
            'sex': '',
            'tissue': '',
            'date': '',
            'description': '',

            'data': [],

        }

        self.geneInfoModel = {

            'identity': '',
            'alias': [],

            'species': '',
            'description': '',

        }

        self.RNASeqDataModel = {

            'identity': '',
            'alias': [],

            'totalUsedSample': [],

            'seqMethod': '',
            'libMethod': '',

            'sampleNumber': 0,

        }

        # self.ATACSeqDataModel = {

        #     'identity': '',
        #     'alias': [],

        #     'totalUsedSample': [],

        #     'seqMethod': '',
        #     'libMethod': '',

        #     'sampleNumber': 0,

        # }

        self.RNASeqClusterModel = {

            'identity': '',
            'alias': '',

            'usedSample': [],
            'usedSampleNumber': 0,

            'parameter': '',

            'clusterNumber': 0,

            'sampleNumberInEachCluster': [],
            'markerGeneInEachCluster': [[]],

            'expSpan': [0, 0],
            'expSpanInEachCluster': [[]],

        }

        # self.ATACSeqClusterModel = {

        #     'identity': '',
        #     'alias': '',

        #     'usedSample': [],
        #     'usedSampleNumber': 0,

        #     'parameter': '',

        #     ## ... ##

        # }

        self.projDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerProj',

        )

        self.sampleDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerSample',

        )

        self.geneInfoDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerGeneInfo',

        )

        self.RNASeqDataDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerRNASeqData',

        )

        # self.ATACSeqDataDB = connect(

        #     host='localhost',
        #     user='cornflower',
        #     passwd='$th00516',
        #     database='cornflowerATACSeqData',

        # )

        self.RNASeqClusterDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerRNASeqCluster',

        )

        # self.ATACSeqClusterDB = connect(

        #     host='localhost',
        #     user='cornflower',
        #     passwd='$th00516',
        #     database='cornflowerATACSeqCluster',

        # )

    # static method #
    @staticmethod
    def autoGenerateProjIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateSampleIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateGeneInfoIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateRNASeqDataIdentity():
        """"""

        pass

    # @staticmethod
    # def autoGenerateATACSeqDataIdentity():
    #     """"""

    #     pass

    @staticmethod
    def autoGenerateRNASeqClusterIdentity():
        """"""

        pass

    # @staticmethod
    # def autoGenerateATACSeqClusterIdentity():
    #     """"""

    #     pass

    # headle DB #
    def handleProjDB(self):
        """"""

        dbCursor = self.projDB.cursor()

    def handleSampleDB(self):
        """"""

        dbCursor = self.sampleDB.cursor()

    def handleGeneInfoDB(self):
        """"""

        dbCursor = self.geneInfoDB.cursor()

    def handleRNASeqDataDB(self):
        """"""

        dbCursor = self.RNASeqDataDB.cursor()

    # def handleATACSeqDataDB(self):
    #     """"""

    #     dbCursor = self.ATACSeqDataDB.cursor()

    def handleRNASeqClusterDB(self):
        """"""

        dbCursor = self.RNASeqClusterDB.cursor()

    # def handleATACSeqClusterDB(self):
    #     """"""

    #     dbCursor = self.ATACSeqClusterDB.cursor()

    # implement method #
    def parseInputFile(self, sampleFiles):
        """"""

        for sampleFile in sampleFiles:

            pass
