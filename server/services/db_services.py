import computersecuritydb.database_manager as dbm
import server.dal.user as user
import server.dal.customer as customer

DATABASE_URL = "mydatabase.db"

def get_db_connection(name="db/app.sqlite") -> dbm.DatabaseManager:
    return dbm.DatabaseManager(name)

def create_user(user: user.User):
    u = user.model_dump()
    query = f"INSERT INTO Users (username, password, email, requires_pass_change) VALUES {tuple(u.values())}"
    conn = get_db_connection()
    conn.execute_query(query)

def search_user(username: str):
    query = f"SELECT * FROM Users WHERE username = '{username}'"

    conn = get_db_connection()
    u = conn.execute_query(query).fetchone()

    return u

def search_user_by_email(email: str):
    query = f"SELECT * FROM Users WHERE email = '{email}'"
    conn = get_db_connection()
    e = conn.execute_query(query).fetchone()
    return e

def update_user(user: user.User):
    query = f"UPDATE Users SET password='{user.password}', email='{user.email}', requires_pass_change={int(user.requires_pass_change)} WHERE username='{user.username}'"
    conn = get_db_connection()
    conn.execute_query(query)

def create_customer(_customer: customer.Customer):
    c = _customer.model_dump()
    query = f"INSERT INTO Customers (name, id, address, animal, feet_size) VALUES {tuple(c.values())}"
    conn = get_db_connection()
    conn.execute_query(query)

def get_customer_by_id(customer_id):
    query = f"SELECT * FROM Customers WHERE id = {customer_id}"

    conn = get_db_connection()
    c = conn.execute_query(query).fetchone()

    return c

def get_customers_by_name(customer_name):
    query = f"SELECT * FROM Customers WHERE name = '{customer_name}';"

    conn = get_db_connection()
    c = conn.execute_query(query).fetchall()
    print(f"{c=}")
    return c

def add_password_history(username, password):
    query = f"INSERT INTO OldPasswords (username, password) VALUES ('{username}', '{password}')"
    conn = get_db_connection()
    conn.execute_query(query)

def get_password_history(username, limit):
    query = f"SELECT * FROM OldPasswords WHERE username = '{username}' ORDER BY id DESC LIMIT {limit}"
    conn = get_db_connection()
    history = conn.execute_query(query).fetchall()
    return history

def add_login_attempt(username):
    query = f"INSERT INTO LoginAudit (username, ts) Values ('{username}', Datetime('now', 'localtime') )"
    conn = get_db_connection()
    conn.execute_query(query)

def get_login_attempts(username, time_in_sec=60):
    print(f"ENTER: get_login_attempts({username=}, {time_in_sec=})")
    query = f"""
    SELECT username FROM LoginAudit
        WHERE username = '{username}' AND ts >= Datetime('now', '-{time_in_sec} seconds', 'localtime')
        ORDER BY ts DESC LIMIT 1000
    """
    conn = get_db_connection()
    attempts = conn.execute_query(query).fetchall()
    return attempts
