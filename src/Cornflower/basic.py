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


def expression_matrix_encoding(exp_mat):
    """"""
    exp_img = read_csv(exp_mat, compression='gzip', header=0, index_col=0)
    exp_img_row = ''
    exp_img_col = ''
    exp_img_val = exp_img.values

    with open(exp_mat + '.png.gz', 'wb') as exp_img_FH:
        exp_img_FH.write(imencode('.png', exp_img_val, [IMWRITE_PNG_BILEVEL, 1])[1])


def expression_matrix_decoding(exp_img):
    """"""
    with open(exp_img, 'rb') as exp_img_FH:
        exp_mat = imdecode(asarray(bytearray(exp_img_FH.read()), dtype=uint8), IMREAD_COLOR)

    return exp_mat
