from rest_framework import serializers

from comments.serializers import CommentInlineSerializer
from .models import Article

# General - - - - - - - - - - - - - - - - - - - - #

class ArticleInlineSerializer(serializers.ModelSerializer):
    author  = serializers.ReadOnlyField(source='author.username', default=None)
    url     = serializers.HyperlinkedIdentityField(view_name='api:articles:article-detail', lookup_field='slug', read_only=True)

    class Meta:
        model = Article
        fields = ['url', 'slug', 'title', 'author', 'public']

# Get - - - - - - - - - - - - - - - - - - - - - - #

class GetArticleSerializer(serializers.ModelSerializer):
    comments    = serializers.SerializerMethodField('get_comments')
    id          = serializers.ReadOnlyField(source='slug')
    time        = serializers.SerializerMethodField('get_time') 
    textual     = serializers.SerializerMethodField ('get_textual') 
    url         = serializers.HyperlinkedIdentityField(view_name='api:articles:article-detail', lookup_field='slug', read_only=True)  

    class Meta:
        model = Article
        fields = ['id', 'textual', 'time', 'comments', 'public', 'url']
        read_only_fields = ['public']

    def get_comments(self, obj):
        request = self.context.get('request')
        return {'commentsUrl': request.build_absolute_uri(obj.get_comments_url()), 'commentsCount': self.get_comments_count(obj), 'lastComments': self.get_last_comments(obj)}

    def get_textual(self, obj):
        author = obj.author
        if author:
            author = author.username
        return {'title': obj.title, 'author': author, 'topic': self.get_topic(obj), 'content': obj.content}
    
    def get_time(self, obj):
        return {'timestamp': obj.timestamp, 'updated': obj.updated}

    def get_comments_count(self, obj):
        article = obj
        qs = article.get_number_of_comments()
        return qs      

    def get_last_comments(self, obj):        
        article = obj
        qs = article.get_comments()[:5]
        return CommentInlineSerializer(qs, many=True, context=self.context).data
    
    def get_topic(self, obj):
        return obj.get_topic_display()

# Post - - - - - - - - - - - - - - - - - - - - - - #

class PostArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'title', 'topic', 'content', 'public']
        read_only_fields = ['author']

class StaffPostArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'title', 'topic', 'content', 'public']

    # def update(self, instance, validated_data):
    #     print(instance)
    #     print(validated_data)
    #     return super().update(instance, validated_data)