#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-15
"""


from sys import (argv, stderr)
from os.path import basename
from gzip import (open as gopen, compress, decompress)
from numpy import (asarray, char)
from mysql.connector import connect


config = {'host': 'localhost',
          'user': 'yuhao',
          'password': '#92064rmf',
          'port': 3306,
          'database': 'cornflowerDB',
          'charset': 'utf8'
          }


def store_info(prefix, row_arr, col_arr):
    """"""
    connector = connect(**config)
    cursor = connector.cursor()

    sql_create_table_row = 'CREATE TABLE IF NOT EXISTS `' + \
                           prefix + \
                           '.row` (' \
                           '`ID` INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY, ' \
                           '`FE1` TEXT NOT NULL, ' \
                           '`FE2` TEXT NOT NULL, ' \
                           '`FE3` TEXT NOT NULL, ' \
                           '`ROW_LEN` INT UNSIGNED NOT NULL, ' \
                           '`ROW_LOC` INT UNSIGNED NOT NULL' \
                           ') ENGINE=INNODB DEFAULT CHARSET=utf8;'
    sql_create_table_col = 'CREATE TABLE IF NOT EXISTS `' + \
                           prefix + \
                           '.col` (' \
                           '`ID` INT UNSIGNED AUTO_INCREMENT NOT NULL PRIMARY KEY, ' \
                           '`SA1` TEXT NOT NULL, ' \
                           '`SA2` TEXT NOT NULL, ' \
                           '`SA3` TEXT NOT NULL, ' \
                           '`SA4` TEXT NOT NULL, ' \
                           '`COL_LOC` INT UNSIGNED NOT NULL' \
                           ') ENGINE=INNODB DEFAULT CHARSET=utf8;'

    cursor.execute(sql_create_table_row)
    cursor.execute(sql_create_table_col)

    sql_insert_row = 'INSERT INTO `' + prefix + '.row` (`FE1`, `FE2`, `FE3`, `ROW_LEN`, `ROW_LOC`) ' \
                                                'VALUES (%s, %s, %s, %s, %s)'
    sql_insert_col = 'INSERT INTO `' + prefix + '.col` (`SA1`, `SA2`, `SA3`, `SA4`, `COL_LOC`) ' \
                                                'VALUES (%s, %s, %s, %s, %s)'

    cursor.executemany(sql_insert_row, row_arr)
    cursor.executemany(sql_insert_col, col_arr)

    connector.commit()


def get_info(prefix, row, col):
    """"""
    connector = connect(**config)
    cursor = connector.cursor()

    row = '%06x' % row
    col = '%08x' % col

    sql_select_row = 'SELECT `ROW_LEN`, `ROW_LOC` from `' + prefix + '.row` WHERE ' \
                                                           '`FE1` = "' + row[:2] + '" and ' \
                                                           '`FE2` = "' + row[2:4] + '" and ' \
                                                           '`FE3` = "' + row[4:] + '";'
    sql_select_col = 'SELECT `COL_LOC` from `' + prefix + '.col` WHERE ' \
                                                           '`SA1` = "' + col[:2] + '" and ' \
                                                           '`SA2` = "' + col[2:4] + '" and ' \
                                                           '`SA3` = "' + col[4:6] + '" and ' \
                                                           '`SA4` = "' + col[6:] + '";'

    cursor.execute(sql_select_row)
    row_len, feature_loc = cursor.fetchone()

    cursor.execute(sql_select_col)
    sample_loc = cursor.fetchone()[0]

    return row_len, feature_loc, sample_loc


def largeList2matrix(largeList_path):
    """"""
    prefix = str(basename(largeList_path)).split('.')[0]

    row_arr = set()
    col_arr = set()

    with open(prefix + '.b_mat', 'wb') as OFH:
        with gopen(largeList_path, 'rb') as IFH:
            IFH.readline()
            IFH.readline()

            max_row, max_col, _ = IFH.readline().decode().split()
            max_row = int(max_row)
            max_col = int(max_col)

            fe_id = 1
            sa_id = 1
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

                    if row > max_row or col > max_col:
                        print('Coordinates out of range in r' + str(row) + 'c' + str(col) + '.', file=stderr)
                        continue

                    while row - fe_id > 0:
                        l0 = OFH.tell()
                        OFH.write(compress(frameBuf))
                        l1 = OFH.tell()

                        row_hex = '%06x' % fe_id
                        row_arr.add((row_hex[:2], row_hex[2:4], row_hex[4:], l1 - l0, l0))

                        fe_id += 1
                        frameBuf = bytearray(max_col * 2)

                    while col - sa_id > 0:
                        col_hex = '%08x' % sa_id
                        col_arr.add((col_hex[:2], col_hex[2:4], col_hex[4:6], col_hex[6:], (sa_id - 1) * 2))

                        sa_id += 1

                    frameBuf[(col - 1) * 2] = val_h
                    frameBuf[(col - 1) * 2 + 1] = val_l

                buffer = bytearray(IFH.read(268435456))

            l0 = OFH.tell()
            OFH.write(compress(frameBuf))
            l1 = OFH.tell()

            row_hex = '%06x' % fe_id
            row_arr.add((row_hex[:2], row_hex[2:4], row_hex[4:], l1 - l0, l0))

    row_arr = sorted(row_arr, key=lambda x: int(''.join(x[0:3]), 16))
    col_arr = sorted(col_arr, key=lambda x: int(''.join(x[0:4]), 16))
    store_info(prefix, tuple(row_arr), tuple(col_arr))


def find_exp_value(matirx_path, feature, sample):
    """"""
    prefix = str(basename(matirx_path)).split('.')[0]
    row_len, feature_loc, sample_loc = get_info(prefix, feature, sample)

    with open(matirx_path, 'rb') as IFH:
        IFH.seek(feature_loc, 0)
        line = decompress(IFH.read(row_len))

        exp_value = line[sample_loc] * 256 ** 1 + line[sample_loc + 1] * 256 ** 0

        print(feature, sample, '%.2e' % exp_value)


if __name__ == '__main__':
    if argv[1] == 'conv':
        largeList2matrix(argv[2])

    elif argv[1] == 'find':
        find_exp_value(argv[2], int(argv[3]), int(argv[4]))

    else:
        print('Bad command.', file=stderr)
