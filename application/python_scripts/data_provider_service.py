# Connection of Python and MySQL database to retrieve information

import pymysql
from application.python_scripts.exceptions import MissingKeyData, ValueNotInDDBB


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
        types = self.cursor.fetchall()  # tuple of tuple elements containing row data
        # the below will convert the tuple of tuples "types" onto a list of strings
        types_list = self._single_item_tuple_to_list_convertor(types)
        return types_list

    def get_all_unique_categories(self):
        sql = "CALL GetCategory()"
        self.cursor.execute(sql)
        categories = self.cursor.fetchall()  # tuple of tuple elements containing row data
        # the below will convert the tuple of tuples "category" onto a list of strings
        categories_list = self._single_item_tuple_to_list_convertor(categories)
        return categories_list

    def get_url(self, type_name=None, category_name=None):
        try:
            # Try block to check that we actually have provided the required info
            self._check_provided_data(type_name, category_name)

        except MissingKeyData as exc:
            # Except to execute if the error is due to type or category not being provided
            print(exc)
            self.conn.rollback()
            print("rolled back")

        except Exception as exc:
            # Except to execute for any other error than MissingKeyData
            print(exc)
            self.conn.rollback()
            print("rolled back")

        else:
            # Else block to execute when no errors are found within the try block
            sql = "CALL GetUrl(%s, %s)"
            input_values = (type_name, category_name, )  # tuple with the data to replace %s placeholders
            self.cursor.execute(sql, input_values)
            urls = self.cursor.fetchall()  # tuple of tuple elements containing row data
            # the below will convert the tuple of tuples "urls" onto a list of strings
            urls_list = self._single_item_tuple_to_list_convertor(urls)
            return urls_list

    def set_type(self, type_name):
        sql = "CALL InsertType(%s)"
        input_values = (type_name,)  # tuple with the data to replace %s placeholders
        try:
            # code to add the new type on to the type_media table.
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        # below code is to retrieve the latest type added on to the table, so it can be returned
        sql_new_type_name = "select type_name from type_media order by type_id desc limit 1"
        self.cursor.execute(sql_new_type_name)
        new_type = self.cursor.fetchone()  # tuple of tuple elements containing row data
        return new_type[0]

    def set_source(self, source_name):
        sql = "CALL InsertSource(%s)"
        input_values = (source_name,)  # tuple with the data to replace %s placeholders
        try:
            # code to add the new source on to the source_media table.
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        # below code is to retrieve the latest source added on to the table, so it can be returned
        sql_new_source_name = "select source_name from source_media order by source_id desc limit 1"
        self.cursor.execute(sql_new_source_name)
        new_source = self.cursor.fetchone()  # tuple of tuple elements containing row data
        return new_source[0]

    def set_category(self, category_name):
        sql = "CALL InsertCategory(%s)"
        input_values = (category_name,)  # tuple with the data to replace %s placeholders
        try:
            # code to add the new category on to the category_media table.
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        # below code is to retrieve the latest category added on to the table, so it can be returned
        sql_new_category_name = "select category_name from category_media order by category_id desc limit 1"
        self.cursor.execute(sql_new_category_name)
        new_category = self.cursor.fetchone()  # tuple of tuple elements containing row data
        return new_category[0]

    def set_media(self, title, url, type_id, source_id, category_id):
        sql = "CALL InsertMedia(%s, %s, %s, %s, %s)"
        input_values = (title, url, type_id, source_id, category_id,)  # tuple with the data to replace %s placeholders
        try:
            # code to add the new media on to the media table.
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        # below code is to retrieve the latest media added on to the table, so it can be returned
        sql_new_media_title = "select media_title from media order by media_id desc limit 1"
        self.cursor.execute(sql_new_media_title)
        new_media = self.cursor.fetchone()  # tuple of tuple elements containing row data
        return new_media[0]

    # HELPER FUNCTIONS: semi private methods to be used in this class methods
    def _single_item_tuple_to_list_convertor(self, row_tuples):
        """Given a tuple of single item tuples, returns a list with each element being the element within the single tuple element"""
        items_list = []
        for item in row_tuples:
            items_list.append(item[0])
        return items_list

    # semi-private method used to check if all info for method get_url() is actually provided
    def _check_provided_data(self, type_name, category_name):
        if not type_name and not category_name:
            raise MissingKeyData("Both type and category name user selection MUST be given")
        elif not type_name:
            raise MissingKeyData("Type name MUST be given")
        elif not category_name:
            raise MissingKeyData("Category name MUST be given")
        elif type_name not in self.get_all_unique_types():
            raise ValueNotInDDBB("Type name does not exist in the database")
        elif category_name not in self.get_all_unique_categories():
            raise ValueNotInDDBB("Category name does not exist in the database")


# The below is for testing purposes only
if __name__ == "__main__":
    MYSQL = DataProviderService()
    print(MYSQL.get_all_unique_types())
    print(MYSQL.get_all_unique_categories())
    print(MYSQL.get_url("sound", "instrumental"))
    # print(MYSQL.get_url("sound"))
    # print(MYSQL.get_url("flower", "instrumental"))
    # print(MYSQL.get_url("sound", "instrumentals"))
    # print(MYSQL.set_type("test_type"))
    # print(MYSQL.get_all_unique_types())
    # print(MYSQL.set_source("test_source"))
    # print(MYSQL.set_category("test_category"))
    # print(MYSQL.get_all_unique_categories())
    # print(MYSQL.set_media("test_media", "test_url", 1, 1, 3))
