import os


def get_username():
    username = os.getenv("USERNAME")

    if username is None:
        raise OSError("USERNAME environment is not set.")

    return username.lower()


def get_password():
    password = os.getenv("PASSWORD")

    if password is None:
        raise OSError("PASSWORD environment is not set.")

    return password
