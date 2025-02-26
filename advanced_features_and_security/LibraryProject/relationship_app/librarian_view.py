from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.userprofile.role == "Librarian")
def librarian_view(request):
    return render(request, "relationship_app/librarian_dashboard.html")
