# LibraryProject
# Security Enhancements in LibraryProject

## Implemented Security Measures

### 1. Secure Settings
- Set `DEBUG=False`
- Configured `ALLOWED_HOSTS`
- Enabled `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`
- Configured `SECURE_HSTS_SECONDS`
- Added `X_FRAME_OPTIONS = 'DENY'` for clickjacking protection

### 2. CSRF Protection
- Added `{% csrf_token %}` to all forms.

### 3. Secure Database Access
- Used Django ORM instead of raw SQL.
- Validated user inputs with Django forms.

### 4. Content Security Policy (CSP)
- Installed `django-csp` and configured allowed sources.

## Testing
- Manually tested form submissions and ensured CSRF protection.
- Used Django’s `runserver` to confirm CSP headers are applied.
