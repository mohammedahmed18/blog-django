from articles.views import add_article, article_page
from django.urls import path

urlpatterns = [
    path('<str:title>' , view=article_page , name='article_page'),
    path('article/new' , view=add_article , name="article_add")
]
