from .views import author_profile, login, logout
from django.urls import path

urlpatterns = [
    path('logout' , view=logout , name='author_logout'),
    path('login' , view=login , name='author_login'),
    path('<str:username>/profile' , view=author_profile , name="author_profile")
]
