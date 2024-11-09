import requests


def get_user(username):
    print(requests.get(f"http://localhost:8000/base/user/{username}").json())
def add_user(user):
    print(requests.post("http://localhost:8000/base/user", json=user).json())
def update_user_password(user_old_new):
    print(requests.post("http://localhost:8000/base/user/updatePassword", json=user_old_new).json())

def login_user(user_login):
    print(requests.post("http://localhost:8000/base/user/login", json=user_login).json())

def add_customer(customer):
    print(requests.post("http://localhost:8000/base/customer", json=customer).json())

def get_customer(customer_id=None, name=None):
    params = {
        "id": customer_id,
        "name":name
    }
    print(requests.get("http://localhost:8000/base/customer", params={k:v for k,v in params.items() if v is not None}).json())

if __name__ == "__main__":
    users_add = {'username': "Nitzan",'email':"nitz@an.com",'password': "A123!45v67"}
    add_user(users_add)
    get_user(users_add['username'])
    login_user({'username': users_add['username'], 'password': users_add['password']+'aaa'}) # BAD
    login_user({'username': users_add['username'], 'password': users_add['password']})

    update_user_password({'username': users_add['username'], 'old_password': users_add['password'], 'new_password': 'Aa49123456!'})

    customer_add = {"name": "Cust1", "id": 123456789, "address": "Beirut", "animal": "Lion", "feet_size": 13}
    add_customer(customer_add)
    get_customer(name=customer_add['name'])
