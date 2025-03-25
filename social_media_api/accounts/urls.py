from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserRegistrationView, 
    UserLoginView, 
    UserProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token-login/', obtain_auth_token, name='token-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]