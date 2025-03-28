from django.shortcuts import get_object_or_404, render, redirect
from .forms import BookForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from .models import Library, Book
# "relationship_app.can_change_book", "relationship_app.can_delete_book

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


# Book Views with permissions
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        # Create a new book instance and save it
        new_book = Book(title=title, author=author, published_date=published_date)
        new_book.save()

        return redirect('book_list')
    
    # "relationship_app.can_change_book", "relationship_app.can_delete_book
    # View to Edit a Book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})
# View to Delete a Book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})