from django.conf import settings
from django.db import models

from articles.models import Article

User = settings.AUTH_USER_MODEL

# - - - - - - - - - - - - - - - - - - - Comment - - - - - - - - - - - - - - - - - - - - #

class Comment(models.Model):
    author      = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    article     = models.ForeignKey(Article, on_delete=models.CASCADE)
    content     = models.TextField()
    
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-timestamp"]
        
    def __str__(self):
        return f"Comment [{self.id}]"