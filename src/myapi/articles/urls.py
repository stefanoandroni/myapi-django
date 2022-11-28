from django.urls import path

from .views import ArticleCreateAPIView, ArticleDeleteAPIView, ArticleDetailAPIView, ArticleListAPIView, ArticleUpdateAPIView

app_name = 'articles'

urlpatterns = [
    path('', ArticleListAPIView.as_view(), name='article-list'),
    path('create/', ArticleCreateAPIView.as_view(), name='article-create'),
    path('<slug:slug>/update/', ArticleUpdateAPIView.as_view(), name='article-update'),
    path('<slug:slug>/delete/', ArticleDeleteAPIView.as_view(), name='article-delete'),
    path('<slug:slug>/', ArticleDetailAPIView.as_view(), name='article-detail'),
]
