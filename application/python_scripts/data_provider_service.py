# Connection of Python and MySQL database to retireve information

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
        database = 'FortyWinks'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()

    def get_all_unique_types(self):
        sql = "CALL GetType()"
        self.cursor.execute(sql)
        types = self.cursor.fetchall()
        return types

    def get_all_unique_categories(self):
        sql = "CALL GetCategory()"
        self.cursor.execute(sql)
        categories = self.cursor.fetchall()
        return categories

    def get_url(self, type_name=None, category_name=None):
        if type_name==None or category_name==None:
            pass
        else:
            sql = "CALL GetUrl(%s, %s)"
            input_values = (type_name, category_name, )
            self.cursor.execute(sql, input_values)
            urls = self.cursor.fetchall()
        return urls

    def set_type(self, type_name):
        pass

    def set_source(self, source_name):
        pass

    def set_media(self, title, url, type_id, source_id, category_id):
        pass


# The below is for testing purposes only
if __name__ == "__main__":
    MYSQL = DataProviderService()
    print(MYSQL.get_all_unique_types())
    print(MYSQL.get_all_unique_categories())
    print(MYSQL.get_url("sound", "instrumental"))
