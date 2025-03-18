# from django.urls import path
# from .views import (
#     register, user_login, user_logout, profile, home,
#     PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
# )

# urlpatterns = [
#     path("", home, name="home"),
#     path("register/", register, name="register"),
#     path("login/", user_login, name="login"),
#     path("logout/", user_logout, name="logout"),
#     path("profile/", profile, name="profile"),
    
#     # Blog Post URLs
#     path("posts/", PostListView.as_view(), name="post-list"),
#     path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
#     path("posts/new/", PostCreateView.as_view(), name="post-create"),
#     path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),
#     path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
# ]
from django.urls import path
from .views import (
    register, user_login, user_logout, profile, home,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView, add_comment
)

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    
    # Blog Post URLs 
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"), 
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), 
     
    # Comment URLs
    path("posts/<int:pk>/comments/new/", add_comment, name="add-comment"),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"), 
     
     ]
