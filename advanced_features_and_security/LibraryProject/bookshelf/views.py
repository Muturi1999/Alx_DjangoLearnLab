from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Book, CustomUser
from .forms import BookForm  # You'll need to create this form

# Function-based views with permission decorators

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """Display a list of all books (requires can_view permission)"""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_detail(request, pk):
    """Display details of a specific book (requires can_view permission)"""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """Create a new book (requires can_create permission)"""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user  # Associate the book with the current user
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """Edit an existing book (requires can_edit permission)"""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """Delete a book (requires can_delete permission)"""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# Class-based views with permission mixins

class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Class-based view to list all books (requires can_view permission)"""
    model = Book
    permission_required = 'bookshelf.can_view'
    context_object_name = 'books'
    template_name = 'bookshelf/book_list.html'

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Class-based view to display book details (requires can_view permission)"""
    model = Book
    permission_required = 'bookshelf.can_view'
    context_object_name = 'book'
    template_name = 'bookshelf/book_detail.html'

class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Class-based view to create a new book (requires can_create permission)"""
    model = Book
    permission_required = 'bookshelf.can_create'
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Class-based view to update a book (requires can_edit permission)"""
    model = Book
    permission_required = 'bookshelf.can_edit'
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Class-based view to delete a book (requires can_delete permission)"""
    model = Book
    permission_required = 'bookshelf.can_delete'
    template_name = 'bookshelf/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')