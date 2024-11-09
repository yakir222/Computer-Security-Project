import requests

def add_user(user):
    print(requests.post("http://localhost:8000/base/user", json=user).json())
def add_customer(customer):
    requests.post("http://localhost:8000/base/customer", json=customer)

if __name__ == "__main__":
    users = [
        {'username': "Nitzan",'email':"nitz@an.com",'password': "A123!45v67"},
        {'username': "Yakir",'email':"yak@ir.com",'password': "abCde!7kon"},
        {'username': "Netanel",'email':"netan@el.com",'password': "!1234hij&H"},
        {'username': "Liel",'email':"liel@co.com",'password': "1bcd5$6A7o"}
    ]
    customers = [
        {"name": "Cust1", "id": 123456789, "address": "Beirut", "animal": "Lion", "feet_size": 13},
        {"name": "Cust2", "id": 123456709, "address": "Paris", "animal": "Frog", "feet_size": 9},
        {"name": "Cust3", "id": 123456489, "address": "Nova (Formerly Gaza)", "animal": "Donkey", "feet_size": 10},
        {"name": "Cust4", "id": 121456789, "address": "Holon", "animal": "Alligator", "feet_size": 43},
        {"name": "Cust5", "id": 123458789, "address": "Nowehere", "animal": "Ant", "feet_size": 34}
    ]
    for u in users:
        add_user(u)
    for c in customers[:]:
        add_customer(c)

# INSERT INTO OldPasswords (username, password) VALUES ("Liel",    "pinkRules"),
#     ("Netanel", "adMatayHIT"),
#     ("Yakir",   "KamaTzahal"),
#     ("Nitzan",  "titulim.reminder"),
#     ("Liel",    "pinkRules"),
#     ("Liel",    "partzuLi"),
#     ("Liel",    "Sisma123!"),
#     ("Nitzan",  "alTithatenAvi"),
#     ("Yakir",   "theFrontendIsDone");
