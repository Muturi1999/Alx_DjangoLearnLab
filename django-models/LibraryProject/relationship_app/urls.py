# relationship_app/urls.py

# from django.urls import path
# from . import views



# urlpatterns = [
#     # Function-based view URL
#     path('books/', views.book_list, name='book_list'),
    
#     # Class-based view URL
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
# ]

from django.urls import path
from .views import list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-Based View
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-Based View
]
