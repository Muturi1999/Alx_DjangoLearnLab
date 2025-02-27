# from django import forms
# from .models import Book

# class BookForm(forms.ModelForm):
#     """Form for creating and editing Book instances"""
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'publication_year']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.TextInput(attrs={'class': 'form-control'}),
#             'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """Form for creating and editing Book instances"""
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ExampleForm(forms.Form):
    """Dummy form to satisfy external dependencies"""
    example_field = forms.CharField(max_length=255, required=True)
