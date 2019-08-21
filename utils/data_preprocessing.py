#!/usr/bin/env python3


from sys import (argv, stderr)
from pandas import (DataFrame, read_table)


class single_cell_data_table:
    def __init__(self):
        """"""
        self._data = DataFrame()

    def data_table_transpose(self, data_file, flag):
        """"""
        try:
            self._data = read_table(data_file, compression='gzip', header=0, index_col=0)

        except OSError:
            self._data = read_table(data_file, header=0, index_col=0)

        if flag == 'transpose':
            self._data = self._data.transpose()
            self._data.to_csv(''.join((data_file, '.T.csv.gz')), compression='gzip', header=True, index=True)

        elif flag == 'tsv2csv':
            self._data.to_csv(''.join((data_file, '.csv.gz')), compression='gzip', header=True, index=True)


if __name__ == '__main__':
    data_table = single_cell_data_table()

    try:
        if argv[1] == '--help' or argv[1] == '-h' or len(argv) <= 2:
            print(' '.join(('USAGE:', argv[0], '[--help|-h] <transpose|tsv2csv> <data table file>')))

        else:
            data_table.data_table_transpose(argv[2], argv[1])

    except FileNotFoundError:
        print('Invalid file', file=stderr)
