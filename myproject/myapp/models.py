from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)

    def __str__(self):
        return self.title


class Post_comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, verbose_name="コメント", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
