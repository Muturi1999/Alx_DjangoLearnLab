# from django.urls import path
# from .views import list_books, LibraryDetailView
# from django.contrib.auth import views as auth_views
# from .views import user_login, user_logout, register


# app_name = 'relationship_app'

# urlpatterns = [
#     path('books/', list_books, name='list_books'),  # Function-Based View
#     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
#     path("login/", user_login, name="login"),
#     path("logout/", user_logout, name="logout"),
#     path("register/", register, name="register"),
# ]
# from django.urls import path
# from .views import list_books, LibraryDetailView, user_login, user_logout, register

# app_name = 'relationship_app' 

# urlpatterns = [
#     path('books/', list_books, name='list_books'),
#     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
#     path("login/", user_login, name="login"),
#     path("logout/", user_logout, name="logout"),
#     path("register/", register, name="register"),
# ]
# from django.urls import path
# from .views import user_login, user_logout, register, list_books, LibraryDetailView

# app_name = 'relationship_app' 

# urlpatterns = [
#     path("login/", user_login, name="login"),
#     path("logout/", user_logout, name="logout"),
#     path("register/", register, name="register"),  
#     path("books/", list_books, name="list_books"),
#     path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
# ]
# Roll back to this for it was working for task two

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register, admin_view, librarian_view, member_view
from LibraryProject.relationship_app import views
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'relationship_app'

urlpatterns = [
    # Authentication views using Django's built-in views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), template_name="relationship_app/logout.html"),
    path("register/", views.register, name="register"),

    # Role-based dashboard views
    path("admin/dashboard/", admin_view, name="admin_dashboard"),
    path("librarian/dashboard/", librarian_view, name="librarian_dashboard"),
    path("member/dashboard/", member_view, name="member_dashboard"),

    # Book and library views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]
