import sqlite3


class DatabaseConnection:

    def __init__(self, database="test_database.db"):
        self.database = database
        self.connection = None

    def connect(self):
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