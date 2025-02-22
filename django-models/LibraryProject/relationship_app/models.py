from django.db import models
# from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        related_name='librarian'  # Allows reverse querying: `library.librarian`
    )

    @staticmethod
    def get_librarian_by_library(library_instance):
        """Retrieve librarian for a given library instance."""
        try:
            return Librarian.objects.get(library=library_instance)
        except Librarian.DoesNotExist:
            return None

    def __str__(self):
        return f"{self.name} (Librarian at {self.library.name})"
    

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

