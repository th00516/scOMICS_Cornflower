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
from mysql.connector import connect


def store_info(prefix, row_arr, col_arr):
    """"""
    config = {'host': 'localhost',
              'user': 'yuhao',
              'password': '#92064rmf',
              'port': 3306,
              'database': 'cornflowerDB',
              'charset': 'utf8'
              }

    connector = connect(**config)
    cursor = connector.cursor()

    sql_create_table_row = 'CREATE TABLE IF NOT EXISTS `' + \
                           prefix + \
                           '.row` (' \
                           '`id` INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY, ' \
                           '`gene` TEXT NOT NULL, ' \
                           '`row` INT UNSIGNED NOT NULL' \
                           ') ENGINE=INNODB DEFAULT CHARSET=utf8;'
    sql_create_table_col = 'CREATE TABLE IF NOT EXISTS `' + \
                           prefix + \
                           '.col` (' \
                           '`id` INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY, ' \
                           '`cell` TEXT NOT NULL, ' \
                           '`col` INT UNSIGNED NOT NULL' \
                           ') ENGINE=INNODB DEFAULT CHARSET=utf8;'

    cursor.execute(sql_create_table_row)
    cursor.execute(sql_create_table_col)

    sql_insert_row = 'INSERT INTO `' + prefix + '.row` (`gene`, `row`) VALUES (%s, %s)'
    sql_insert_col = 'INSERT INTO `' + prefix + '.col` (`cell`, `col`) VALUES (%s, %s)'

    cursor.executemany(sql_insert_row, row_arr)
    cursor.executemany(sql_insert_col, col_arr)

    connector.commit()


def largeList2matrix(largeList_path):
    """"""
    prefix = str(basename(largeList_path)).split('.')[0]

    row_arr = set()
    col_arr = set()

    with open(prefix + '.csv.gz', 'wb') as OFH:
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

            n = 1
            frameBuf = BytesIO(new_line)

            buffer = bytearray(IFH.read(268435456))  # IO buffer = 256M

            while buffer:
                while not buffer.endswith(b'\n'):
                    buffer.extend(bytearray(IFH.read(1)))

                for row, col, val in list(char.split(asarray(buffer.decode().split('\n')[:-1]))):
                    row = int(row)
                    col = int(col)
                    val = val.encode()

                    row_arr.add(('FE%07d' % row, row))
                    col_arr.add(('SA%07d' % col, col))

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

    row_arr = sorted(row_arr, key=lambda x: x[1])
    col_arr = sorted(col_arr, key=lambda x: x[1])
    store_info(prefix, tuple(row_arr), tuple(col_arr))


if __name__ == '__main__':
    largeList2matrix(argv[1])
