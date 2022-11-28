import requests
from getpass import getpass

from utils import authenticate

# Make request

# Make request - data
username = input("Username: ")
password = getpass("Password: ")
password2 = getpass("Password2: ")
data = {
    'username': username,
    'password': password,
    'password2': password2
}
# Make request - request
endpoint = "http://127.0.0.1:8000/api/auth/register/"
r = requests.post(endpoint, data=data)
print("text", r.text)

# Authenticate and get token
if r.status_code == 201:
    auth_r = authenticate(username, password)
    if auth_r.status_code == 200:
        token = auth_r.json()['token']
        print(f"token: {token}")