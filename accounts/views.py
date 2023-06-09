from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import NewUserForm


def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    form = NewUserForm()
    return render(request, "registration/signup.html", {"form": form})


def home(request):
    return render(request, 'index.html')

# def logout(request):
#     logout(request)
#     return redirect('home')
