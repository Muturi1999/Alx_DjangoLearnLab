# relationship_app/urls.py
from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='book_list'),
    
    # Class-based view for library details
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Index view
    path('', views.index, name='index'),
]