from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserRegistrationView, 
    UserLoginView, 
    UserProfileView,
    FollowUserView, 
    UnfollowUserView, 
    UserFollowersListView, 
    UserFollowingListView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token-login/', obtain_auth_token, name='token-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(),name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(),name='unfollow-user'),   
    # List followers and following
    path('followers/<int:user_id>/', UserFollowersListView.as_view(), name='user-followers' ),
    path('following/<int:user_id>/', UserFollowingListView.as_view(), name='user-following' ),
]
