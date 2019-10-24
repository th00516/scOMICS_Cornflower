#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-15
"""


from sys import (argv, stderr)
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
            max_row, max_col, _ = IFH.readline().decode().split()
            max_row = int(max_row)
            max_col = int(max_col)

            ####################################################
            # Generate a frame for accommodating all the value #
            ####################################################
            new_line = ''.join(('0.00e+00,' * (max_col - 1), '0.00e+00\n')).encode()
            ####################################################

            frameBuf = BytesIO(new_line)

            buffer = bytearray(IFH.read(268435456))  # IO buffer = 256M

            n = 1
            while buffer:
                while not buffer.endswith(b'\n'):
                    buffer.extend(bytearray(IFH.read(1)))

                for row, col, val in list(char.split(asarray(buffer.decode().split('\n')[:-1]))):
                    row = int(row)
                    col = int(col)
                    val = val.encode()

                    if row > max_row or col > max_col:
                        print('Coordinates out of range in r' + str(row) + 'c' + str(col) + '.', file=stderr)
                        continue

                    if row > n:
                        frameBuf.seek(0, SEEK_SET)
                        OFH.write(gcompress(frameBuf.read()))
                        frameBuf.close()

                        n += 1
                        frameBuf = BytesIO(new_line)

                    frameBuf.seek((col - 1) * 9, SEEK_SET)
                    frameBuf.write(val)

                buffer = bytearray(IFH.read(268435456))

            frameBuf.seek(0, SEEK_SET)
            OFH.write(gcompress(frameBuf.read()))
            frameBuf.close()


if __name__ == '__main__':
    largeList2matrix(argv[1])
