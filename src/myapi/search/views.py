from django.shortcuts import render

from rest_framework import generics

from articles.models import Article
from articles.serializers import GetArticleSerializer

class SearchListView(generics.ListAPIView): # on Article (to generalize)
    '''
        /GET parameters/
       *q       (contains)    [title, content (case insensitive)]
        topic   (equal)      
        author  (equal)

        * required
    '''
    queryset = Article.objects.all()
    serializer_class = GetArticleSerializer

    def get_queryset(self, *args, **kwargs): #add user as parameter
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        q = request.GET.get('q')
        topic = request.GET.get('topic')
        author = request.GET.get('author')
        results = Article.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = request.user
            results = qs.search(q, user=user, author=author, topic=topic)
        return results