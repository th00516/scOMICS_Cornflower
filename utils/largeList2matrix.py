#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-15
"""


from sys import argv
from os.path import basename
from os import SEEK_SET
from gzip import (open as gopen, compress as gcompress)
from io import BytesIO
from numpy import (asarray, char)


def largeList2matrix(largeList_path):
    """"""
    with open(basename(largeList_path) + '.csv.gz', 'wb') as OFH:
        with gopen(largeList_path, 'rb') as IFH:
            IFH.readline()
            IFH.readline()
            _, max_col, _ = IFH.readline().decode().split()
            max_col = int(max_col)

            ####################################################
            # Generate a frame for accommodating all the value #
            ####################################################
            new_line = ''.join(('0.00e+00,' * (max_col - 1), '0.00e+00\n')).encode()
            ####################################################

            frameBuf = BytesIO(new_line)

            buffer = IFH.read(209715200)  # IO buffer = 200M
            while buffer:
                while buffer[-1] != 10:
                    buffer += IFH.read(1)

                n = 1
                for row, col, val in list(char.split(asarray(buffer.decode().split('\n')[:-1]))):
                    row = int(row)
                    col = int(col)

                    if row > n:
                        frameBuf.seek(0, SEEK_SET)
                        OFH.write(gcompress(frameBuf.read()))
                        frameBuf.close()

                        n += 1
                        frameBuf = BytesIO(new_line)

                    frameBuf.seek((col - 1) * 9, SEEK_SET)
                    frameBuf.write(val.encode())

                buffer = IFH.read(209715200)

            frameBuf.seek(0, SEEK_SET)
            OFH.write(gcompress(frameBuf.read()))
            frameBuf.close()


if __name__ == '__main__':
    largeList2matrix(argv[1])
