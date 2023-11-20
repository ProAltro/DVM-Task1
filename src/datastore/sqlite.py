import sqlite3


class Databse:
    def __init__(self, con: str):
        self.con = sqlite3.connect(con)

    def fetch_data(self, query: str):
        try:
            cursor = self.con.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def insert_data(self, query: str):
        try:
            cursor = self.con.cursor()
            cursor.execute(query)
            self.con.commit()
            return cursor.lastrowid
        except Exception as e:
            print(e)
            return None


class SQLHandler:
    def __init__(self, db: Databse, **services):
        self.services: dict = {
            service: handler(db) for service, handler in services.items()
        }
