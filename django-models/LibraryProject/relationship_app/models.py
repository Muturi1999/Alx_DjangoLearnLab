from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField(null=True, blank=True)  # Adding this field
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Adding related_name
    
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='libraries')  # Adding related_name
    
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name