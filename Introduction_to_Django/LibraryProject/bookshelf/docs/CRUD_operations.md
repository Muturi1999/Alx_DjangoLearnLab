<!-- creating a book instance  -->
from bookshelf.models import Book

book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book1)


<!-- retriveing/getting existing book instance -->
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

<!-- updating the book instance  -->
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")


<!-- deleting a book  -->
book.delete()
print(Book.objects.all())
