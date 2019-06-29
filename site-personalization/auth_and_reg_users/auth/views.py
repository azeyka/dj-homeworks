from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout

from .forms import SignUpForm, LoginForm

def home(request):
    return render(
        request,
        'home.html',
    )


def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username, 'email', password)

            return redirect('/login/')

    return render(
        request,
        'signup.html',
        {
            'form': form
        }
    )

def login(request):
    form = LoginForm()
    error = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(f'/')
            else:
                error = True
    return render(
        request,
        'login.html',
        {
            'form': form,
            'error': error
        }
    )


def logout(request):
    auth_logout(request)

    return render(
        request,
        'logout.html',
    )