from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(blank=True, null=True)
    hits = models.IntegerField(default=0)

    def save_article(self):
        self.modified_at = timezone.now()
        self.save()


class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(blank=True, null=True)
    article = models.ForeignKey(
        'Article',
        related_name='article_comments',
        on_delete=models.CASCADE
    )

    def save_comment(self):
        self.modified_at = timezone.now()
        self.save()