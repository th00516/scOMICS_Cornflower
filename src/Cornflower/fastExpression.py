#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-08
"""


def fast_extract_expression(exp_mat, row, col):
    """"""
    exp_val1, exp_val2, exp_val3 = exp_mat[row, col, :]

    return exp_val1, exp_val2, exp_val3
