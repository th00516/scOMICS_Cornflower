#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-15
"""


from sys import (argv, stderr)
from os import SEEK_SET
from os.path import basename
from gzip import (open as gopen, compress as gcompress)
# from lzma import (open as lopen, compress as lcompress)
from numpy import (asarray, char)


def largeList2matrix(largeList_path):
    """"""
    with open(basename(largeList_path) + '.mat.gz', 'w+b') as OFH:
        with gopen(largeList_path, 'rb') as IFH:
            IFH.readline()
            IFH.readline()
            max_col, max_row, _ = IFH.readline().decode(encoding='utf-8').split()
            max_col = int(max_col)
            max_row = int(max_row)

            size = max_col * max_row

            ####################################################
            # Generate a frame for accommodating all the value #
            ####################################################
            step_len = 0
            for i in range(1, (size + 1), max_col):
                for j in range(1, (max_col + 1)):
                    frm = gcompress('0.00e+00,'.encode(encoding='utf-8'))
                    if j == max_col:
                        frm = gcompress('0.00e+00\n'.encode(encoding='utf-8'))

                    OFH.write(frm)

                    step_len = len(frm)
            ####################################################

            ############################
            # Fill data into the frame #
            ############################
            buffer = IFH.read(536870912)  # buffer = 512M
            while buffer:
                buffer = buffer.decode(encoding='utf-8')
                while buffer[-1] != '\n':
                    buffer += IFH.read(1).decode(encoding='utf-8')

                buffer = asarray(list(char.split(asarray(buffer.split('\n')[:-1]))))

                for col, row, val in buffer:
                    col = int(col)
                    row = int(row)

                    dat = gcompress((val + ',').encode(encoding='utf-8'))
                    if col == max_col:
                        dat = gcompress((val + '\n').encode(encoding='utf-8'))

                    if len(dat) == step_len:
                        OFH.seek((((row - 1) * max_col + col) - 1) * step_len, SEEK_SET)
                        OFH.write(dat)
                    else:
                        print('Compression failed.', file=stderr)
                        exit(1)

                buffer = IFH.read(536870912)
            ############################


if __name__ == '__main__':
    largeList2matrix(argv[1])
