#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-08
"""


from mysql.connector import connect
from numpy import (asarray, int)


def fast_extract_expression(exp_mat, table, sample, feature):
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

    cursor.execute('SELECT `row`, `coor` FROM `' + table + '.row`;')
    row = asarray(cursor.fetchall())

    cursor.execute('SELECT `col`, `coor` FROM `' + table + '.col`;')
    col = asarray(cursor.fetchall())

    connector.commit()

    row = int(row[row[:, 0] == feature, 1])
    col = int(col[col[:, 0] == sample, 1])

    exp_val1, exp_val2, exp_val3 = exp_mat[row, col, :]

    return exp_val1, exp_val2, exp_val3
