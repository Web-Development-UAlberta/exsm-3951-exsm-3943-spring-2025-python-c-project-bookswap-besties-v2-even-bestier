from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    # Node: the email and password are inhertited from AbstractUser
    first_name = models.TextField(max_length=255, blank=False, null=False)
    last_name = models.TextField(max_length=255, blank=False, null=False)
    address = models.TextField(max_length=255, blank=False, null=False)
    genre_preference = models.TextField(max_length=255, null=True)
    
    wishlist_books = models.ManyToManyField('bookswap.Book', through='bookswap.WishList', related_name='wishlist_books')
    
    @property
    def unread_notification_count(self):
        from notifications.models import Notification
        return Notification.objects.filter(member=self, is_read=False).count()
    
    @property 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def library_items(self):
        from bookswap.models import LibraryItem
        return LibraryItem.objects.filter(member=self)
