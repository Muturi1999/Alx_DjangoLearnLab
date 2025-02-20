# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Function-based view URL
    path('books/', views.list_books, name='book_list'),
    
    # Class-based view URL
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]