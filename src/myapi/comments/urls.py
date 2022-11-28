from django.urls import path

from .views import CommentCreateAPIView, CommentDeleteAPIView, CommentDetailAPIView, CommentListAPIView, CommentUpdateAPIView

app_name = 'comments'

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='comment-list'),
    path('<int:id>/delete/', CommentDeleteAPIView.as_view(), name='comment-delete'),
    path('<int:id>/update/', CommentUpdateAPIView.as_view(), name='comment-update'),
    path('<int:id>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('<slug:slug>/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('<slug:slug>/', CommentListAPIView.as_view(), name='article-comment-list'),
]
