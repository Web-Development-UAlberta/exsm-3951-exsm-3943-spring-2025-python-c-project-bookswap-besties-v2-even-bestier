from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification

# Placeholder code, feel free to replace all
@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(member=request.user)
    return render(request, "notifications/index.html", {
        "notifications": notifications
    })
    
@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.is_read = True
    notification.save()
    return redirect("notifications")

#count messages for notification badge
register = template.Library()

@register.simple_tag
def unread_messages(member):
    return Notification.objects.filter(member=member, is_read=False).count()



