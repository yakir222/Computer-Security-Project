import sqlite3
from typing import Optional

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


class DatabaseManager:
    def __init__(self, db_name: str) -> None:
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()

    def __del__(self) -> None:
        self.conn.close()

    def execute_query(self, query: str, parameters: Optional[tuple] = None) -> sqlite3.Cursor:
        print(f"DEBUG QUERY - @@@{query}@@@{parameters}")

        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        self.conn.commit()
        return self.cursor

    def create_table(self, name: str, fields: list, key=None):
        if key:
            fields.append(f'PRIMARY KEY ({key})')

        template = f'CREATE TABLE IF NOT EXISTS {name}({", ".join(fields)})'
        # if key:
        #     # Remove closing parentheses and add primary key statement
        #     template = template[:-1] + f', PRIMARY KEY ({key}) )'
        self.execute_query(template)
