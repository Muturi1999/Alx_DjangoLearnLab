# relationship_app/query_samples.py

# Import necessary models
from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        # Find author by name
        author = Author.objects.get(name=author_name)
        # Get all books by this author using filter()
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []

def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        # Find library by name
        library = Library.objects.get(name=library_name)
        # Get all books in this library
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        # Find library by name
        library = Library.objects.get(name=library_name)
        # Get the librarian for this library
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

# Example usage (uncomment to test)
'''
# First create some sample data
def create_sample_data():
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter", author=author1)
    book2 = Book.objects.create(title="1984", author=author2)
    book3 = Book.objects.create(title="Animal Farm", author=author2)
    
    # Create libraries
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="City Library")
    
    # Add books to libraries
    library1.books.add(book1, book2)
    library2.books.add(book2, book3)
    
    # Create librarians
    librarian1 = Librarian.objects.create(name="John Smith", library=library1)
    librarian2 = Librarian.objects.create(name="Jane Doe", library=library2)

# Run queries
if __name__ == '__main__':
    # Uncomment to create sample data
    # create_sample_data()
    
    # Query books by author
    rowling_books = query_books_by_author("J.K. Rowling")
    print("Books by J.K. Rowling:")
    for book in rowling_books:
        print(f"- {book.title}")
    
    # List books in library
    central_books = list_books_in_library("Central Library")
    print("\nBooks in Central Library:")
    for book in central_books:
        print(f"- {book.title} by {book.author.name}")
    
    # Get librarian for library
    city_librarian = get_librarian_for_library("City Library")
    print(f"\nLibrarian for City Library: {city_librarian.name if city_librarian else 'None'}")
'''