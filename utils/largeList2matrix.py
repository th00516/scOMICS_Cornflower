#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-15
"""


from sys import argv
from os.path import basename
from gzip import (open as gopen, compress as gcompress)
from lz4.block import (compress as lcompress, decompress as ldecompress)
from numpy import (asarray, char)


def largeList2matrix(largeList_path):
    """"""
    with open(basename(largeList_path) + '.csv.gz', 'w+b') as OFH:
        with gopen(largeList_path, 'rb') as IFH:
            IFH.readline()
            IFH.readline()
            max_row, max_col, _ = IFH.readline().decode().split()
            max_col = int(max_col)

            ####################################################
            # Generate a frame for accommodating all the value #
            ####################################################
            new_line = lcompress(''.join(('0.00e+00,' * (max_col - 1), '0.00e+00\n')).encode())
            ####################################################

            buffer = IFH.read(209715200)  # IO buffer = 200M
            while buffer:
                buffer = buffer.decode()
                while buffer[-1] != '\n':
                    buffer += IFH.read(1).decode()

                n = 1
                frameBuf = ldecompress(new_line).decode().split(',')
                for row, col, val in asarray(list(char.split(asarray(buffer.split('\n')[:-1])))):
                    row = int(row)
                    col = int(col)

                    if row > n:
                        OFH.write(gcompress(''.join(','.join(frameBuf)).encode()))
                        n += 1
                        frameBuf = ldecompress(new_line).decode().split(',')

                    frameBuf[col - 1] = val
                OFH.write(gcompress(''.join(','.join(frameBuf)).encode()))

                buffer = IFH.read(209715200)


if __name__ == '__main__':
    largeList2matrix(argv[1])
