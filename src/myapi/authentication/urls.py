from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token 

from .views import RegisterView

app_name = 'authentication'

urlpatterns = [
    path('', obtain_auth_token, name='obtain-token'),
    path('register/', RegisterView.as_view(), name='register'),
]