# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  # ✅ Fixed to match the expected format
    except Author.DoesNotExist:
        return None

def list_library_books(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

def get_library_librarian(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)  # ✅ Fixed query
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return "No librarian assigned to this library"

# Example usage:
if __name__ == "__main__":
    # Query books by author
    author_books = query_books_by_author("John Doe")
    if author_books:
        print("Books by John Doe:", [book.title for book in author_books])

    # List library books
    library_books = list_library_books("Central Library")
    if library_books:
        print("Books in Central Library:", [book.title for book in library_books])

    # Get librarian
    librarian = get_library_librarian("Central Library")
    if librarian:
        print("Central Library's librarian:", librarian.name if isinstance(librarian, Librarian) else librarian)
