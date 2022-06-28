import zlib
from django.db import models
from authors.models import Author
from .storage import OverwriteStorage

def get_cover_image_path(self, article=None):
    return f'static/articles/{self.pk}/cover.png'



class Article(models.Model):
    author = models.ForeignKey(Author , on_delete=models.CASCADE , related_name='articles')
    title = models.CharField(max_length=65 , default="" , unique=True)
    date_published = models.DateField(auto_now_add = True)
    markdown = models.TextField()
    likes = models.IntegerField(default = 0)
    cover = models.ImageField(upload_to=get_cover_image_path,storage=OverwriteStorage())
    def __str__(self) -> str:
        return self.title.replace('%_%', ' ')

    def url_string(self):
        return self.title.replace('%_%' , '__')

class Comment(models.Model):
    author = models.ForeignKey(Author , on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='comments' ,default=None)
    def get_avatar(self):
        return self.author.avatar
    def get_author(self):
        return self.author

    def __str__(self) -> str:
        return self.comment