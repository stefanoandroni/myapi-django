from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response

from api.mixins import CommentOwnerQsMixin, CommentStaffNoRestrictionsQsMixin
from articles.models import Article
from .models import Comment
from .serializers import CommentInlineSerializer, CommentSerializer, PostCommentSerializer, StaffPostCommentSerializer

# - - - - - - - - - - - - - - - - - - - - CBV (Class Based View) - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - -
# Comment CRUD  
# - - - - - - - - - -

# CRUD views kept separate for learning purposes

#Create
class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = PostCommentSerializer
    
    def create(self, request, *args, **kwargs):
        # method override to return the object created with a different serializer (?) bad?
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        obj_serializer = CommentSerializer(obj, context={'request': request})
        return Response(obj_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StaffPostCommentSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        article = get_object_or_404(Article, slug=slug)
        if self.request.user.is_staff:
            return serializer.save(article=article)
        return serializer.save(article=article, author=self.request.user)   

# Retrieve (detail)
class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

# Retrieve (list)
class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentInlineSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        article_slug = self.kwargs.get('slug')
        if article_slug:
            qs = qs.filter(article=article_slug)
        return qs

# Update
class CommentUpdateAPIView(CommentOwnerQsMixin, generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = PostCommentSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.initial_data['article'] = instance.article
        serializer.is_valid(raise_exception=True)
        obj = self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        obj_serializer = CommentSerializer(obj, context={'request': request})
        return Response(obj_serializer.data)

# Delete
class CommentDeleteAPIView(CommentStaffNoRestrictionsQsMixin, CommentOwnerQsMixin, generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = PostCommentSerializer
    lookup_field = 'id'