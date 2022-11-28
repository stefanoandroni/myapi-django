from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

# Overriding the default one
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer' # default 'Token'

