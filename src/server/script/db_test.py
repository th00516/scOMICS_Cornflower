#!/usr/bin/env python3


import sys
import zlib

from time import time, localtime, strftime
from mysql.connector import connect




def autoGenerateSeqDataIdentity(seqType):
        """"""

        seqDataFlagTemplate = ['', '', '']

        seqDataFlagTemplate[0] = '%X' % int(strftime("%y", localtime(time())))
        seqDataFlagTemplate[1] = '%X' % int(strftime("%m", localtime(time())))

        seqDataFlagTemplate[2] = {

            'WGS':           '0',
            'RNASeq':        '1',
            'ATACSeq':       '2',
            'HiCSeq':        '3',
            'BisulfiteSeq':  '4',

        }

        return seqDataFlagTemplate[0] + seqDataFlagTemplate[1] + seqDataFlagTemplate[2][seqType]

tableName = autoGenerateSeqDataIdentity('RNASeq')




seqDataDB = connect(

    host='localhost',
    user='yuhao',
    passwd='#92064rmf',
    database='cornflowerDB',

)

dbCursor = seqDataDB.cursor()

dbCursor.execute(

    'create table if not exists `' + tableName + '` (' + \
    '`identity` char(7) not null primary key, ' + \
    '`description` text, ' + \
    '`usedCell` longtext not null, ' + \
    '`usedGene` mediumtext not null, ' + \
    '`involvedStudy` text, ' + \
    '`type` varchar(16) not null, ' + \
    '`seqMethod` varchar(16) not null, ' + \
    '`libMethod` varchar(16) not null, ' + \
    '`numberOfCell` int unsigned not null)' + \
    'engine=InnoDB charset=utf8 row_format=compressed key_block_size=8'

)



dbCursor.execute('select `identity` from `' + tableName + '` order by `identity` desc limit 1')

lastRecord = dbCursor.fetchone()
recordName = ''

if lastRecord is not None:

    recordName = tableName + '%03X' % (int(lastRecord[0][4:], 16) + 1)

else:

    recordName = tableName + '000'


dbCursor.execute(

    'insert into `' + tableName + '` set ' + \
    '`identity` = "' + recordName + '",' + \
    '`description` = "ADSFASDFASDFASAD",' + \
    '`usedCell` = "C1,C2,C3",' + \
    '`usedGene` = "G1,G2,G3",' + \
    '`involvedStudy` = "S1",' + \
    '`type` = "RNASeq",' + \
    '`seqMethod` = "3Seq",' + \
    '`libMethod` = "iDrop",' + \
    '`numberOfCell` = 1000'

)

seqDataDB.commit()