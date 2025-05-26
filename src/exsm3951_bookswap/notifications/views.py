from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification


@login_required
def notifications_view(request):
    notifications = Notification.objects.filter(member=request.user).order_by('-timestamp')
    return render(request, "notifications/index.html", {
        "notifications": notifications
    })
    
@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.is_read = True
    notification.save()
    return redirect("notifications")

@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id, member=request.user)
    notification.delete()
    return redirect("notifications")

