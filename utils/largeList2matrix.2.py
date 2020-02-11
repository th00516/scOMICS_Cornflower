#!/usr/bin/env python3


from sys import (argv, stderr)
from os.path import basename
from gzip import (open as gopen, compress, decompress)
from numpy import (asarray, char)
from mysql.connector import connect


class largeList:
    def __init__(self, *args, **kwargs):
        """"""
        pass
