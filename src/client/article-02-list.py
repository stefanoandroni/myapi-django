import requests
from utils import authenticate

# Authenticate
auth_r = authenticate()

if auth_r.status_code == 200:
    # Make request

    # Make request - headers
    token = auth_r.json()['token']
    print(token)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    # Make request - request
    endpoint = "http://localhost:8000/api/articles/"
    r = requests.get(endpoint, headers=headers)
    print(r.text)
    