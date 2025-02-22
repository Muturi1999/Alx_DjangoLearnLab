from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, "relationship_app/member_dashboard.html")
