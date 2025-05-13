from django.db import models
from authentication.models import Member
 
"""
Everytime a book is listed:
1. Get all users who have the book in their wishlist
2. Create a notification record for each user about that book listing
3. Display to the user in the notifications page all the notification


Adding a book to wishlist that already has a listing:
1. User adds a book to their wishlist
2. Check if the book already has a listing(s)
3. Create a notification to user if it does
4. Display the notification on the notifications page
"""

class Notification(models.Model):
    # have to add to member inside brackets related_name='notifications' for counting notificatons
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='notifications')  
    message = models.TextField()
    title = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    