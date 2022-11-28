import requests
from utils import authenticate

DEFAULT_ARTICLE_TITLE = "My New Article"

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
    article_title = input("article_title: ") or DEFAULT_ARTICLE_TITLE
    data ={
        "title": article_title,
        "content": "My New Article Content",
        "topic": "c",
        "public": True,
    }
    # Make request - request
    endpoint = "http://localhost:8000/api/articles/create/"
    r = requests.post(endpoint, json=data, headers=headers)
    print(r.text)







