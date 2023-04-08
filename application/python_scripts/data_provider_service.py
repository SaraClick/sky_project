# Connection of Python and MySQL database

import pymysql
# from passlib.hash import sha256_crypt


class DataProviderService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        """
        host = 'localhost'
        port = 3306
        user = 'root'
        password = 'password'
        database = 'fortywinks'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()

    def get_unique_types(self):
        pass

