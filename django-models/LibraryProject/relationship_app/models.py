from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensures author names are unique
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Ensures book titles are unique
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'
    )
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"  # Improved string representation

class Library(models.Model):
    name = models.CharField(max_length=200, unique=True)  # Library names should be unique
    books = models.ManyToManyField(
        Book, 
        related_name='libraries', 
        blank=True  # Allows a library to have no books initially
    )
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,  
        on_delete=models.CASCADE, 
        related_name='librarian'
    )
    
    def __str__(self):
        return f"{self.name} (Librarian at {self.library.name})"  
