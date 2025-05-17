from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomEditUserForm
from authentication.models import Member
from django.contrib import messages

@login_required
def profile_settings_view(request):
    return render(request, "profile/settings.html")

@login_required
def update_account(request, pk):
    user = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        post_data = request.POST.copy()
        form = CustomEditUserForm(post_data, isinstance=user)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        #finish entering fields here

        messages.success(request, "Profile updated successfully!")
        return redirect('library') #where should we redirect to?
    else:
        form = CustomEditUserForm(isinstance=user)
        context = {
            'form': form,
        }
    return render(request, 'profile/settings.html', context)