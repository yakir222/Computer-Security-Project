import sqlite3
import computersecuritydb.database_manager as dbm

# Connecting to the database
def test_setting_up_connection_creates_new_file():
    import os
    db_file = 'example.db'
    assert not os.path.exists(db_file)
    dbm.DatabaseManager(db_file)
    assert os.path.exists(db_file)
    os.remove(db_file)

def test_create_new_table_returns_cursor():
    import os
    db_file = 'example.db'
    dbconn = dbm.DatabaseManager(db_file)
    cur = dbconn.execute_query('''
        CREATE TABLE IF NOT EXISTS Users(
            username TEXT,
            email TEXT,
            password TEXT,
            requires_pass_change INT,
            PRIMARY KEY (username)
        )
    ''')
    assert cur is not None
    assert type(cur) is sqlite3.Cursor
    os.remove(db_file)


# # Creating tables if they don't exist
# db_manager.execute_query('''
#     CREATE TABLE IF NOT EXISTS Users(
#         username TEXT,
#         email TEXT,
#         password TEXT,
#         requires_pass_change INT,
#         PRIMARY KEY (username)
#     )
# ''')

# db_manager.execute_query('''
#     CREATE TABLE IF NOT EXISTS OldPasswords(
#         username TEXT,
#         password TEXT,
#         FOREIGN KEY (username) REFERENCES Users(username)
#     )
# ''')

# db_manager.execute_query('''
#     CREATE TABLE IF NOT EXISTS Tokens(
#         username TEXT,
#         token TEXT,
#         FOREIGN KEY (username) REFERENCES Users(username)
#     )
# ''')

# db_manager.execute_query('''
#     CREATE TABLE IF NOT EXISTS Customers(
#         name TEXT,
#         id INT,
#         address TEXT,
#         animal TEXT,
#         feet_size INT
#     )
# ''')
