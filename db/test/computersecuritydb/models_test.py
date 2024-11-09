import os
import pytest

import computersecuritydb.models as m
import computersecuritydb.database_manager as dbm

db_file = "test_models.sqlite"
dbconn = None
counter = 0

def add_counter():
    global counter
    counter += 1

def setup_db_connection(state=True):
    global dbconn, db_file
    if state:
        dbconn = dbm.DatabaseManager(db_file)
    else:
        del dbconn
        os.remove(db_file)

def setup_function(function):
    """setup any state tied to the execution of the given function. Invoked for every test function in the module."""
    print()
    add_counter()
    print(f"{counter}) -- SetUp ({function.__name__=})")
    setup_db_connection()


def teardown_function(function):
    """teardown any state that was previously setup with a setup_function call."""
    global dbconn
    add_counter()
    setup_db_connection(False)
    print(f"{counter}) -- tearDown ({function.__name__=})")

def test_save_and_load_user_returns_new_user():
    dbconn.create_table("Users",
        [
            "username TEXT",
            "email TEXT",
            "password TEXT",
            "requires_pass_change INT"
        ],
        "username"
    )
    test_user = m.User(**{'username':'Test User', 'email': 'test@exmaple.com', 'password': 'testPass!', 'requires_pass_change': False})
    test_user.save(dbconn)
    # return

    loaded = m.User.load(test_user.username, dbconn)
    assert type(loaded) is m.User
    assert loaded is not test_user
    assert loaded.username == test_user.username
    assert loaded.email == test_user.email
    assert loaded.password == test_user.password
    assert loaded.requires_pass_change == test_user.requires_pass_change
    assert loaded.requires_pass_change is False


def test_save_and_load_user_returns_new_user2():
    pass

def test_save_and_load_user_returns_new_user3():
    pass

# Example Usage of User model
# new_user = User("john_doe", "john@example.com", "password123", 1)
# new_user.save(db_manager)

# loaded_user = User.load("john_doe", db_manager)
# if loaded_user:
#     print("Loaded user:", loaded_user.__dict__)
# else:
#     print("User not found.")

# new_user.update_password("new_password123", db_manager)
# print("Updated password.")

# new_user.delete(db_manager)
# print("Deleted user.")

# # Close the database connection
# del db_manager
