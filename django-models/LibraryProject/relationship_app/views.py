from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    
    # Pass the books to the template for rendering
    context = {
        'books': books
    }
    
    # Render the list_books.html template with the books data
    return render(request, 'relationship_app/list_books.html', context)

    

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        # Get the base context from the parent class
        context = super().get_context_data(**kwargs)
        
        # Add any additional context if needed
        # For example, you could add a count of books
        context['book_count'] = self.object.books.count()
        
        return context