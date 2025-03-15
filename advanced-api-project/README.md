# Advanced API Project

## API Endpoints
- `GET /api/books/` → List all books (Public)
- `GET /api/books/<id>/` → Get book details (Public)
- `POST /api/books/create/` → Create book (Authenticated)
- `PUT /api/books/<id>/update/` → Update book (Authenticated)
- `DELETE /api/books/<id>/delete/` → Delete book (Authenticated)

## Authentication
- Use `Token Authentication` (DRF’s default)
- Ensure you include `Authorization: Token <your_token>` in your requests.

## Permissions
- Read operations: Public
- Write operations: Restricted to authenticated users
