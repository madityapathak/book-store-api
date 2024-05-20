from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Author(models.Model):
    name = models.CharField(max_length=35)
    bio = models.CharField(max_length=70)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=35)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField()
    isbn = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False,blank=False,related_name='book_reviews')
    rating = models.IntegerField(null=False,blank=False)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True,null=True,blank=True)