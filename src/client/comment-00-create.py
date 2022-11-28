import requests
from utils import authenticate

DEFAULT_ARTICLE_SLUG = "new-article-title"

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
        "content": "New Comment Content"
    }
    # Make request - request
    article_slug = input("article_slug: ") or DEFAULT_ARTICLE_SLUG
    endpoint = f"http://localhost:8000/api/comments/{article_slug}/create/"
    r = requests.post(endpoint, json=data, headers=headers)
    print("text", r.text)



