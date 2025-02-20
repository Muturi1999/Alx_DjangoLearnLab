# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView, ListView
# Make sure this exact import is present
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Make sure to explicitly use DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context