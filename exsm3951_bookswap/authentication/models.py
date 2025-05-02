from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    # Node: the email and password are inhertited from AbstractUser
    first_name = models.TextField(max_length=255, blank=False, null=False)
    last_name = models.TextField(max_length=255, blank=False, null=False)
    address = models.TextField(max_length=255, blank=False, null=False)
    genre_preference = models.TextField(max_length=255, null=True)
    
    wishlist_books = models.ManyToManyField('bookswap.Book', through='bookswap.WishList', related_name='wishlist_books')
    