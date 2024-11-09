import datetime


def get_new_token(username: str) -> str:
    return f"MYTOKEN[{username}-{datetime.datetime.now()}]"
