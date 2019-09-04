#!/usr/bin/env python3


from sys import (argv, stderr)
from pandas import (DataFrame, read_table, read_csv)
from cv2 import imwrite
from numpy import (array,
                   uint8)


class single_cell_data_table:
    def __init__(self, data_file):
        """"""
        self.__data_file = data_file
        self.__data = DataFrame()
        self.__imat = array([], dtype=uint8)

    def read_table(self):
        """"""
        try:
            self.__data = read_table(self.__data_file, compression='gzip', header=0, index_col=0)

        except OSError:
            self.__data = read_table(self.__data_file, header=0, index_col=0)

    def read_csv(self):
        """"""
        try:
            self.__data = read_csv(self.__data_file, compression='gzip', header=0, index_col=0)

        except OSError:
            self.__data = read_csv(self.__data_file, header=0, index_col=0)

    def write_csv(self):
        self.__data.to_csv(''.join((self.__data_file, '.csv.gz')), compression='gzip', header=True, index=True)

    def write_img(self):
        imwrite(''.join((self.__data_file, '.tif')), self.__imat)

    def transpose(self):
        """"""
        self.__data = self.__data.transpose()

    def to_image(self):
        """"""
        self.__imat = self.__data.values * 255


if __name__ == '__main__':
    data_table = single_cell_data_table(argv[2])

    if argv[2].endswith('.txt.gz') or argv[2].endswith('.txt'):
        data_table.read_table()

    if argv[2].endswith('.csv.gz') or argv[2].endswith('.csv'):
        data_table.read_csv()

    try:
        if argv[1] == '--help' or argv[1] == '-h' or len(argv) <= 2:
            print(' '.join(('USAGE:', argv[0], '[--help|-h] <table2csv|transpose|2img> <data table file>')))

        else:
            if argv[1] == 'table2csv':
                data_table.write_csv()

            if argv[1] == 'transpose':
                data_table.transpose()
                data_table.write_csv()

            if argv[1] == '2img':
                data_table.to_image()
                data_table.write_img()

    except FileNotFoundError:
        print('Invalid file', file=stderr)
