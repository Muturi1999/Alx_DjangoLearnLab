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
# urls.py
from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Authentication URLs
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.register, name="register"),
    
    # Application URLs
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
