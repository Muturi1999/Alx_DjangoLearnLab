# from rest_framework import generics, permissions
# from .models import Book
# from .serializers import BookSerializer

# # List all books (Read)
# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # Retrieve a single book by ID (Read)
# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# # Create a new book (Create)
# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

# # Update an existing book (Update)
# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

# # Delete a book (Delete)
# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

from datetime import datetime
from rest_framework import generics, permissions, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # Explicitly importing both
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Handles listing all books.
    Available to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Available to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Handles creating new book entries.
    Only authenticated users can create books.
    Includes validation to prevent future publication years.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Explicit usage of IsAuthenticated

    def perform_create(self, serializer):
        """Ensure publication_year is not in the future before saving."""
        if serializer.validated_data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Handles updating an existing book entry.
    Only authenticated users can update books.
    Includes validation to prevent future publication years.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Explicit usage of IsAuthenticated

    def perform_update(self, serializer):
        """Ensure publication_year is not updated to a future date."""
        if serializer.validated_data.get('publication_year', datetime.now().year) > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deleting a book entry.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Explicit usage of IsAuthenticated
