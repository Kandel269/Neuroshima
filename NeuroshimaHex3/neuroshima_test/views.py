from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def greeting_view(request):
    return HttpResponse("witaj w witrynie neuroshimka xdd")

@login_required
def greeting_view_user(request):
    user = request.user
    return HttpResponse(f"Witaj w neuroszimce {user}")