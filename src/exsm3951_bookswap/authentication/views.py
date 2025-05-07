from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('/')  # redirect to login 
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/library/')
        else: 
            messages.error(request, "username or password is not valid! Try again!")
            return redirect('/')
        
    return render(request, 'auth/login.html')

def user_logout(request):
	logout(request)
	return redirect('/')