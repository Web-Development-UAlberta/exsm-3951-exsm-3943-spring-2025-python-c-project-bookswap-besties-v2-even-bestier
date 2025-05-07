from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_settings_view(request):
    return render(request, "profile/settings.html")