from unicodedata import name
from articles.views import add_article, article_page, edit_article, get_article_comments, post_comment,mark_it_down
from django.urls import path

urlpatterns = [
    path('<str:title>' , view=article_page , name='article_page'),
    path('article/new' , view=add_article , name="article_add"),
    path('article/<str:title>/edit' , view=edit_article , name='article_edit'),
    path('article/comments' , view=get_article_comments , name='article_comments'),
    path('article/add_comment' , view=post_comment , name='add_comment'),
    path('markdown/html' , view=mark_it_down , name="mark_it_down")
]
