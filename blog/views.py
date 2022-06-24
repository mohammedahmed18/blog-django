from articles.models import Article
from django.shortcuts import render


def homePage(req):
    articles = Article.objects.order_by('-pk')
    return render(req , 'blog/index.html' , {'articles' : articles})