from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BasePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.title)
    

class Post(BasePost):

    @property
    def comments(self):
        return self.comments_set.all()


class Comment(BasePost):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
