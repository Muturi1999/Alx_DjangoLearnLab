from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    """View accessible only to users with the 'Member' role."""
    return render(request, 'relationship_app/member_dashboard.html')
