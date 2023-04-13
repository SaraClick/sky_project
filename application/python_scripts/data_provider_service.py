# Connection of Python and MySQL database to retrieve information

import pymysql
import sys
import redirect
import url_for

from application.python_scripts.exceptions import MissingKeyData, ValueNotInDDBB


class DataProviderService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        """
        host = 'localhost'
        port = 3306
        user = 'root'
        database = 'FortyWinks'
        password = ""
        # At the beginning of the course, all MAC users installed MySQL with no password set however WINDOWS users
        # set the password "password" for MySQL. The below if statement will check if the system is Windows/Mac,
        # and if Windows set the password to password, otherwise an empty string is used
        if sys.platform == 'win32':
            password = 'password'
        self.conn = pymysql.connect(host=host, port=port, user=user, db=database, password=password)
        self.cursor = self.conn.cursor()

    def get_all_unique_types(self):
        """Returns a list of strings. Each string is a type of media within our database."""
        # The below sql string is the query that will run inside mySql. This will call the GetType stored procedure.
        sql = "CALL GetType()"
        # The below is to execute the sql query
        self.cursor.execute(sql)
        # fetchall() retrieves all rows of a query and returns a tuple of tuples
        types = self.cursor.fetchall()
        # the below will convert the tuple of tuples "types" into a list of strings
        types_list = self._single_item_tuple_to_list_convertor(types)
        return types_list

    # same structure as get_all_unique_types(self) and refer above for comment breakdown.

    def get_all_unique_categories(self):
        """Returns a list of strings. Each string is a category of media within our database."""
        sql = "CALL GetCategory()"
        self.cursor.execute(sql)
        categories = self.cursor.fetchall()
        categories_list = self._single_item_tuple_to_list_convertor(categories)
        return categories_list

    def get_url(self, type_name=None, category_name=None):
        """Given a type and category name, it returns a list of Url strings matching the type and category."""
        try:
            # Try block to check that we actually have provided the required info
            self._check_provided_data(type_name, category_name)

        except MissingKeyData as exc:
            # Except block to execute if the error is due to type or category not being provided
            print(exc)
            self.conn.rollback()
            print("rolled back")

        except Exception as exc:
            # Except block to execute for any  error other than MissingKeyData
            print(exc)
            self.conn.rollback()
            print("rolled back")

        else:
            # Else block to execute when no errors are found within the try block
            sql = "CALL GetUrl(%s, %s)"  # %s is a placeholder for input to be given
            input_values = (type_name, category_name, )  # tuple with the data to replace %s placeholders
            self.cursor.execute(sql, input_values)
            urls = self.cursor.fetchall()  # tuple of tuple elements containing row data
            # the below will convert the tuple of tuples "urls" onto a list of strings
            urls_list = self._single_item_tuple_to_list_convertor(urls)
            return urls_list

    def set_type(self, type_name):
        """Given a new type_name string, inserts the type_name into the database."""
        # The below sql string is the query that will run inside mySql. This will call the GetType stored procedure.
        sql = "CALL InsertType(%s)"  # %s is a placeholder for a parameter to be given
        # The below is to execute the sql query
        input_values = (type_name,)  # tuple with the data to replace %s placeholders
        try:
            # code to add the new type on to the type_media table.
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        # below code is to retrieve the latest type added to the table, so it can be returned
        sql_new_type_name = "select type_name from type_media order by type_id desc limit 1"
        self.cursor.execute(sql_new_type_name)
        new_type = self.cursor.fetchone()  # tuple of tuple elements containing row data
        return new_type[0]

    # same structure as set_type method, refer above for comment breakdown.
    def set_source(self, source_name):
        """Given a new source_name string, inserts the source_name into the database."""
        sql = "CALL InsertSource(%s)"
        input_values = (source_name,)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_source_name = "select source_name from source_media order by source_id desc limit 1"
        self.cursor.execute(sql_new_source_name)
        new_source = self.cursor.fetchone()
        return new_source[0]

    # same structure as set_type method, refer above for comment breakdown.
    def set_category(self, category_name):
        """Given a new category_name string, inserts the category_name into the database."""
        sql = "CALL InsertCategory(%s)"
        input_values = (category_name,)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_category_name = "select category_name from category_media order by category_id desc limit 1"
        self.cursor.execute(sql_new_category_name)
        new_category = self.cursor.fetchone()
        return new_category[0]

    # same structure as set_type method, refer above for comment breakdown.
    def set_media(self, title, url, type_id, source_id, category_id):
        """Given a title, url, type_id, source_id, category_id string, inserts the media into the database."""
        sql = "CALL InsertMedia(%s, %s, %s, %s, %s)"
        input_values = (title, url, type_id, source_id, category_id,)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_media_title = "select media_title from media order by media_id desc limit 1"
        self.cursor.execute(sql_new_media_title)
        new_media = self.cursor.fetchone()
        return new_media[0]

    # HELPER FUNCTIONS: semi private methods to be used in this class methods
    def _single_item_tuple_to_list_convertor(self, row_tuples):
        """Given a tuple of single item tuples, returns a list with each being the first element of the individual tuples"""
        items_list = []
        # looping through the tuple of tuples
        for item in row_tuples:
            # appending the first element of each tuple into item_list
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

    # Admin login
    # def get_all_admins(self):
    #     admin_email = input('Enter admin email: ')
    #     admin_password = input('Enter admin password: ')
    #     sql = f"SELECT * FROM admins WHERE admin_email = '{admin_email}' AND admin_password = '{admin_password}' AND admin_status = 'active'"
    #     self.cursor.execute(sql)
    #     result = self.cursor.fetchall()
    #
    #     if result:
    #         print('Login successful')
    #     else:
    #         print('Username or password not recognised')
    def get_all_admins(self, email, password):
        if not email or password:
            raise MissingKeyData("Email/password has not been recognised")
        # elif is email and password:
        #     return

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
