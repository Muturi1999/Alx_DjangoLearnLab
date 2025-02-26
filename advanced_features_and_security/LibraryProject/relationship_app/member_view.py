from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.userprofile.role == "Member")
def member_view(request):
    return render(request, "relationship_app/member_dashboard.html")
