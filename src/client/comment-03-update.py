import requests
from utils import authenticate

DEFAULT_COMMENT_ID = 1

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
    # Make request - data
    data ={
        "content": "My Updated Comment Content",
    }
    # Make request - request
    comment_id = input("comment_id: ") or DEFAULT_COMMENT_ID
    endpoint = f"http://localhost:8000/api/comments/{comment_id}/update/"
    r = requests.put(endpoint, headers=headers, json=data)
    print("text", r.text)



