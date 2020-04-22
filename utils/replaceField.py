#!/usr/bin/env python3


import sys
import datatable as dt


def replaceField(file1, file2, field):
    """"""
    
    F1 = dt.fread(file1, nthreads=10)
    F2 = dt.fread(file2)

    F1[field] = F2[field]

    F1.to_csv(file1 + '.new.csv', quoting='none')


if __name__ == '__main__':

    replaceField(sys.argv[1], sys.argv[2], sys.argv[3])