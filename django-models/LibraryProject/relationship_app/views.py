from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Book, Library  

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view: Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html' 
    context_object_name = 'library'  
