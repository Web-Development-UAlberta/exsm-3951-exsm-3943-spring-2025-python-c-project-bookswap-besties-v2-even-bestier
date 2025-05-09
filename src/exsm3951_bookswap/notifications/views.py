from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Placeholder code, feel free to replace all
@login_required
def notifications_view(request):

    notifications = []

    return render(request, "notifications/index.html", {
        "notifications": notifications
    })