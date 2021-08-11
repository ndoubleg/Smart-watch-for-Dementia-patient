import sys

import pymysql
from pymysql.cursors import DictCursor

from singleton_instance import SingletonInstance


class DatabaseManager(SingletonInstance):
    connection = None
    cursor = None
    DB_CREDENTIALS = "credentials"
    DB_WATCH_DATA = "watch_data"
    DB_USER_DATA = "userinfo"
    def create_connection(self, database):
        """ Create connection with database """
        try:
            print(f"Connecting to database : {database} ...")
            self.connection = pymysql.connect(user="ubuntu", password='', database=database)
            print(f"Successfully connected to database : {database}")
        except pymysql.Error as e:
            print(e)

    def get_cursor(self):
        """ Create cursor """
        self.cursor = self.connection.cursor(DictCursor)

    def close_connection(self, database):
        """ Close connection to database """
        if self.connection is not None:
            self.connection.close()
            print(f"Succesfully closed database : {database}")

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
        WHERE {column_name}
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()[-1]

    def insert_row(self, *values, database, table_name):
        float_list = []

        column_str = '('
        column_name_list = self.get_column_names(database, table_name)
        column_str += ", ".join(column_name_list)
        column_str += ')'

        # if isinstance(values[0], float):
        #     for flo in values:
        #         float_list.append(str(flo))

        value_str = '("'
        value_str += '", "'.join(values)
        value_str += '")'

        print(value_str, file=sys.stderr)

        query = f"""
        INSERT INTO {table_name} 
        {column_str}
        VALUES
        {value_str};
        """
        self.cursor.execute(query)

    def get_column_names(self, database, table_name):
        column_name_list = []
        query = f"""
        SELECT `COLUMN_NAME`
        FROM `INFORMATION_SCHEMA`.`COLUMNS`
        WHERE `TABLE_SCHEMA` = '{database}'
            AND `TABLE_NAME` = '{table_name}';
        """
        self.cursor.execute(query)
        for col in self.cursor.fetchall():
            column_name_list.append(col['COLUMN_NAME'])
        return column_name_list

    def insert_with_specific_field(self,*values,table_name,field_name):
        float_list = []
        column_str = '('
        column_name_list = field_name
        column_str += ", ".join(column_name_list)
        column_str += ')'
            
        if isinstance(values[0], float):
            for flo in values:
                float_list.append(str(flo))
        if len(values)!=0:
            for value in values:
                float_list.append(str(value))

        value_str = '("'
        value_str += '", "'.join(float_list)
        value_str += '")'

        query = f"""
        INSERT INTO {table_name} 
        {column_str}
        VALUES
        {value_str};
        """
        print(query)
        self.cursor.execute(query)
        self.connection.commit() 
    def get_login_info(self,login_id,pw,table_name):
        
        
#        login_id = '"'+login_id+'"'
#        pw = '"'+pw+'"'
        query=f"""
        SELECT name
        FROM {table_name}
        WHERE id="{login_id}" AND pw="{pw}";
        """
         
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return result[-1]
        else:
            return "wrong"
