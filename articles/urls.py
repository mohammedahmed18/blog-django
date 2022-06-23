from articles.views import add_article, article_page, get_article_comments, post_comment
from django.urls import path

urlpatterns = [
    path('<str:title>' , view=article_page , name='article_page'),
    path('article/new' , view=add_article , name="article_add"),
    path('article/comments' , view=get_article_comments , name='article_comments'),
    path('article/add_comment' , view=post_comment , name='add_comment')
]
