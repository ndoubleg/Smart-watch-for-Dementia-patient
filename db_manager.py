import pymysql
from pymysql.cursors import DictCursor

from singleton_instance import SingletonInstance


class DatabaseManager(SingletonInstance):
    connection = None
    cursor = None
    DATABASE = "credentials"

    def create_connection(self):
        """ Create connection with database """
        try:
            print(f"Connecting to database : {self.DATABASE} ...")
            self.connection = pymysql.connect(user="ubuntu", password='', database=self.DATABASE)
            print(f"Successfully connected to database : {self.DATABASE}")
        except pymysql.Error as e:
            print(e)

    def get_cursor(self):
        """ Create cursor """
        self.cursor = self.connection.cursor(DictCursor)

    def close_connection(self):
        """ Close connection to database """
        if self.connection is not None:
            self.connection.close()
            print(f"Succesfully closed database : {self.DATABASE}")

    def select_column_with_filter(self, table_name, column_name, filter_keyword):
        """Fetch all records with 'filter_keyword' inside 'column_name' """
        query = f"""
        SELECT {column_name} 
        FROM {table_name} 
        WHERE {column_name} LIKE '%{filter_keyword}%'
        """
        self.cursor.execute(query)

    def select_last_element_of_column(self, table_name, column_name):
        """Fetch last record in 'column_name' """
        query = f"""
        SELECT {column_name} 
        FROM {table_name} 
        ORDER BY {column_name} DESC LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()[0]
