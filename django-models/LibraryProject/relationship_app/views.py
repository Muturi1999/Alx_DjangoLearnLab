from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Library, Book

# Role-based access control functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Register view (Using built-in Django UserCreationForm)
def register(request):
    if request.user.is_authenticated:
        return redirect("relationship_app:list_books")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("relationship_app:list_books")
    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})

# Book listing
@login_required
def list_books(request):
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Library detail view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all().select_related('author')
        return context

# ==============================
# 🚀 Role-Based Access Views
# ==============================

@login_required
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    """View for Admin users only."""
    return render(request, "relationship_app/admin_view.html")

@login_required
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """View for Librarian users only."""
    return render(request, "relationship_app/librarian_view.html")

@login_required
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """View for Member users only."""
    return render(request, "relationship_app/member_view.html")
