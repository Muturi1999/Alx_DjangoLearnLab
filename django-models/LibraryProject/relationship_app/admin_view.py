from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from relationship_app.models import UserProfile  # Ensure this import is correct

@login_required
def admin_view(request):
    """Admin-only view"""
    try:
        if request.user.userprofile.role != "Admin":  # Ensure 'role' is the correct field name
            return HttpResponseForbidden("You do not have permission to access this page.")
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("User profile not found.")

    return render(request, "relationship_app/admin_dashboard.html")
