import json
import re

import server.services.db_services as db_services

class PasswordComplexityError(Exception):
    pass

def check_password_complexity(password):
    """
    Check if the password is complex based on the given config and return a tuple (bool, message).
    """
    print("Loading config")
    with open('server/config.json', 'r') as conf_f:
        config = json.load(conf_f)
    complexity_requirements = config['complex_password_requirements']
    print("complexity: ", json.dumps(complexity_requirements, indent=2))
    length_requirement = config['password_length']

    print("Checking length")
    if len(password) < length_requirement:
        return False, f"Password must be at least {length_requirement} characters long."

    print("Checking uppercase")
    if complexity_requirements['uppercase'] and not re.search(r'[A-Z]', password):
        return False, "Password must include at least one uppercase letter."

    print("Checking lowercase")
    if complexity_requirements['lowercase'] and not re.search(r'[a-z]', password):
        return False, "Password must include at least one lowercase letter."

    print("Checking numbers")
    if complexity_requirements['numbers'] and not re.search(r'\d', password):
        return False, "Password must include at least one number."

    print("Checking special characters")
    if complexity_requirements['special_characters'] and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must include at least one special character."

    # check dictionary
    words: list = config["block_dictionary_use"]
    if any(map(lambda word: word.lower() in password.lower(), words)):
        return False, f"Password cannot include words dictionary. {words}"

    return True, "OK"

def validate_history(username, password):
    with open('server/config.json', 'r') as conf_f:
        config = json.load(conf_f)
    history = db_services.get_password_history(username, config["password_history"])
    print("history content:")
    print(*history, sep='\n')
    passwords_repeat = map(lambda x: x["password"] == password, history)
    if any(passwords_repeat):
        return False
    return True

def validate_attempts(username):
    with open('server/config.json', 'r') as conf_f:
        config = json.load(conf_f)

    login_attempts = config['login_attempts']
    attempts = db_services.get_login_attempts(username, time_in_sec=login_attempts['cooldown_sec'])
    if len(attempts) >= login_attempts['limit']:
        return False, "Don't fool me"
    return True, "OK"
# def validate_username():
#     ...
