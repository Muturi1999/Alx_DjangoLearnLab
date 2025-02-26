from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for authors
        }