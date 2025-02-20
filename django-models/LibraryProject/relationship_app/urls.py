from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # URL pattern for the function-based view
    path('books/', views.list_books, name='book_list'),
    
    # URL pattern for the class-based view
    # The <int:pk> captures a numeric parameter from the URL and passes it as 'pk'
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]