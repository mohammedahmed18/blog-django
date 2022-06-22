from authors.models import Author
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



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
            username = req.POST.get('username')
            password = req.POST.get('password')
            author = Author.objects.get(username = username)
            # check for password
            password_correct = Author.check_password(author , password)
            if not password_correct:
                raise ObjectDoesNotExist                

            auth.login(req ,author)
            return redirect('/')        
        except ObjectDoesNotExist as e :
            return render(req,'authors/login.html',{'error' : 'username or password is incorrect'})

   