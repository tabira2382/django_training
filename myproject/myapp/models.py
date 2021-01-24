from django.db import models


class Post(models.Model):
    title = models.CharField('タイトル', max_length=50)
    comment = models.TextField('コメント', max_length=1000)

    def comment_number(self):
        n = Post.objects.filter(comment=self).count()
        return n

    def __str__(self):
        return self.title
