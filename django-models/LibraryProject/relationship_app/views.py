# from django.shortcuts import render,redirect
# from django.views.generic.detail import DetailView  
# from .models import Library, Book
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# def list_books(request):
#     """Lists all books with their authors."""
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})

# class LibraryDetailView(DetailView):
#     """Displays details for a specific library, listing all books available."""
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'



# def user_login(request):
#     """Handles user login"""
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("list_books")  # Redirect to book listing page
#     else:
#         form = AuthenticationForm()
    
#     return render(request, "relationship_app/login.html", {"form": form})

# def user_logout(request):
#     """Handles user logout"""
#     logout(request)
#     return render(request, "relationship_app/logout.html")

# def register(request):
#     """Handles user registration"""
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("list_books")  # Redirect to book listing page
#     else:
#         form = UserCreationForm()
    
#     return render(request, "relationship_app/register.html", {"form": form})
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView  
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Library, Book

def list_books(request):
    """Lists all books with their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """Displays details for a specific library, listing all books available."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def user_login(request):
    """Handles user login."""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("relationship_app:list_books")
    else:
        form = AuthenticationForm()
    
    return render(request, "relationship_app/login.html", {"form": form})

@login_required
def user_logout(request):
    """Handles user logout."""
    logout(request)
    return redirect("relationship_app:login") 

# def register(request):
#     """Handles user registration."""
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("relationship_app:list_books")  # ✅ Namespaced URL
#     else:
#         form = UserCreationForm()
    
#     return render(request, "relationship_app/register.html", {"form": form})
def register(request):
    """Handles user registration"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("relationship_app:list_books")  # Redirect after successful registration
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})