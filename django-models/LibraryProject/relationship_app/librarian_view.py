from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    """View accessible only to users with the 'Librarian' role."""
    return render(request, 'relationship_app/librarian_dashboard.html')
