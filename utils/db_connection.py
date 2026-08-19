import sqlite3
from utils.config import Config


class DatabaseConnection:

    def __init__(self, database=None):
        self.database = database or Config.DATABASE_NAME
        self.connection = sqlite3.connect(self.database)

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.database)

        return self.connection

    def execute_query(self, query, parameters=()):
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchall()

    def execute_update(self, query, parameters=()):
        cursor = self.connection.cursor()
        cursor.execute(query, parameters)
        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None