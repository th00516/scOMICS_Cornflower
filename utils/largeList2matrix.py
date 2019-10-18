#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-15
"""


from sys import argv
from os.path import basename
from gzip import open as gopen
from lzma import compress, decompress
from numpy import (asarray, char)


def largeList2matrix(largeList_path):
    """"""
    with open(basename(largeList_path) + '.csv.gz', 'w+b') as OFH:
        with gopen(largeList_path, 'rb') as IFH:
            IFH.readline()
            IFH.readline()
            max_row, max_col, _ = IFH.readline().decode(encoding='utf-8').split()
            max_col = int(max_col)

            ####################################################
            # Generate a frame for accommodating all the value #
            ####################################################
            new_line = compress(('0.00e+00,' * (max_col - 1) + '0.00e+00\n').encode(encoding='utf-8'))

            buffer = IFH.read(104857600)  # buffer = 100M
            while buffer:
                buffer = buffer.decode(encoding='utf-8')
                while buffer[-1] != '\n':
                    buffer += IFH.read(1).decode(encoding='utf-8')

                n = 1
                frameBuf = decompress(new_line).decode(encoding='utf-8').split(',')
                for row, col, val in asarray(list(char.split(asarray(buffer.split('\n')[:-1])))):
                    row = int(row)
                    col = int(col)

                    if row > n:
                        OFH.write(compress(''.join(','.join(frameBuf)).encode(encoding='utf-8')))
                        n += 1
                        frameBuf = decompress(new_line).decode(encoding='utf-8').split(',')

                    frameBuf[col - 1] = val
                OFH.write(compress(''.join(','.join(frameBuf)).encode(encoding='utf-8')))

                buffer = IFH.read(104857600)
            ####################################################


if __name__ == '__main__':
    largeList2matrix(argv[1])
