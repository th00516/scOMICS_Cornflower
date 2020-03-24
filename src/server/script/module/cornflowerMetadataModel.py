#!/usr/bin/env python3


import sys

from mysql.connector import connect


class cornflowerMetadataModel:

    def __init__(self):

        # metadata model #
        self.seqDataModel = {

            'identity': '',

            'usedSample': '',
            'usedGene': '',
            'involvedStudy': '',

            'type': '',
            'seqMethod': '',
            'libMethod': '',

            'numberOfCell': '',

        }

        self.geneInfoModel = {

            'identity': '',
            'alias': '',
            'description': '',

            'species': '',

        }

        self.cellInfoModel = {

            'identity': '',
            'alias': '',
            'description': '',

            'species': '',
            'sex': '',
            'source': '',
            'samplingDate': '',

        }

        self.studyInfoModel = {

            'identity': '',
            'alias': '',
            'description': '',

            'generatedData': '',

            'organization': '',
            'publication': '',

        }

        self.RNASeqClusterModel = {

            'identity': '',

            'usedData': '',
            'clusterMethod': '',
            'clusterParameter': '',

            'numberOfCluster': '',
            'cellNumberInEachCluster': '',
            'markerGeneInEachCluster': '',

            'expSpan': '',
            'expSpanInEachCluster': '',

        }

        self.ATACSeqClusterModel = {

            'identity': '',

            'usedData': '',
            'clusterMethod': '',
            'clusterParameter': '',

            'numberOfCluster': '',
            'cellNumberInEachCluster': '',
            'markerGeneInEachCluster': '',

            ## ... ##

        }

        # DB handler #
        self.seqDataDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerRNASeqData',

        )

        self.geneInfoDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerGeneInfo',

        )

        self.cellInfoDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerCellInfo',

        )

        self.studyInfoDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerStudyInfo',

        )

        self.RNASeqClusterDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerRNASeqCluster',

        )

        self.ATACSeqClusterDB = connect(

            host='localhost',
            user='cornflower',
            passwd='$th00516',
            database='cornflowerATACSeqCluster',

        )

    # static method #
    @staticmethod
    def autoGenerateSeqDataIdentity():
        """"""

        seqDataFlagTemplate = {

            'isRNASeq':     2 ** 0,
            'isATACSeq':    2 ** 1,

            'is3':          2 ** 3,
            'is5':          2 ** 4,
            'isFull':       2 ** 5,

            ''

            'isIDrop':      2 ** 7,
            'is10XData':    2 ** 8,

        }

    @staticmethod
    def autoGenerateGeneInfoIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateCellInfoIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateStudyInfoIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateRNASeqClusterIdentity():
        """"""

        pass

    @staticmethod
    def autoGenerateATACSeqClusterIdentity():
        """"""

        pass

    # headle DB #
    def handleSeqDataDB(self):
        """"""

        dbCursor = self.seqDataDB.cursor()

    def handleGeneInfoDB(self):
        """"""

        dbCursor = self.geneInfoDB.cursor()

    def handleCellInfoDB(self):
        """"""

        dbCursor = self.cellInfoDB.cursor()

    def handleStudyInfoDB(self):
        """"""

        dbCursor = self.studyInfoDB.cursor()

    def handleRNASeqClusterDB(self):
        """"""

        dbCursor = self.RNASeqClusterDB.cursor()

    def handleATACSeqClusterDB(self):
        """"""

        dbCursor = self.ATACSeqClusterDB.cursor()

    # implement method #
    def parseInputFile(self, sampleFiles):
        """"""

        for sampleFile in sampleFiles:

            pass
