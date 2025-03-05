# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer
# from rest_framework import viewsets

# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all() 
#     serializer_class = BookSerializer 


# class BookViewSet(viewsets.ModelViewSet):
#     """
#     A ViewSet for performing CRUD operations on the Book model.
#     """
#     queryset = Book.objects.all() 
#     serializer_class = BookSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    Only authenticated users can access this.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]  # Allow only admins to modify
