# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Library  # Explicitly import Library model

# Function-based view
def book_list(request):
    """
    Function-based view to display all books
    """
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based views
class LibraryListView(ListView):
    """
    Class-based view to display list of libraries
    """
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'

class LibraryDetailView(DetailView):
    """
    Class-based view to display library details
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        context['books'] = self.object.books.all().select_related('author')
        return context