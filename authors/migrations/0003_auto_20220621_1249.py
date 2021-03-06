# Generated by Django 3.2.7 on 2022-06-21 10:49

import authors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_joined',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='hide_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='author',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='author',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='author',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(blank=True, default=authors.models.get_default_avatar, null=True, upload_to=authors.models.get_avatar_image_path),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
