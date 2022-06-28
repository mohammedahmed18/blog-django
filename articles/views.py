from django.http import JsonResponse , HttpResponse
from articles.models import Article
from django.shortcuts import redirect, render
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from blog.templatetags.markdown_extras import markdown


# Create your views here.
def article_page(req , title):
    article = Article.objects.get(title = title.replace('__' , '%_%'))
    author = article.author
    author_username = author.username.replace(' ' , '-')
    comment_form = CommentForm()
    context = {
        'article' : article,
        'author_username' : author_username,
        'author' : author,
        'comment_form' : comment_form
    }
    return render(req ,'articles/articlepage.html' , context)

@login_required()
def add_article(req):
    form = ArticleForm(req.POST or None ,files=req.FILES or None)
    if req.method == 'GET':
        return render(req , 'articles/create.html' , {'form' : form})
    if req.method == 'POST':
        if form.is_valid():
            article = form.save(commit=False)
            article.author = req.user
            if '_' in article.title:
                return render(req , 'articles/create.html' , {'form' : form , "error" : "article title can't contains underscores"})

            article.title = article.title.replace(' ' , '%_%')
            article.save()
            return redirect('/')
    
    return render(req , 'articles/create.html' , {'form' : form})


def auth_author(req,article):
    if article.author != req.user:
        return False
    return True


@login_required()
def edit_article(request , title):
    if request.method == 'GET':
        article = Article.objects.get(title = title.replace('__' , '%_%'))
        if not auth_author(request , article):
            return JsonResponse({"msg" : "not authorized"},status = 401)
        instance_article = article
        instance_article.title = instance_article.title.replace('%_%' , ' ') 
        form = ArticleForm(instance=instance_article)
        return render(request , 'articles/edit.html' , {'form' : form , 'article' : article})
    if request.method == 'POST' and request.POST.get('_method', '').lower() == 'put':
        _article = Article.objects.get(title = title.replace(' ' , '%_%'))
        if not auth_author(request , _article):
            return JsonResponse({"msg" : "not authorized"},status = 401)
        form = ArticleForm(request.POST,request.FILES ,instance=_article)
        article = form.save(commit=False)
        article.author = request.user
        if '_' in article.title:
            return render(request , 'articles/edit.html' , {'form' : form , "error" : "article title can't contains underscores"})

        article.title = article.title.replace(' ' , '%_%')
        article.save()
        return redirect('article_page',title=_article.url_string())

def get_article_comments(req):
     # req should be ajax and method should be GET.
    if req.is_ajax and req.method == "GET":
        article_title = req.GET.get("article_title", None)
        # get the article
        try:
            article = Article.objects.get(title = article_title)
            # article is found
            
            # comments = []
            # for comment in article.comments.all():
            #     comments.append({
            #         "comment" : comment.comment,
            #         'author' : {
            #             'username' :str(comment.get_author()),
            #             'avatar' : str(comment.get_avatar()) 
            #         }
            #     })

            comments =article.comments.order_by('-pk')
            data = comments.values(
                'comment',
                'author__username',
                'author__avatar'
            )

            return JsonResponse(list(data), status = 200 , safe=False)

        except ObjectDoesNotExist:
            return JsonResponse({"msg":"article doesn't exist"}, status = 404)


    return JsonResponse({}, status = 400)


@login_required()
def post_comment(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = CommentForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article_id = request.POST.get('article_id')
            comment.save()
            # send to client side.
            return JsonResponse({"comment": str(comment) , 'author__username' : str(comment.author) , 'author__avatar' : str(comment.author.avatar)}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

@login_required()
def mark_it_down(req):
     # req should be ajax and method should be GET.
    if req.is_ajax and req.method == "GET":
        markdown_raw = req.GET.get("markdown", None)
        html = markdown(markdown_raw)
        return JsonResponse({'html' : html}, status = 200 , safe=False)

        
    return JsonResponse({}, status = 400)



