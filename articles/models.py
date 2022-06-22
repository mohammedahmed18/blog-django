import zlib
from django.db import models
from authors.models import Author
# Create your models here.

def get_cover_image_path(self, article=None):
    return f'static/articles/{self}/cover.png'

class Comment(models.Model):
    author = models.ForeignKey(Author , on_delete=models.CASCADE)
    comment = models.TextField()


class Article(models.Model):
    author = models.ForeignKey(Author , on_delete=models.CASCADE , related_name='articles')
    title = models.CharField(max_length=65 , default="" , unique=True)
    date_published = models.DateField(auto_now_add = True)
    markdown = models.TextField()
    likes = models.IntegerField(default = 0)
    cover = models.ImageField(upload_to=get_cover_image_path)
    comments = models.ForeignKey(Comment , on_delete=models.CASCADE , default=None , null=True)
    def __str__(self) -> str:
        return self.title.replace(' ' , '-')

