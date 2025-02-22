from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

@login_required
@user_passes_test(lambda u: u.userprofile.role == "Admin")
def admin_view(request):
    return render(request, "relationship_app/admin_dashboard.html")
