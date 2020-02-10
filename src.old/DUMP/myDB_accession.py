#!/usr/bin/env python3
"""
This software is used to access MySQL database.
"""


from sys import (argv, stderr)
from mysql.connector import (connect, errors)


class myDB:
    def __init__(self, user, host=None, pswd=None):
        self.user = user
        self.host = 'localhost' if host is None or host == '' else host
        self.pswd = pswd

        try:
            self.db_connection = connect(user=self.user, host=self.host, password=self.pswd, database='cornflowerDB')

        except errors.ProgrammingError:
            print(' '.join(('ERROR:', 'Access denied (invalid password)')), file=stderr)
            exit(1)

        self.cursor = self.db_connection.cursor()

    def show_basic_info(self):
        """
        Show basic info of databases and users.

        :return: None
        """
        print(''. join(('==== DATABASES of ', self.user, '@', self.host, ' ====')))
        self.cursor.execute('SHOW DATABASES')
        list(map(print, [_[0] for _ in self.cursor]))

        if myDB_obj.db_connection.user == 'root':
            print('\n==== ALL USERS ====')
            self.cursor.execute('SELECT user, host FROM mysql.user')
            list(map(print, [_ for _ in [''.join((u, '@', h)) for u, h in self.cursor]]))

        else:
            print('\n++++ Only root can show all the users ++++')

    def add_tab(self):
        """"""
        pass

    def del_tab(self):
        """"""
        pass

    def in_item(self):
        """"""
        pass

    def rm_item(self):
        """"""
        pass

    def grep_item(self):
        """"""
        pass


if __name__ == '__main__':
    """"""
    try:
        myDB_obj = myDB(user=argv[1], host=argv[2], pswd=argv[3])
        myDB_obj.show_basic_info()

    except IndexError:
        print(' '.join(('USAGE:', argv[0], '<user>', '[host]', '[password]')), file=stderr)
