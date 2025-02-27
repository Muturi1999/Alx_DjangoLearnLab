from django.urls import path
from . import views
from .views import example_form_view


urlpatterns = [
    # Function-based view URLs
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/new/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('example-form/', example_form_view, name='example_form'),

    
    # Alternatively, you can use the class-based view URLs
    # path('books/', views.BookListView.as_view(), name='book_list'),
    # path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    # path('books/new/', views.BookCreateView.as_view(), name='book_create'),
    # path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    # path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]