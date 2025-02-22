# relationship_app/urls.py

from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view URL
    path('books/', views.book_list, name='book_list'),
    
    # Class-based view URL
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]