from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .models import Library, Book

def user_login(request):
    """Handles user login."""
    if request.user.is_authenticated:
        return redirect("relationship_app:list_books")

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("relationship_app:list_books")
    else:
        form = AuthenticationForm()
    
    return render(request, "relationship_app/login.html", {"form": form})

def register(request):
    """Handles user registration."""
    if request.user.is_authenticated:
        return redirect("relationship_app:list_books")

    if request.method == "POST":
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("relationship_app:list_books")
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})

@login_required
def user_logout(request):
    """Handles user logout."""
    logout(request)
    return redirect("relationship_app:login")

@login_required
def list_books(request):
    """Lists all books with their authors."""
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(LoginRequiredMixin, DetailView):
    """Displays details for a specific library, listing all books available."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all().select_related('author')
        return context
