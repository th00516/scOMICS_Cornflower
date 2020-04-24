#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import sys




class Config:
    """"""

    def __init__(self):
        """"""

        self.CONF = {}


    def parseConf(self, confFile):
        """"""

        self.CONF.update({'options': []})

        with open(confFile, 'rt') as CIN:

            for l in CIN:

                if l[0] == '#':
                    continue

                l = l.split()

                if l[0].strip() not in self.CONF:

                    self.CONF.update({l[0]: l[1:]})

                if l[0] == 'data_set':
                    self.CONF['options'] = [{'label': _, 'value': _} for _ in l[1:]]