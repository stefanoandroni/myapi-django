import requests
from utils import authenticate

DEFAULT_ARTICLE_SLUG = "my-new-article"

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
        # "title": "My Updated Article Title",
        "content": "My Updated Article Content",
    }
    # Make request - request
    article_slug = input("article_slug: ") or DEFAULT_ARTICLE_SLUG
    endpoint = f"http://localhost:8000/api/articles/{article_slug}/update/"
    r = requests.put(endpoint, headers=headers, json=data)
    print(r.text)



