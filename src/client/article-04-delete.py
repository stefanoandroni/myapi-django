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
    # Make request - request
    article_slug = input("article_slug: ") or DEFAULT_ARTICLE_SLUG
    endpoint = f"http://localhost:8000/api/articles/{article_slug}/delete/"
    r = requests.delete(endpoint, headers=headers)
    print("Deleted:", r.status_code==204)



