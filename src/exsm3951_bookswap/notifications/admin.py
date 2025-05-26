from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'member', 'title', 'message', 'is_read', 'timestamp']
    
    
admin.site.register(Notification, NotificationAdmin)
    