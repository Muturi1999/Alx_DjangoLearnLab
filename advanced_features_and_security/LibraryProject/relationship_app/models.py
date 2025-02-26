from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    class Meta:
        permissions = [
            ('can_add_book', 'Can add a book'),
            ('can_change_book', 'Can update a book'),
            ('can_delete_book', 'Can delete a book')
        ]

class Library(models.Model):
    name = models.CharField(max_length=200, unique=True)
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return f"{self.name} (Librarian at {self.library.name})"

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")  # Use AUTH_USER_MODEL
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.email} - {self.role}"  # Use email instead of username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # Ensure correct signal sender
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'profile'):
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
