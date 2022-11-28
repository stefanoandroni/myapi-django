from autoslug import AutoSlugField

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse

User = settings.AUTH_USER_MODEL

# - - - - - - - - - - - - - - - - - - - Article - - - - - - - - - - - - - - - - - - - - #

class ArticleTopic(models.TextChoices):
    CHRONICLE   = "c", "Chronicle"
    POLITICS    = "p", "Politics"
    SPORT       = "s", "Sport"
    ECONOMY     = "e", "Economy"

class ArticleQuerySet(models.QuerySet):
    def is_public(self):
         return self.filter(public=True)
    
    def search(self, query, user=None, author=None, topic=None):
        lookup = (Q(title__icontains=query) | Q(content__icontains=query))
        if author is not None:
            lookup &= Q(author__username=author)
        if topic is not None:
            lookup &= Q(topic=topic)
        qs = self.is_public().filter(lookup)
        if user is not None: 
            qs2 = self.filter(author=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ArticleManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query, author=None, topic=None):
        return self.get_queryset.search(query, user=None, author=None, topic=None)

class Article(models.Model):
    slug            = AutoSlugField(primary_key=True, populate_from='title') 
    author          = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    title           = models.CharField(max_length=120) 
    topic           = models.CharField(max_length=1, choices=ArticleTopic.choices, default=ArticleTopic.CHRONICLE)
    content         = models.TextField()
    public          = models.BooleanField(default=False)

    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    objects         = ArticleManager()

    class Meta:
        ordering = ["-timestamp"]
    
    @property
    def name(self):
        return self.title
    
    @property
    def user(self):
        return self.author

    def __str__(self):
        return f"Article [{self.title}] ({self.author})"
    
    def set_public(self, public=True):
        self.public = public
        return public

    def get_comments(self):
        qs = self.comment_set.all().order_by('-timestamp')
        return qs

    def get_comments_url(self):
        kwargs = {
            "slug": self.slug  
        }
        return reverse('api:comments:article-comment-list', kwargs=kwargs)

    def get_number_of_comments(self):
        qs = self.comment_set.all().count()
        return qs