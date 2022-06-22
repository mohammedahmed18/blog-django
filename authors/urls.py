from .views import login, logout
from django.urls import path

urlpatterns = [
    path('logout' , view=logout , name='author_logout'),
    path('login' , view=login , name='author_login'),
]
