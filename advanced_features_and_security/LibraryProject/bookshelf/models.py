from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Link to CustomUser model
        on_delete=models.CASCADE,
        related_name="books",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
