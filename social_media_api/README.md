# Social Media API
A Django REST Framework-based Social Media API with user authentication and profile management.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- virtualenv

### Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

   pip install -r requirements.txt

4. Run migrations:

   python3 manage.py makemigrations
   python3 manage.py migrate
   
5. Start the development server:

   python3 manage.py runserver
   

## API Endpoints
- `/api/accounts/register/`: User registration
- `/api/accounts/login/`: User login (Token authentication)
- `/api/accounts/profile/`: User profile management

## Authentication
Uses Token-based authentication. On successful login/registration, a token is returned.