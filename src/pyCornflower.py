#!/usr/bin/env python3


"""
AUTHOR: Hao Yu (yuhao@genomics.cn)
DATE:   2019-10-08
"""


from sys import argv

from Cornflower.basic import expression_matrix_encoding
from Cornflower.basic import expression_matrix_decoding
from Cornflower.fastExpression import fast_extract_expression


if __name__ == '__main__':
    expression_matrix_encoding(argv[1])
    exp_matrix = expression_matrix_decoding(argv[1] + '.png.gz')

    exp_value = fast_extract_expression(exp_matrix, int(argv[2]) - 1, int(argv[3]) - 1)

    print(exp_value)
