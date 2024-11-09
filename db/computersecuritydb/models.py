from pydantic import BaseModel, EmailStr
from typing import Optional

from computersecuritydb.database_manager import DatabaseManager


class User(BaseModel):
    username: str
    password: str
    email: EmailStr
    requires_pass_change: bool

    def save(self, db_manager: DatabaseManager) -> None:
        db_manager.execute_query('''
            INSERT INTO Users(username, email, password, requires_pass_change)
            VALUES (?, ?, ?, ?)
        ''', (self.username, self.email, self.password, int(self.requires_pass_change)))

    @staticmethod
    def load(username: str, db_manager: DatabaseManager) -> Optional["User"]:
        db_manager.execute_query('SELECT * FROM Users WHERE username = ?', (username,))
        user_data = db_manager.cursor.fetchone()
        if user_data:
            rv = User(**user_data)
            rv.requires_pass_change = bool(rv.requires_pass_change)
            return rv
        return None

    def update_password(self, new_password: str, db_manager: DatabaseManager) -> None:
        self.password = new_password
        db_manager.execute_query('UPDATE Users SET password = ? WHERE username = ?', (new_password, self.username))

    def delete(self, db_manager: DatabaseManager) -> None:
        db_manager.execute_query('DELETE FROM Users WHERE username = ?', (self.username,))

class OldPassword:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def save(self, db_manager: DatabaseManager) -> None:
        db_manager.execute_query('INSERT INTO OldPasswords(username, password) VALUES (?, ?)', (self.username, self.password))

class Customer:
    def __init__(self, name: str, id: int, address: str, favorite_animal: str, shoe_size: int) -> None:
        self.name = name
        self.id = id
        self.address = address
        self.favorite_animal = favorite_animal
        self.shoe_size = shoe_size

    def save(self, db_manager: DatabaseManager) -> None:
        db_manager.execute_query('''
            INSERT INTO Customers(name, id, address, favorite_animal, shoe_size)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.name, self.id, self.address, self.favorite_animal, self.shoe_size))
