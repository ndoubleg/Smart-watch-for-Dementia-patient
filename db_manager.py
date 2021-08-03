import sqlite3

class DatabaseManager:
    connection = None
    cursor = None
    DB_PATH = "~/*.db"

    def create_connection(self):
        try:
            print(f"Connecting to database : {self.DB_PATH} ...")
            self.connection = sqlite3.connect(self.DB_PATH)
            print(f"Succesfully connected to database : {self.DB_PATH}")
        except sqlite3.Error as e:
            print(e)

