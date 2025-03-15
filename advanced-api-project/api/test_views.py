from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book, Author

class BookAPITestCase(TestCase):
    """Test case for Book API endpoints."""
    
    def setUp(self):
        """Set up test data before running each test."""
        self.client = APIClient()
        
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create test authors
        self.author_a = Author.objects.create(name="Author A")
        self.author_b = Author.objects.create(name="Author B")
        self.author_c = Author.objects.create(name="Author C")

        # Create test books
        self.book1 = Book.objects.create(title="Book One", author=self.author_a, publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author=self.author_b, publication_year=2021)

        # API endpoints
        self.book_list_url = "/api/books/"
        self.book_detail_url = f"/api/books/{self.book1.id}/"
        self.book_create_url = "/api/books/create/"
    
    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_authenticated(self):
        """Test creating a book while authenticated using login."""
        self.client.login(username='testuser', password='password123')  # ✅ Added login authentication
        data = {"title": "New Book", "author": self.author_c.id, "publication_year": 2023}
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication."""
        data = {"title": "New Book", "author": self.author_c.id, "publication_year": 2023}
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Test updating a book while authenticated using login."""
        self.client.login(username='testuser', password='password123')  # ✅ Added login authentication
        data = {"title": "Updated Book", "author": self.author_a.id, "publication_year": 2025}
        response = self.client.patch(self.book_detail_url, data, format="json")  # ✅ Changed to PATCH
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_authenticated(self):
        """Test deleting a book while authenticated using login."""
        self.client.login(username='testuser', password='password123')  # ✅ Added login authentication
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.book_list_url}?title=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book One")

    def test_search_books(self):
        """Test searching for books."""
        response = self.client.get(f"{self.book_list_url}?search=Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[1]['publication_year'], 2021)
