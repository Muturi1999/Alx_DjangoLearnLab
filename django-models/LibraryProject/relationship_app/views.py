# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
# Explicitly import models
from .models import Book, Library

def book_list(request):
    """Function-based view for listing all books"""
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })

class LibraryDetailView(DetailView):
    """Class-based view for displaying library details"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all().select_related('author')
        return context