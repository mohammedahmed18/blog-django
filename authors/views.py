from authors.models import Author
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import Http404



@login_required
def logout(req):
    if req.method == 'POST':
        method = req.POST.get('_method', '').lower()
        if method == 'delete':
            auth.logout(req)
            return redirect('/')



def login(req):

    if req.user.is_authenticated:
        return redirect('/')

    if req.method == 'GET':
        return render(req,'authors/login.html')
    if req.method == 'POST':
        try:
            email = req.POST.get('email')
            password = req.POST.get('password')
            author = Author.objects.get(email = email)
            # check for password
            password_correct = Author.check_password(author , password)
            if not password_correct:
                raise ObjectDoesNotExist                

            auth.login(req ,author)
            return redirect('/')        
        except ObjectDoesNotExist as e :
            return render(req,'authors/login.html',{'error' : 'username or password is incorrect'})



def author_profile(req , username):
    try: 
        author_username = username.replace('-' , ' ')
        author = Author.objects.get(username = author_username)
        author_articles = author.articles
        context = {
            'author' : author,
            'author_articles' : author_articles
        }
        return render(req , 'authors/authorprofile.html' ,context)
    except ObjectDoesNotExist:
        raise Http404
