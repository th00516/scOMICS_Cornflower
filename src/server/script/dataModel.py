#!/usr/bin/env python3


import sys
import mysql.connector


class dataModel:

    def __init__(self):

        self.__option = {

            'dataQualityLevel': ['low', 'high', 'ref'],
            'libMethod': ['iDrop', '10x'],
            'seqMethod': ['full-length', '3-terminal'],

        }

        self.model = {
            'identity': '',
            'alias': [],

            'dataQualityLevel': self.__option['dataQualityLevel'][0],

            'sampleInfo': {

                'species': [],
                'tissue': [],

            },

            'dataInfo': {

                'libMethod': self.__option['libMethod'][0],
                'seqMethod': self.__option['seqMethod'][1],

            },

            'clusterNumber': 0,
            'clusterMarkerGene': [

            ],

            'cellNumber': 0,
            'cellNumberInCluster': [

            ],

            'expSpan': [0, 0],
            'expSpanInCluster': [

            ]
        }

    @staticmethod
    def autoGenerateIdentity(idPool):
        """"""

        pass

    def parseInputFile(self, sampleFile):
        """"""

        pass

    def exportDB(self):
        """"""

        pass
