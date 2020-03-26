#!/usr/bin/env python3


import sys

from time import time, localtime, strftime
from mysql.connector import connect


class cornflowerMetadataModel:

    def __init__(self):

        # metadata model #
        self.seqDataModel = {

            'identity': '',
            'description': '',

            'usedCell': '',
            'usedGene': '',
            'involvedStudy': '',

            'type': '',
            'seqMethod': '',
            'libMethod': '',

            'numberOfCell': '',

        }

        self.geneInfoModel = {

            'identity': '',
            'description': '',

            'alias': '',

            'species': '',

        }

        self.cellInfoModel = {

            'identity': '',
            'description': '',

            'alias': '',

            'species': '',
            'sex': '',
            'source': '',
            'samplingDate': '',

        }

        self.studyInfoModel = {

            'identity': '',
            'description': '',

            'alias': '',

            'generatedData': '',

            'organization': '',
            'publication': '',

        }

        self.RNASeqClusterModel = {

            'identity': '',
            'description': '',

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
            'description': '',

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
            database='cornflowerSeqData',

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
    def autoGenerateSeqDataIdentity(seqType):
        """"""

        flagTemplate = ['', '', '']

        flagTemplate[0] = '%X' % int(strftime("%y", localtime(time())))
        flagTemplate[1] = '%X' % int(strftime("%m", localtime(time())))

        flagTemplate[2] = {

            'WGS':           '0',
            'RNASeq':        '1',
            'ATACSeq':       '2',
            'HiCSeq':        '3',
            'BisulfiteSeq':  '4',

        }

        return flagTemplate[0] + flagTemplate[1] + flagTemplate[2][seqType]

    @staticmethod
    def autoGenerateGeneInfoIdentity(species):
        """"""

        tmp = species.split(' ')

        flagTemplate = ['', '']

        flagTemplate[0] = tmp[0][:3].upper()
        flagTemplate[1] = tmp[1][:2].upper()

        return flagTemplate[0] + flagTemplate[1]

    @staticmethod
    def autoGenerateCellInfoIdentity():
        """"""

        flagTemplate = ['', '']

        flagTemplate[0] = '%X' % int(strftime("%y", localtime(time())))
        flagTemplate[1] = '%X' % int(strftime("%m", localtime(time())))

        return flagTemplate[0] + flagTemplate[1]

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
    def handleSeqDataDB(self, seqType):
        """"""

        tableName = cornflowerMetadataModel.autoGenerateSeqDataIdentity(seqType)

        dbCursor = self.seqDataDB.cursor()
        dbCursor.execute(

            'create table if not exists `' + tableName + '` (' + \
            '`identity` char(7) not null primary key, ' + \
            '`description` mediumtext, ' + \
            '`usedCell` longtext not null, ' + \
            '`usedGene` mediumtext not null, ' + \
            '`involvedStudy` text, ' + \
            '`type` varchar(16) not null, ' + \
            '`seqMethod` varchar(16) not null, ' + \
            '`libMethod` varchar(16) not null, ' + \
            '`numberOfCell` int not null)' + \
            'engine=InnoDB default charset=utf8 row_format=compressed key_block_size=8'
            
        )

        dbCursor.execute('select `identity` from `' + tableName + '` order by `identity` desc limit 1')

        lastRecord = dbCursor.fetchone()

        if lastRecord is not None:

            self.seqDataModel['identity'] = tableName + '%03X' % (int(lastRecord[0][4:], 16) + 1)

        else:

            self.seqDataModel['identity'] = tableName + '000'

        dbCursor.execute(
            
            'insert into `' + tableName + '` set ' + \

            '`identity` = "' +      self.seqDataModel['identity']       + '",' + \
            '`description` = "' +   self.seqDataModel['description']    + '",' + \
            '`usedCell` = "' +      self.seqDataModel['usedCell']       + '",' + \
            '`usedGene` = "' +      self.seqDataModel['usedGene']       + '",' + \
            '`involvedStudy` = "' + self.seqDataModel['involvedStudy']  + '",' + \
            '`type` = "' +          self.seqDataModel['type']           + '",' + \
            '`seqMethod` = "' +     self.seqDataModel['seqMethod']      + '",' + \
            '`libMethod` = "' +     self.seqDataModel['libMethod']      + '",' + \
            '`numberOfCell` = ' +   self.seqDataModel['numberOfCell']   + ''

        )

        self.seqDataDB.commit()



    def handleGeneInfoDB(self, species):
        """"""

        tableName = cornflowerMetadataModel.autoGenerateGeneInfoIdentity(species)

        dbCursor = self.geneInfoDB.cursor()
        dbCursor.execute(

            'create table if not exists `' + tableName + '` (' + \
            '`identity` char(7) not null primary key, ' + \
            '`description` mediumtext, ' + \
            '`alias` longtext not null, ' + \
            '`species` mediumtext not null) ' + \
            'engine=InnoDB default charset=utf8 row_format=compressed key_block_size=8'
            
        )

        dbCursor.execute('select `identity` from `' + tableName + '` order by `identity` desc limit 1')

        lastRecord = dbCursor.fetchone()

        if lastRecord is not None:

            self.seqDataModel['identity'] = tableName + '%03X' % (int(lastRecord[0][4:], 16) + 1)

        else:

            self.seqDataModel['identity'] = tableName + '000'

        dbCursor.execute(
            
            'insert into `' + tableName + '` set ' + \

            '`identity` = "' +      self.seqDataModel['identity']       + '",' + \
            '`description` = "' +   self.seqDataModel['description']    + '",' + \
            '`usedCell` = "' +      self.seqDataModel['usedCell']       + '",' + \
            '`usedGene` = "' +      self.seqDataModel['usedGene']       + '",' + \
            '`involvedStudy` = "' + self.seqDataModel['involvedStudy']  + '",' + \
            '`type` = "' +          self.seqDataModel['type']           + '",' + \
            '`seqMethod` = "' +     self.seqDataModel['seqMethod']      + '",' + \
            '`libMethod` = "' +     self.seqDataModel['libMethod']      + '",' + \
            '`numberOfCell` = ' +   self.seqDataModel['numberOfCell']   + ''

        )

        self.seqDataDB.commit()

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