#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-08
"""


from mysql.connector import connect


def fast_extract_expression(exp_mat, table, sample, feature):
    """"""
    config = {'host': '127.0.0.1',
              'user': 'yuhao',
              'password': '#92064rmf',
              'port': 3306,
              'database': 'cornflowerDB',
              'charset': 'utf8'
              }

    connector = connect(**config)
    cursor = connector.cursor()

    cursor.execute('SELECT `coor` FROM `' + table + '.row` WHERE `row`="' + feature + '";')
    row = int(cursor.fetchone()[0])

    cursor.execute('SELECT `coor` FROM `' + table + '.col` WHERE `col`="' + sample + '";')
    col = int(cursor.fetchone()[0])

    exp_val1, exp_val2, exp_val3 = exp_mat[row, col, :]

    return exp_val1, exp_val2, exp_val3
