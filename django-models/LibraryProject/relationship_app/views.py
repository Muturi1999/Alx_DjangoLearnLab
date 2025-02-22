from django.shortcuts import render
from django.views.generic.detail import DetailView  
from .models import Library, Book

def list_books(request):
    """Lists all books with their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """Displays details for a specific library, listing all books available."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
