from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, "relationship_app/librarian_dashboard.html")
