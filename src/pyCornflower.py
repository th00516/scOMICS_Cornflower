#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-08
"""


from sys import argv
from os.path import basename

from Cornflower.basic import expression_matrix_encoding
from Cornflower.basic import expression_matrix_decoding
from Cornflower.fastExpression import fast_extract_expression


if __name__ == '__main__':
    if argv[1] == 'format':
        expression_matrix_encoding(argv[2], basename(argv[2]).split('.')[0])

    if argv[1] == 'search':
        exp_matrix = expression_matrix_decoding(argv[2] + '.png.gz')

        exp_value = fast_extract_expression(exp_matrix, basename(argv[2]).split('.')[0], argv[3], argv[4])

        print(exp_value)
