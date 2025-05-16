from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')  # redirect to login 
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('browse_books')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('browse_books')
        else: 
            messages.error(request, "username or password is not valid! Try again!")
            return redirect('login')
        
    return render(request, 'auth/login.html')

def user_logout(request):
	logout(request)
	return redirect('login')