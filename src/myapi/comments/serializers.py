from rest_framework import serializers

from .models import Comment

# General - - - - - - - - - - - - - - - - - - - - #

class CommentInlineSerializer(serializers.ModelSerializer):
    author          = serializers.ReadOnlyField(source='author.username', default=None)
    url             = serializers.HyperlinkedIdentityField(view_name='api:comments:comment-detail', lookup_field='id', read_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'author', 'content']

class CommentSerializer(serializers.ModelSerializer):
    time            = serializers.SerializerMethodField('get_time') 
    textual         = serializers.SerializerMethodField ('get_textual') 
    url             = serializers.HyperlinkedIdentityField(view_name='api:comments:comment-detail', lookup_field='id', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'article', 'textual', 'time', 'url']

    def get_textual(self, obj):
        return {'author': obj.author.username, 'content': obj.content}
    
    def get_time(self, obj):
        return {'timestamp': obj.timestamp, 'updated': obj.updated}

# Post - - - - - - - - - - - - - - - - - - - - - - #

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'author', 'content']
        read_only_fields = ['article', 'author']

class StaffPostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'author', 'content']
        read_only_fields = ['article']

