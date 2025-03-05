## Authentication & Permissions

This API uses **Token Authentication**.

### Getting a Token
1. Register or login to an account.
2. Send a `POST` request to `/api/api-token-auth/` with:
   ```json
   {
       "username": "your_username",
       "password": "your_password"
   }
