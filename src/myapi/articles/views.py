from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from api.mixins import ArticleAllPublicHisPrivateQsMixin, ArticleHisPublicHisPrivateQsMixin, ArticleStaffNoRestrictionsQsMixin
from .models import Article
from .serializers import StaffPostArticleSerializer, ArticleInlineSerializer, GetArticleSerializer, PostArticleSerializer

# - - - - - - - - - - - - - - - - - - - - CBV (Class Based View) - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - -
# Article CRUD  
# - - - - - - - - - -

# CRUD views kept separate for learning purposes

# Create
class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostArticleSerializer

    def create(self, request, *args, **kwargs):
        # method override to return the object created with a different serializer (?) bad?
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        obj_serializer = GetArticleSerializer(obj, context={'request': request})
        return Response(obj_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StaffPostArticleSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            return serializer.save()
        return serializer.save(author=self.request.user)
    
# Retrieve (detail)
class ArticleDetailAPIView(ArticleStaffNoRestrictionsQsMixin, ArticleAllPublicHisPrivateQsMixin, generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = GetArticleSerializer
    lookup_field = 'slug'

# Retrieve (list)
class ArticleListAPIView(ArticleStaffNoRestrictionsQsMixin, ArticleAllPublicHisPrivateQsMixin, generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleInlineSerializer

# Update
class ArticleUpdateAPIView(ArticleStaffNoRestrictionsQsMixin, ArticleHisPublicHisPrivateQsMixin, generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostArticleSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StaffPostArticleSerializer
        return super().get_serializer_class()
    
    def perform_update(self, serializer):
        if self.request.user.is_staff:
            return serializer.save()
        return serializer.save(author=self.request.user)
    
    def update(self, request, *args, **kwargs):
        # method override to return the object updated with a different serializer (?) bad?
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # title is a required field in serializer
        if not ('title' in serializer.initial_data): # not good here (?)
            serializer.initial_data['title'] = instance.title
        serializer.is_valid(raise_exception=True)
        obj = self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        obj_serializer = GetArticleSerializer(obj, context={'request': request})
        return Response(obj_serializer.data)

# Delete
class ArticleDeleteAPIView(ArticleStaffNoRestrictionsQsMixin, ArticleHisPublicHisPrivateQsMixin, generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleInlineSerializer
    lookup_field = 'slug'

# class ArticleListCreateAPIView(generics.ListCreateAPIView):
#     # get->all post->authehticated
#     queryset = Article.objects.all()
#     serializer_class = ArticleInlineSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             if self.request.user.is_superuser:
#                 return ArticleAdminSerializer
#             return ArticleSerializer
#         return super().get_serializer_class()

#     def perform_create(self, serializer):
#         if self.request.user.is_superuser:
#             return serializer.save()
#         return serializer.save(author=self.request.user)