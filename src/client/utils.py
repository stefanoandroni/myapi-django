import requests
from getpass import getpass

DEFAULT_USERNAME = "m.lowson"
DEFAULT_PASSWORD = "RM@CQvj4YGXr5-y"

def authenticate(username=None, password=None):
    if not username or not password:
        username = DEFAULT_USERNAME if username is None else username
        password = DEFAULT_PASSWORD if password is None else password
        username = input("Username: ") or DEFAULT_USERNAME
        password = getpass("Password: ") or DEFAULT_PASSWORD
    auth_endpoint = "http://localhost:8000/api/auth/"
    auth_r = requests.post(auth_endpoint, json={"username": username, "password": password})
    return auth_r