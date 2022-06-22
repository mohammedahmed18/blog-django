from .models import Article
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'cover' , 'markdown' )
# Register your models here.
admin.site.register(Article , ArticleAdmin)