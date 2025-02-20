import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Use `.get()`
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return []

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Use `.get()`
        return [book.title for book in library.books.all()]
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Ensure library exists
        librarian = Librarian.objects.get(library=library)  # Use `.get()` on Librarian model
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Sample Usage
if __name__ == '__main__':
    print("Books by Author 'John Doe':", books_by_author("John Doe"))
    print("Books in 'Central Library':", books_in_library("Central Library"))
    print("Librarian of 'Central Library':", librarian_of_library("Central Library"))
