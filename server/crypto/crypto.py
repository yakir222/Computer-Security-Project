import hashlib
import os.path as osp
import hmac
import secrets
from datetime import datetime
import random

class NoSaltFileError(RuntimeError):
    pass

__SALT_PATH = "salt.b64"

def hash_password(password, salt):
    """Hash the password with the salt using HMAC."""
    # Convert the password and salt to bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Compute the HMAC-SHA256 hash
    hashed_password = hmac.new(salt_bytes, password_bytes, hashlib.sha256).hexdigest()

    return hashed_password

def get_salt():
    print("ENTER: get_salt")
    try:
        return load_salt_file()
    except NoSaltFileError:
        # No salt file, create one
        salt = generate_salt()
        create_salt_file(salt)
        return salt

def load_salt_file():
    print("Loading salt file")
    try:
        with open(__SALT_PATH, 'r') as salt_f:
            return salt_f.read()
    except OSError:
        print("Salt file not existing.")
        raise NoSaltFileError()


def create_salt_file(salt: str):
    print("Saving salt")
    with open(__SALT_PATH, 'w') as salt_f:
        return salt_f.write(salt)

def generate_salt(length=16):
    print("Creating salt")
    return secrets.token_hex(length)  # 16 bytes, 32 characters in hex

def hash_password_sha1(randomValue):
    return hashlib.sha1(randomValue.encode('utf-8')).hexdigest()

def generate_random_password():
    print("Creating random password")
    generated_raw = f"{datetime.now()}{random.random()}"
    generated_hashed = hash_password_sha1(generated_raw)
    return generated_hashed

if __name__ == "__main__":
    print(get_salt())
