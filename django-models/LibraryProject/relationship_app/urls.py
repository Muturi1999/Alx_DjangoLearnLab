# relationship_app/urls.py
from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # URL pattern for function-based view
    path('books/', views.book_list, name='book_list'),
    
    # URL patterns for class-based views
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]