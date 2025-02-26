from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views  

app_name = 'relationship_app'

urlpatterns = [
    # Authentication views
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    # Role-based dashboards
    path("admin/dashboard/", views.admin_view, name="admin_dashboard"),
    path("librarian/dashboard/", views.librarian_view, name="librarian_dashboard"),
    path("member/dashboard/", views.member_view, name="member_dashboard"),

    # Book views
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # CRUD operations
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
