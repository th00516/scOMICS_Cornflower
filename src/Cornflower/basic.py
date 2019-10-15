#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-08
"""


from gzip import open
from cv2 import (imdecode, imencode,
                 IMREAD_COLOR, IMWRITE_PNG_BILEVEL)
from numpy import (asarray,
                   uint8)
from pandas import read_csv
from mysql.connector import connect


def expression_matrix_encoding(exp_mat, table):
    """"""
    exp_img = read_csv(exp_mat, compression='gzip', header=0, index_col=0)
    exp_img_row = exp_img.index.to_list()
    exp_img_col = exp_img.columns.to_list()
    exp_img_val = exp_img.to_numpy()

    with open(exp_mat + '.png.gz', 'wb') as exp_img_FH:
        exp_img_FH.write(imencode('.png', exp_img_val, [IMWRITE_PNG_BILEVEL, 1])[1])

    config = {'host': '127.0.0.1',
              'user': 'yuhao',
              'password': '#92064rmf',
              'port': 3306,
              'database': 'cornflowerDB',
              'charset': 'utf8'
              }

    connector = connect(**config)
    cursor = connector.cursor()

    sql_create_table_row = ' '.join(('CREATE TABLE IF NOT EXISTS',
                                     '`' + table + '.row` ('
                                                   '`row` VARCHAR(32) NOT NULL PRIMARY KEY, '
                                                   '`coor` INT UNSIGNED NOT NULL'
                                                   ') ENGINE=INNODB DEFAULT CHARSET=utf8;'))
    sql_create_table_col = ' '.join(('CREATE TABLE IF NOT EXISTS',
                                     '`' + table + '.col` ('
                                                   '`col` VARCHAR(32) NOT NULL PRIMARY KEY,'
                                                   '`coor` INT UNSIGNED NOT NULL'
                                                   ') ENGINE=INNODB DEFAULT CHARSET=utf8;'))

    cursor.execute(sql_create_table_row)
    cursor.execute(sql_create_table_col)

    sql_insert_row = ' '.join(('INSERT INTO', '`' + table + '.row` (`row`, `coor`) VALUES (%s, %s);'))
    sql_insert_col = ' '.join(('INSERT INTO', '`' + table + '.col` (`col`, `coor`) VALUES (%s, %s);'))

    exp_img_row = tuple(zip(exp_img_row, range(0, len(exp_img_row))))
    exp_img_col = tuple(zip(exp_img_col, range(0, len(exp_img_col))))

    cursor.executemany(sql_insert_row, exp_img_row)
    cursor.executemany(sql_insert_col, exp_img_col)

    sql_index_row = ' '.join(('CREATE UNIQUE INDEX', '`' + table + '.row` ON `' + table + '.row` (`row`)'))
    sql_index_col = ' '.join(('CREATE UNIQUE INDEX', '`' + table + '.col` ON `' + table + '.col` (`col`)'))

    cursor.execute(sql_index_row)
    cursor.execute(sql_index_col)

    connector.commit()


def expression_matrix_decoding(exp_img):
    """"""
    with open(exp_img, 'rb') as exp_img_FH:
        exp_mat = imdecode(asarray(bytearray(exp_img_FH.read()), dtype=uint8), IMREAD_COLOR)

    return exp_mat
