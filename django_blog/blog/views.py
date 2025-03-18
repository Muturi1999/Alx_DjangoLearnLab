from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms

# Custom Registration Form (Extends UserCreationForm)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# User Registration View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("profile")  # Redirect to profile page after registration
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# User Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("profile")  # Redirect to profile page after login
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

# Profile View (Requires Authentication)
@login_required
def profile(request):
    return render(request, "blog/profile.html")

def home(request):
    return render(request, "blog/home.html")

