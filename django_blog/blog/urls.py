from django import views
from django.urls import path
from .views import register, user_login, user_logout, profile, home

urlpatterns = [
    path("", home, name="home"), 
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
]
