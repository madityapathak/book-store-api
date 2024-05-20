from django.contrib import admin
from .models import User,Book,Author,Review


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email']

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Review)