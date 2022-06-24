from authors.storage import OverwriteStorage
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.
def get_avatar_image_path(self,author=None):
    return f'static/avatars/{self.pk}/avatar.png'

def get_avatar_image_path(instance, filename):
    return os.path.join('static/avatars', str(instance.pk), 'avatar.png')

def get_default_avatar():
    return 'static/defaults/avatar.png'



# create a new author 
class AuthorManager(BaseUserManager):
    def create_author(self , email , password , username):
        if not username:
            raise ValueError("username is missing")
        if not email:
            raise ValueError("username is missing")

        author = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        author.set_password(password)
        author.save()


    def create_superuser(self , email , password , username):
        if not username:
            raise ValueError("username is missing")
        if not email:
            raise ValueError("username is missing")

        author = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        author.set_password(password)
        author.is_admin = True
        author.is_staff = True
        author.is_superuser = True
        author.save()

class Author(AbstractBaseUser):
    username = models.CharField(unique=True , max_length=50)
    email = models.EmailField(verbose_name='email',unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateField(auto_now_add=True , null=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True , null=True)

    avatar = models.ImageField(upload_to=get_avatar_image_path , storage=OverwriteStorage(),null = True , blank = True , default=get_default_avatar)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    
    objects = AuthorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'password']
    def __str__(self) -> str:
        return self.username

    def get_profile_iamge_filename(self):
        return str(self.avatar)[str(self.avatar).index(f'avatars/{self.pk}/'):]


    def has_perm(self , perm , obj=None):
        return self.is_admin
    
    def has_module_perms(self , app_label):
        return True