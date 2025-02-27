# from django.db import models
# from django.conf import settings  # Import settings to reference AUTH_USER_MODEL
# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     publication_year = models.IntegerField()
#     owner = models.ForeignKey(
#         settings.AUTH_USER_MODEL,  # Link to CustomUser model
#         on_delete=models.CASCADE,
#         related_name="books",
#         null=True,
#         blank=True
#     )

#     def __str__(self):
#         return f"{self.title} by {self.author} ({self.publication_year})"

# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Fix conflicting related names
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    owner = models.ForeignKey(
        CustomUser,  # Link to CustomUser model
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
