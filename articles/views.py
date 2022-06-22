from django.http import JsonResponse
from articles.models import Article
from django.shortcuts import redirect, render
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def article_page(req , title):
    article = Article.objects.get(title = title.replace('-' , ' '))
    return render(req ,'articles/articlepage.html' , {'article' : article})

@login_required()
def add_article(req):
    form = ArticleForm(req.POST or None ,files=req.FILES or None)
    if req.method == 'GET':
        return render(req , 'articles/create.html' , {'form' : form})
    if req.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            article.author = req.user
            article.save()
            return redirect('/')
    
    return render(req , 'articles/create.html' , {'form' : form})
    