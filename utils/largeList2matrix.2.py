#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-15
"""


from sys import (argv, stderr)
from os.path import basename
from enum import Enum
from gzip import open
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


def largeList2matrix(largeList_path, flag):
    """"""
    prefix = str(basename(largeList_path)).split('.')[0]

    row_arr = set()
    col_arr = set()

    with open(prefix + '.b_mat', 'wb') as OFH:
        with open(largeList_path, 'rb') as IFH:
            IFH.readline()
            IFH.readline()

            max_row, max_col, _ = IFH.readline().decode().split()
            max_row = int(max_row)
            max_col = int(max_col)

            OFH.write(bytes((max_col // 256 ** 2,)))
            OFH.write(bytes((max_col % 256 ** 2 // 256 ** 1,)))
            OFH.write(bytes((max_col % 256 ** 2 % 256 ** 1 // 256 ** 0,)))

            n = 1
            frameBuf = bytearray(max_col * 2)
            buffer = bytearray(IFH.read(268435456))  # IO buffer = 256M

            while buffer:
                while not buffer.endswith(b'\n'):
                    buffer.extend(bytearray(IFH.read(1)))

                for row, col, val in list(char.split(asarray(buffer.decode().split('\n')[:-1]))):
                    row = int(row)
                    col = int(col)
                    val = int(float(val))

                    val = 256 ** 2 if val > 256 ** 2 else val

                    val_h = val // 256 ** 1
                    val_l = val % 256 ** 1 // 256 ** 0

                    if flag == 1:
                        row_arr.add(('FE%06d' % row, row))
                        col_arr.add(('SA%08d' % col, col))

                    if row > max_row or col > max_col:
                        print('Coordinates out of range in r' + str(row) + 'c' + str(col) + '.', file=stderr)
                        continue

                    if row > n:
                        OFH.write(frameBuf)

                        n += 1
                        frameBuf = bytearray(max_col * 2)

                    frameBuf[(col - 1) * 2] = val_h
                    frameBuf[(col - 1) * 2 + 1] = val_l

                buffer = bytearray(IFH.read(268435456))

            OFH.write(frameBuf)

    if flag == 1:
        row_arr = sorted(row_arr, key=lambda x: x[1])
        col_arr = sorted(col_arr, key=lambda x: x[1])
        store_info(prefix, tuple(row_arr), tuple(col_arr))


def search_exp_value(matirx_path, row, col):
    """"""
    with open(matirx_path, 'rb') as IFH:
        max_col = int(ord(IFH.read(1))) * 256 ** 2 + \
                  int(ord(IFH.read(1))) * 256 ** 1 + \
                  int(ord(IFH.read(1))) * 256 ** 0

        IFH.seek(3 + ((row - 1) * max_col + (col - 1)) * 2, 0)
        val = int(ord(IFH.read(1))) * 256 ** 1 + int(ord(IFH.read(1))) * 256 ** 0
        print('%d\t%d\t%.2e' % (row, col, val))


if __name__ == '__main__':
    if argv[1] == 'trans':
        class flags(Enum):
            nosql = 0
            mysql = 1

        largeList2matrix(argv[2], flags.nosql.value)

    elif argv[1] == 'show':
        search_exp_value(argv[2], int(argv[3]), int(argv[4]))

    else:
        print('Bad command.', file=stderr)
