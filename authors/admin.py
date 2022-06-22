from django.contrib import admin
from authors.models import Author

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('email' , 'username' , 'date_joined' , 'is_admin' , 'is_staff')
    search_fields = ('email' , 'username')
    readonly_fields = ('password' , 'date_joined' , 'last_login' , 'id')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Author , AuthorAdmin)