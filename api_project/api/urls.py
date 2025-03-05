# from django.urls import path
# from .views import BookList

# urlpatterns = [
#     path('books/', BookList.as_view(), name='book-list'),
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet, BookList


# router = DefaultRouter()
# router.register(r'books_all', BookViewSet, basename='book_all')

# urlpatterns = [
#     path('books/', BookList.as_view(), name='book-list'),
#     path('', include(router.urls)), 
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Registers BookViewSet

# Define urlpatterns properly
urlpatterns = [
    path('', include(router.urls)),  # Includes all ViewSet-generated URLs
]
