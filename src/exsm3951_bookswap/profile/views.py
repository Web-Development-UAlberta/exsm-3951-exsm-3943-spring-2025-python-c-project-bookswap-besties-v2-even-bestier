from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomEditUserForm
from authentication.models import Member
from django.contrib import messages


@login_required
def profile_settings_view(request):
    user = request.user
    if request.method == 'POST':
        form = CustomEditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_settings')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomEditUserForm(instance=user)
    
    context = {'form': form}
    return render(request, "profile/settings.html", context)
