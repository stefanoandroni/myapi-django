from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('articles/', include('articles.urls')),
    path('comments/', include('comments.urls')),
    path('search/', include('search.urls')),
]
